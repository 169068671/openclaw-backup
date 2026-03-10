#!/usr/bin/env python3
"""
豆瓣详情获取脚本
获取电影/书籍/音乐的详细信息
"""

import sys
import json
import argparse
import re
from typing import Dict, Any

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("错误：需要安装 requests 和 beautifulsoup4 库")
    print("运行：pip3 install --user requests beautifulsoup4")
    sys.exit(1)


def get_movie_detail(movie_id: str) -> Dict[str, Any]:
    """
    获取电影详情

    Args:
        movie_id: 电影 ID

    Returns:
        电影详细信息
    """
    url = f"https://movie.douban.com/subject/{movie_id}/"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取基本信息
        detail = {
            "type": "电影",
            "id": movie_id,
            "url": url,
        }

        # 标题
        title_elem = soup.find('span', property='v:itemreviewed')
        if title_elem:
            detail["title"] = title_elem.get_text(strip=True)
        else:
            title_elem = soup.find('h1')
            detail["title"] = title_elem.get_text(strip=True) if title_elem else "未知"

        # 评分
        rating_elem = soup.find('strong', class_='ll rating_num')
        detail["rating"] = rating_elem.get_text(strip=True) if rating_elem else "N/A"

        # 评分人数
        rating_people_elem = soup.find('span', property='v:votes')
        detail["rating_count"] = rating_people_elem.get_text(strip=True) if rating_people_elem else "N/A"

        # 年份
        year_elem = soup.find('span', class_='year')
        detail["year"] = year_elem.get_text(strip=True) if year_elem else "N/A"

        # 导演
        directors = []
        for director in soup.find_all('a', rel='v:directedBy'):
            directors.append(director.get_text(strip=True))
        detail["director"] = ", ".join(directors) if directors else "N/A"

        # 主演
        casts = []
        for cast in soup.find_all('a', rel='v:starring'):
            casts.append(cast.get_text(strip=True))
        detail["cast"] = ", ".join(casts) if casts else "N/A"

        # 类型
        genres = []
        for genre in soup.find_all('span', property='v:genre'):
            genres.append(genre.get_text(strip=True))
        detail["genre"] = ", ".join(genres) if genres else "N/A"

        # 国家/地区
        country_elem = soup.find('span', class_='pl', string=lambda x: x and '制片国家' in x if x else None)
        if country_elem and country_elem.next_sibling:
            detail["country"] = country_elem.next_sibling.get_text(strip=True)
        else:
            detail["country"] = "N/A"

        # 简介
        summary_elem = soup.find('span', property='v:summary')
        detail["summary"] = summary_elem.get_text(strip=True) if summary_elem else "N/A"

        # 短评（热门）
        short_comments = []
        for comment in soup.find_all('span', class_='short')[:3]:
            short_comments.append(comment.get_text(strip=True))
        detail["short_comments"] = short_comments

        return detail

    except requests.exceptions.RequestException as e:
        print(f"错误：请求失败 - {e}")
        return {}
    except Exception as e:
        print(f"错误：解析失败 - {e}")
        return {}


def get_book_detail(book_id: str) -> Dict[str, Any]:
    """
    获取书籍详情

    Args:
        book_id: 书籍 ID

    Returns:
        书籍详细信息
    """
    url = f"https://book.douban.com/subject/{book_id}/"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取基本信息
        detail = {
            "type": "书籍",
            "id": book_id,
            "url": url,
        }

        # 标题
        title_elem = soup.find('h1')
        detail["title"] = title_elem.get_text(strip=True) if title_elem else "未知"

        # 评分
        rating_elem = soup.find('strong', class_='ll rating_num')
        detail["rating"] = rating_elem.get_text(strip=True) if rating_elem else "N/A"

        # 评分人数
        rating_people_elem = soup.find('span', property='v:votes')
        detail["rating_count"] = rating_people_elem.get_text(strip=True) if rating_people_elem else "N/A"

        # 作者
        authors = []
        for author in soup.find_all('span', class_='pl', string=lambda x: x and '作者:' in x if x else None):
            if author.next_sibling:
                for a in author.next_sibling.find_all('a'):
                    authors.append(a.get_text(strip=True))
        detail["author"] = ", ".join(authors) if authors else "N/A"

        # 出版社
        publisher_elem = soup.find('span', class_='pl', string=lambda x: x and '出版社:' in x if x else None)
        if publisher_elem and publisher_elem.next_sibling:
            detail["publisher"] = publisher_elem.next_sibling.get_text(strip=True)
        else:
            detail["publisher"] = "N/A"

        # 出版年
        pubdate_elem = soup.find('span', class_='pl', string=lambda x: x and '出版年:' in x if x else None)
        if pubdate_elem and pubdate_elem.next_sibling:
            detail["publish_date"] = pubdate_elem.next_sibling.get_text(strip=True)
        else:
            detail["publish_date"] = "N/A"

        # 简介
        summary_elem = soup.find('div', id='link-report')
        if summary_elem:
            summary_text = summary_elem.get_text(strip=True)
            detail["summary"] = summary_text[:500] if len(summary_text) > 500 else summary_text
        else:
            detail["summary"] = "N/A"

        # 短评（热门）
        short_comments = []
        for comment in soup.find_all('span', class_='short')[:3]:
            short_comments.append(comment.get_text(strip=True))
        detail["short_comments"] = short_comments

        return detail

    except requests.exceptions.RequestException as e:
        print(f"错误：请求失败 - {e}")
        return {}
    except Exception as e:
        print(f"错误：解析失败 - {e}")
        return {}


