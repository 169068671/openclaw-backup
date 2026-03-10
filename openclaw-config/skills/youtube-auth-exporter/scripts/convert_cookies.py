#!/usr/bin/env python3
"""
Convert Netscape cookie file to Playwright storage_state.json format.

This script converts cookies exported by browser-cookies-exporter
(Netscape format) into Playwright's storage_state.json format.
"""

import json
import http.cookiejar as cj
import argparse
from pathlib import Path


def convert_netscape_to_storage_state(cookie_file_path):
    """
    Convert Netscape cookie file to Playwright storage_state.json.

    Args:
        cookie_file_path: Path to Netscape cookie file

    Returns:
        dict: Playwright storage_state.json format
    """
    # Load Netscape cookies
    cookie_jar = cj.MozillaCookieJar(cookie_file_path)
    cookie_jar.load(ignore_discard=True, ignore_expires=True)

    # Convert to Playwright format
    playwright_cookies = []
    for cookie in cookie_jar:
        # Convert expiration time to float or -1
        expires = float(cookie.expires) if cookie.expires and cookie.expires > 0 else -1

        playwright_cookie = {
            "name": cookie.name,
            "value": cookie.value,
            "domain": cookie.domain,
            "path": cookie.path,
            "expires": expires,
            "httpOnly": False,
            "secure": cookie.secure,
            "sameSite": "Lax"  # Default value
        }
        playwright_cookies.append(playwright_cookie)

    # Create storage_state.json format
    # Include common origins for Google services
    storage_state = {
        "cookies": playwright_cookies,
        "origins": [
            {
                "origin": "https://notebooklm.google.com",
                "localStorage": []
            },
            {
                "origin": "https://accounts.google.com",
                "localStorage": []
            },
            {
                "origin": "https://www.google.com",
                "localStorage": []
            }
        ]
    }

    return storage_state


def main():
    parser = argparse.ArgumentParser(
        description="Convert Netscape cookie file to Playwright storage_state.json"
    )
    parser.add_argument(
        "input_file",
        help="Input Netscape cookie file path"
    )
    parser.add_argument(
        "output_file",
        help="Output Playwright storage_state.json file path"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed output"
    )

    args = parser.parse_args()

    # Validate input file exists
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"❌ Error: Input file not found: {args.input_file}")
        return 1

    # Convert cookies
    try:
        storage_state = convert_netscape_to_storage_state(args.input_file)
    except Exception as e:
        print(f"❌ Error converting cookies: {e}")
        return 1

    # Save to JSON
    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(storage_state, f, indent=2)
    except Exception as e:
        print(f"❌ Error saving output file: {e}")
        return 1

    # Success!
    cookie_count = len(storage_state['cookies'])
    print(f"✅ 转换完成！")
    print(f"📁 输入文件: {args.input_file}")
    print(f"📁 输出文件: {args.output_file}")
    print(f"🍪 Cookies 数量: {cookie_count}")

    if args.verbose:
        print("\n" + "=" * 60)
        print("Cookies (first 5):")
        print("=" * 60)
        for i, cookie in enumerate(storage_state['cookies'][:5], 1):
            print(f"{i}. {cookie['name']}: {cookie['domain']}")
        if cookie_count > 5:
            print(f"... and {cookie_count - 5} more")
        print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
