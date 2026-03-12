#!/usr/bin/env python3
"""
Cookie Format Converter - Bidirectional conversion between formats.

Supports:
- Netscape ↔ Playwright storage_state.json
- Netscape ↔ JSON (simple array)
- Playwright ↔ JSON (simple array)

Usage:
  python3 convert_cookies.py netscape-to-playwright cookies.txt storage.json
  python3 convert_cookies.py playwright-to-netscape storage.json cookies.txt
  python3 convert_cookies.py netscape-to-json cookies.txt cookies.json
"""

import json
import http.cookiejar as cj
import argparse
from pathlib import Path
from typing import Dict, List


def netscape_to_playwright(cookie_file_path: str) -> Dict:
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
    storage_state = {
        "cookies": playwright_cookies,
        "origins": []
    }

    return storage_state


def playwright_to_netscape(storage_state_path: str) -> cj.MozillaCookieJar:
    """
    Convert Playwright storage_state.json to Netscape cookie file.

    Args:
        storage_state_path: Path to Playwright storage_state.json

    Returns:
        cj.MozillaCookieJar: Netscape cookie jar
    """
    # Load Playwright storage state
    with open(storage_state_path, 'r', encoding='utf-8') as f:
        storage_state = json.load(f)

    # Convert to Netscape format
    cookie_jar = cj.MozillaCookieJar()

    for p_cookie in storage_state.get('cookies', []):
        # Convert Playwright cookie to http.cookiejar.Cookie
        c = cj.Cookie(
            version=0,
            name=p_cookie.get('name', ''),
            value=p_cookie.get('value', ''),
            port=None,
            port_specified=False,
            domain=p_cookie.get('domain', ''),
            domain_specified=True,
            domain_initial_dot=p_cookie.get('domain', '').startswith('.'),
            path=p_cookie.get('path', '/'),
            path_specified=True,
            secure=p_cookie.get('secure', False),
            expires=p_cookie.get('expires', -1),
            discard=False,
            comment=None,
            comment_url=None,
            rest={},
            rfc2109=False
        )
        cookie_jar.set_cookie(c)

    return cookie_jar


def netscape_to_json(cookie_file_path: str) -> List[Dict]:
    """
    Convert Netscape cookie file to simple JSON array.

    Args:
        cookie_file_path: Path to Netscape cookie file

    Returns:
        list: Array of cookie dictionaries
    """
    cookie_jar = cj.MozillaCookieJar(cookie_file_path)
    cookie_jar.load(ignore_discard=True, ignore_expires=True)

    cookies = []
    for cookie in cookie_jar:
        cookies.append({
            "name": cookie.name,
            "value": cookie.value,
            "domain": cookie.domain,
            "path": cookie.path,
            "expires": cookie.expires if cookie.expires and cookie.expires > 0 else None,
            "secure": cookie.secure
        })

    return cookies


def json_to_netscape(json_path: str) -> cj.MozillaCookieJar:
    """
    Convert simple JSON array to Netscape cookie file.

    Args:
        json_path: Path to JSON file

    Returns:
        cj.MozillaCookieJar: Netscape cookie jar
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        cookies_data = json.load(f)

    cookie_jar = cj.MozillaCookieJar()

    for cookie_data in cookies_data:
        c = cj.Cookie(
            version=0,
            name=cookie_data.get('name', ''),
            value=cookie_data.get('value', ''),
            port=None,
            port_specified=False,
            domain=cookie_data.get('domain', ''),
            domain_specified=True,
            domain_initial_dot=cookie_data.get('domain', '').startswith('.'),
            path=cookie_data.get('path', '/'),
            path_specified=True,
            secure=cookie_data.get('secure', False),
            expires=cookie_data.get('expires', -1) or -1,
            discard=False,
            comment=None,
            comment_url=None,
            rest={},
            rfc2109=False
        )
        cookie_jar.set_cookie(c)

    return cookie_jar


def playwright_to_json(storage_state_path: str) -> List[Dict]:
    """
    Convert Playwright storage_state.json to simple JSON array.

    Args:
        storage_state_path: Path to Playwright storage_state.json

    Returns:
        list: Array of cookie dictionaries
    """
    with open(storage_state_path, 'r', encoding='utf-8') as f:
        storage_state = json.load(f)

    return storage_state.get('cookies', [])


def json_to_playwright(json_path: str) -> Dict:
    """
    Convert simple JSON array to Playwright storage_state.json.

    Args:
        json_path: Path to JSON file

    Returns:
        dict: Playwright storage_state.json format
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        cookies_data = json.load(f)

    # Ensure each cookie has required fields
    playwright_cookies = []
    for cookie in cookies_data:
        playwright_cookie = {
            "name": cookie.get('name', ''),
            "value": cookie.get('value', ''),
            "domain": cookie.get('domain', ''),
            "path": cookie.get('path', '/'),
            "expires": cookie.get('expires', -1),
            "httpOnly": cookie.get('httpOnly', False),
            "secure": cookie.get('secure', False),
            "sameSite": cookie.get('sameSite', 'Lax')
        }
        playwright_cookies.append(playwright_cookie)

    return {
        "cookies": playwright_cookies,
        "origins": []
    }


