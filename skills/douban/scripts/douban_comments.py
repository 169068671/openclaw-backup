#!/usr/bin/env python3
"""
豆瓣评论获取脚本
获取电影/书籍/音乐的热门评论
"""

import sys
import json
import argparse
from typing import List, Dict, Any

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("错误：需要安装 requests 和 beautifulsoup4 库")
    print("运行：pip3 install --user requests beautifulsoup4")
    sys.exit(1)


def get_comments(url: str, limit: int = 20) -> List[Dict[str, Any]]:
    """
    获取豆瓣评论

    Args:
        url: 豆瓣作品 URL
        limit: 获取评论数量

    Returns:
        评论列表
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        comments = []

        # 查找评论
        comment_items = soup.find_all('div', class_='comment-item')

        # 限制评论数量
        comment_items = comment_items[:limit]

        for item in comment_items:
            comment = {}

            # 用户
            user_elem = item.find('span', class_='comment-info').find('a')
            if user_elem:
                comment["user"] = user_elem.get_text(strip=True)
                comment["user_url"] = user_elem.get('href', '')
            else:
                comment["user"] = "匿名用户"
                comment["user_url"] = ""

            # 评分
            rating_elem = item.find('span', class_='rating')
            if rating_elem:
                rating = rating_elem.get('title', '')
                # 提取评分数字（如"推荐"对应5星）
                rating_map = {
                    "力荐": 5,
                    "推荐": 4,
                    "还行": 3,
                    "较差": 2,
                    "很差": 1,
                }
                comment["rating"] = rating_map.get(rating, 0)
            else:
                comment["rating"] = 0

            # 时间
            time_elem = item.find('span', class_='comment-time')
            comment["time"] = time_elem.get_text(strip=True) if time_elem else "N/A"

            # 评论内容
            content_elem = item.find('span', class_='short')
            if content_elem:
                comment["content"] = content_elem.get_text(strip=True)
            else:
                comment["content"] = "N/A"

            # 点赞数
            votes_elem = item.find('span', class_='votes')
            comment["votes"] = votes_elem.get_text(strip=True) if votes_elem else "0"

            comments.append(comment)

        return comments

    except requests.exceptions.RequestException as e:
        print(f"错误：请求失败 - {e}")
        return []
    except Exception as e:
        print(f"错误：解析失败 - {e}")
        return []


def print_comments(comments: List[Dict[str, Any]], show_summary: bool = True):
    """
    打印评论

    Args:
        comments: 评论列表
        show_summary: 是否显示统计摘要
    """
    if not comments:
        print("未找到评论")
        return

    print(f"\n找到 {len(comments)} 条评论：\n")

    # 统计评分分布
    rating_count = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    total_rating = 0
    rated_count = 0

    for i, comment in enumerate(comments, 1):
        print(f"【{i}】{comment['user']}")
        print(f"    时间：{comment['time']}")

        # 显示星级
        rating = comment.get('rating', 0)
        if rating > 0:
            stars = "★" * rating + "☆" * (5 - rating)
            rating_count[rating] += 1
            total_rating += rating
            rated_count += 1
            print(f"    评分：{stars} ({rating}分)")
        else:
            print(f"    评分：未评分")

        print(f"    赞：{comment['votes']}")

        # 评论内容
        content = comment.get('content', 'N/A')
        if content != 'N/A':
            # 限制显示长度
            if len(content) > 200:
                content = content[:200] + "..."
            print(f"    内容：{content}")

        print()

    # 统计摘要
    if show_summary and rated_count > 0:
        print(f"\n{'='*60}")
        print("评分统计")
        print(f"{'='*60}")

        avg_rating = total_rating / rated_count
        print(f"平均评分：{avg_rating:.2f} / 5.0")
        print(f"评分人数：{rated_count}")

        print("\n评分分布：")
        for stars in [5, 4, 3, 2, 1]:
            percentage = (rating_count[stars] / rated_count * 100) if rated_count > 0 else 0
            star_str = "★" * stars + "☆" * (5 - stars)
            print(f"  {star_str} {rating_count[stars]} 人 ({percentage:.1f}%)")


def main():
    parser = argparse.ArgumentParser(description="豆瓣评论获取工具")
    parser.add_argument("url", help="豆瓣作品 URL")
    parser.add_argument("-l", "--limit", type=int, default=20,
                        help="获取评论数量（默认：20）")
    parser.add_argument("-j", "--json", action="store_true",
                        help="输出 JSON 格式")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="简洁输出（不显示统计摘要）")

    args = parser.parse_args()

    # 验证 URL
    if "douban.com" not in args.url:
        print("错误：请提供有效的豆瓣 URL")
        print("示例：https://movie.douban.com/subject/1292052/")
        sys.exit(1)

    # 获取评论
    comments = get_comments(args.url, args.limit)

    # 输出结果
    if args.json:
        print(json.dumps(comments, ensure_ascii=False, indent=2))
    else:
        print_comments(comments, show_summary=not args.quiet)


if __name__ == "__main__":
    main()
