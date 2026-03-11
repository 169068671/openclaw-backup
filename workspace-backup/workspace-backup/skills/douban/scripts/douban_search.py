#!/usr/bin/env python3
"""
豆瓣搜索脚本
支持搜索电影、书籍、音乐
"""

import sys
import json
import argparse
import urllib.parse
from typing import List, Dict, Any

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("错误：需要安装 requests 和 beautifulsoup4 库")
    print("运行：pip3 install --user requests beautifulsoup4")
    sys.exit(1)


# 类别代码
CATEGORY_MOVIE = "1002"  # 电影
CATEGORY_BOOK = "1003"   # 书籍
CATEGORY_MUSIC = "1004"  # 音乐


def search_douban(keyword: str, category: str, limit: int = 10) -> List[Dict[str, Any]]:
    """
    搜索豆瓣（使用豆瓣公开 API）

    Args:
        keyword: 搜索关键词
        category: 类别代码 (1002=电影, 1003=书籍, 1004=音乐)
        limit: 返回结果数量

    Returns:
        搜索结果列表
    """
    # 根据类别构造 URL
    if category == CATEGORY_MOVIE:
        url = "https://movie.douban.com/j/search_subjects"
    elif category == CATEGORY_BOOK:
        url = "https://book.douban.com/j/search_subjects"
    elif category == CATEGORY_MUSIC:
        url = "https://music.douban.com/j/search_subjects"
    else:
        print("错误：不支持的类别")
        return []

    try:
        params = {
            "type": "S",
            "wd": keyword,
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
        }

        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()

        # 豆瓣返回 JSON
        data = response.json()

        # 提取搜索结果
        subjects = data.get("subjects", [])

        # 限制返回数量
        results = subjects[:limit]

        # 格式化结果
        formatted_results = []
        for subject in results:
            formatted = {
                "id": subject.get("id", ""),
                "title": subject.get("title", ""),
                "year": subject.get("year", ""),
                "rating": subject.get("rate", 0),
                "url": f"https://{category_map_reverse.get(category, 'www')}.douban.com/subject/{subject.get('id', '')}",
            }

            # 根据类别添加特定字段
            if category == CATEGORY_MOVIE:
                formatted["director"] = ", ".join([d.get("name", "") for d in subject.get("directors", [])])
                formatted["cast"] = ", ".join([c.get("name", "") for c in subject.get("casts", [])])
                formatted["type"] = "电影"
            elif category == CATEGORY_BOOK:
                formatted["author"] = ", ".join([a.get("name", "") for a in subject.get("authors", [])])
                formatted["publisher"] = subject.get("publisher", "")
                formatted["type"] = "书籍"
            elif category == CATEGORY_MUSIC:
                formatted["artist"] = ", ".join([a.get("name", "") for a in subject.get("artists", [])])
                formatted["type"] = "音乐"

            formatted_results.append(formatted)

        return formatted_results

    except requests.exceptions.RequestException as e:
        print(f"错误：请求失败 - {e}")
        print(f"提示：豆瓣可能限制了访问，请稍后再试或使用代理")
        return []
    except json.JSONDecodeError as e:
        print(f"错误：解析 JSON 失败 - {e}")
        return []
    except Exception as e:
        print(f"错误：未知错误 - {e}")
        return []


# 类别到域名的映射（反向）
category_map_reverse = {
    CATEGORY_MOVIE: "movie",
    CATEGORY_BOOK: "book",
    CATEGORY_MUSIC: "music",
}


def print_results(results: List[Dict[str, Any]], show_details: bool = True):
    """
    打印搜索结果

    Args:
        results: 搜索结果列表
        show_details: 是否显示详细信息
    """
    if not results:
        print("未找到结果")
        return

    print(f"\n找到 {len(results)} 个结果：\n")

    for i, item in enumerate(results, 1):
        print(f"【{i}】{item.get('title', 'N/A')}")

        if item.get('year'):
            print(f"    年份：{item['year']}")

        print(f"    类型：{item.get('type', 'N/A')}")
        print(f"    豆瓣评分：{item.get('rating', 'N/A')}")

        if show_details:
            if item.get('type') == '电影':
                if item.get('director'):
                    print(f"    导演：{item['director']}")
                if item.get('cast'):
                    print(f"    主演：{item['cast']}")
            elif item.get('type') == '书籍':
                if item.get('author'):
                    print(f"    作者：{item['author']}")
                if item.get('publisher'):
                    print(f"    出版社：{item['publisher']}")
            elif item.get('type') == '音乐':
                if item.get('artist'):
                    print(f"    歌手：{item['artist']}")

        if item.get('url'):
            print(f"    链接：{item['url']}")

        print()


def main():
    parser = argparse.ArgumentParser(description="豆瓣搜索工具")
    parser.add_argument("keyword", help="搜索关键词")
    parser.add_argument("-c", "--category", choices=["movie", "book", "music"], default="movie",
                        help="搜索类别（默认：movie）")
    parser.add_argument("-l", "--limit", type=int, default=10,
                        help="返回结果数量（默认：10）")
    parser.add_argument("-j", "--json", action="store_true",
                        help="输出 JSON 格式")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="简洁输出（不显示详细信息）")

    args = parser.parse_args()

    # 映射类别
    category_map = {
        "movie": CATEGORY_MOVIE,
        "book": CATEGORY_BOOK,
        "music": CATEGORY_MUSIC,
    }

    category = category_map[args.category]

    # 执行搜索
    results = search_douban(args.keyword, category, args.limit)

    # 输出结果
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print_results(results, show_details=not args.quiet)


if __name__ == "__main__":
    main()
