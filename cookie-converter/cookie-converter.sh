#!/bin/bash
# Cookie Format Converter - CLI wrapper

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONVERT_SCRIPT="$SCRIPT_DIR/scripts/convert_cookies.py"

# Check if Python script exists
if [ ! -f "$CONVERT_SCRIPT" ]; then
    echo "❌ Error: Converter script not found: $CONVERT_SCRIPT"
    exit 1
fi

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    exit 1
fi

# Show help if no arguments
if [ $# -eq 0 ]; then
    echo "🍪 Cookie Format Converter"
    echo ""
    echo "Usage: cookie-converter <conversion_type> <input_file> <output_file> [options]"
    echo ""
    echo "Conversion types:"
    echo "  netscape-to-playwright    Netscape → Playwright storage_state.json"
    echo "  playwright-to-netscape    Playwright → Netscape cookie file"
    echo "  netscape-to-json          Netscape → JSON array"
    echo "  json-to-netscape          JSON array → Netscape"
    echo "  playwright-to-json        Playwright → JSON array"
    echo "  json-to-playwright        JSON array → Playwright"
    echo ""
    echo "Options:"
    echo "  -v, --verbose            Show detailed output"
    echo ""
    echo "Examples:"
    echo "  cookie-converter netscape-to-playwright cookies.txt storage.json"
    echo "  cookie-converter playwright-to-netscape storage.json cookies.txt"
    echo "  cookie-converter netscape-to-json cookies.txt cookies.json -v"
    echo ""
    echo "Full documentation: $SCRIPT_DIR/SKILL.md"
    exit 0
fi

# Run the converter
python3 "$CONVERT_SCRIPT" "$@"

exit $?