def main():
    parser = argparse.ArgumentParser(
        description="Bidirectional cookie format converter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Netscape → Playwright
  python3 convert_cookies.py netscape-to-playwright cookies.txt storage.json

  # Playwright → Netscape
  python3 convert_cookies.py playwright-to-netscape storage.json cookies.txt

  # Netscape → JSON
  python3 convert_cookies.py netscape-to-json cookies.txt cookies.json

  # JSON → Netscape
  python3 convert_cookies.py json-to-netscape cookies.json cookies.txt

  # Playwright → JSON
  python3 convert_cookies.py playwright-to-json storage.json cookies.json

  # JSON → Playwright
  python3 convert_cookies.py json-to-playwright cookies.json storage.json
        """
    )

    parser.add_argument(
        "conversion_type",
        choices=[
            'netscape-to-playwright',
            'playwright-to-netscape',
            'netscape-to-json',
            'json-to-netscape',
            'playwright-to-json',
            'json-to-playwright'
        ],
        help="Conversion type"
    )

    parser.add_argument(
        "input_file",
        help="Input file path"
    )

    parser.add_argument(
        "output_file",
        help="Output file path"
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

    # Perform conversion
    try:
        if args.conversion_type == 'netscape-to-playwright':
            result = netscape_to_playwright(args.input_file)
            with open(args.output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            cookie_count = len(result['cookies'])

        elif args.conversion_type == 'playwright-to-netscape':
            result = playwright_to_netscape(args.input_file)
            result.save(args.output_file)
            cookie_count = len(result)

        elif args.conversion_type == 'netscape-to-json':
            result = netscape_to_json(args.input_file)
            with open(args.output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            cookie_count = len(result)

        elif args.conversion_type == 'json-to-netscape':
            result = json_to_netscape(args.input_file)
            result.save(args.output_file)
            cookie_count = len(result)

        elif args.conversion_type == 'playwright-to-json':
            result = playwright_to_json(args.input_file)
            with open(args.output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            cookie_count = len(result)

        elif args.conversion_type == 'json-to-playwright':
            result = json_to_playwright(args.input_file)
            with open(args.output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            cookie_count = len(result['cookies'])

    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # Success!
    print(f"✅ 转换完成！")
    print(f"🔄 转换类型: {args.conversion_type}")
    print(f"📁 输入文件: {args.input_file}")
    print(f"📁 输出文件: {args.output_file}")
    print(f"🍪 Cookies 数量: {cookie_count}")

    if args.verbose and cookie_count > 0:
        print("\n" + "=" * 60)
        print("Cookies (first 5):")
        print("=" * 60)

        # Show first 5 cookies
        if args.conversion_type in ['netscape-to-playwright', 'json-to-playwright', 'playwright-to-json']:
            cookies = result.get('cookies', result)
        else:
            cookies = list(result)

        for i, cookie in enumerate(cookies[:5], 1):
            if isinstance(cookie, dict):
                name = cookie.get('name', cookie.get('name', ''))
                domain = cookie.get('domain', '')
            else:
                name = cookie.name
                domain = cookie.domain
            print(f"{i}. {name}: {domain}")

        if cookie_count > 5:
            print(f"... and {cookie_count - 5} more")
        print("=" * 60)

    return 0


if __name__ == "__main__":
    exit(main())