def get_music_detail(music_id: str) -> Dict[str, Any]:
    """
    获取音乐详情

    Args:
        music_id: 音乐 ID

    Returns:
        音乐详细信息
    """
    url = f"https://music.douban.com/subject/{music_id}/"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取基本信息
        detail = {
            "type": "音乐",
            "id": music_id,
            "url": url,
        }

        # 标题
        title_elem = soup.find('h1')
        detail["title"] = title_elem.get_text(strip=True) if title_elem else "未知"

        # 评分
        rating_elem = soup.find('strong', class_='ll rating_num')
        detail["rating"] = rating_elem.get_text(strip=True) if rating_elem else "N/A"

        # 评分人数
        rating_people_elem = soup.find('span', property='v:votes')
        detail["rating_count"] = rating_people_elem.get_text(strip=True) if rating_people_elem else "N/A"

        # 歌手
        artists = []
        for artist in soup.find_all('span', class_='pl', string=lambda x: x and '表演者:' in x if x else None):
            if artist.next_sibling:
                for a in artist.next_sibling.find_all('a'):
                    artists.append(a.get_text(strip=True))
        detail["artist"] = ", ".join(artists) if artists else "N/A"

        # 类型
        genres = []
        for genre in soup.find_all('span', property='v:genre'):
            genres.append(genre.get_text(strip=True))
        detail["genre"] = ", ".join(genres) if genres else "N/A"

        # 简介
        summary_elem = soup.find('div', id='link-report')
        if summary_elem:
            summary_text = summary_elem.get_text(strip=True)
            detail["summary"] = summary_text[:500] if len(summary_text) > 500 else summary_text
        else:
            detail["summary"] = "N/A"

        # 短评（热门）
        short_comments = []
        for comment in soup.find_all('span', class_='short')[:3]:
            short_comments.append(comment.get_text(strip=True))
        detail["short_comments"] = short_comments

        return detail

    except requests.exceptions.RequestException as e:
        print(f"错误：请求失败 - {e}")
        return {}
    except Exception as e:
        print(f"错误：解析失败 - {e}")
        return {}


def print_detail(detail: Dict[str, Any]):
    """
    打印详情信息

    Args:
        detail: 详情字典
    """
    if not detail:
        print("未获取到详细信息")
        return

    print(f"\n{'='*60}")
    print(f"【{detail['type']}】{detail['title']}")
    print(f"{'='*60}")
    print(f"豆瓣评分：{detail.get('rating', 'N/A')} ({detail.get('rating_count', 'N/A')} 人评价)")
    print(f"链接：{detail.get('url', 'N/A')}")

    if detail.get('type') == '电影':
        if detail.get('year'):
            print(f"年份：{detail['year']}")
        if detail.get('director'):
            print(f"导演：{detail['director']}")
        if detail.get('cast'):
            print(f"主演：{detail['cast']}")
        if detail.get('genre'):
            print(f"类型：{detail['genre']}")
        if detail.get('country'):
            print(f"制片国家：{detail['country']}")

    elif detail.get('type') == '书籍':
        if detail.get('author'):
            print(f"作者：{detail['author']}")
        if detail.get('publisher'):
            print(f"出版社：{detail['publisher']}")
        if detail.get('publish_date'):
            print(f"出版时间：{detail['publish_date']}")

    elif detail.get('type') == '音乐':
        if detail.get('artist'):
            print(f"歌手：{detail['artist']}")
        if detail.get('genre'):
            print(f"类型：{detail['genre']}")

    # 简介
    if detail.get('summary') and detail['summary'] != 'N/A':
        print(f"\n简介：")
        print(f"{detail['summary']}")

    # 短评
    if detail.get('short_comments'):
        print(f"\n热门短评：")
        for i, comment in enumerate(detail['short_comments'], 1):
            print(f"  {i}. {comment}")

    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description="豆瓣详情获取工具")
    parser.add_argument("id", help="作品 ID（电影/书籍/音乐 ID）")
    parser.add_argument("-t", "--type", choices=["movie", "book", "music"], default="movie",
                        help="作品类型（默认：movie）")
    parser.add_argument("-j", "--json", action="store_true",
                        help="输出 JSON 格式")

    args = parser.parse_args()

    # 根据类型获取详情
    if args.type == "movie":
        detail = get_movie_detail(args.id)
    elif args.type == "book":
        detail = get_book_detail(args.id)
    elif args.type == "music":
        detail = get_music_detail(args.id)

    # 输出结果
    if args.json:
        print(json.dumps(detail, ensure_ascii=False, indent=2))
    else:
        print_detail(detail)


if __name__ == "__main__":
    main()
