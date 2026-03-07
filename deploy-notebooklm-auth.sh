#!/bin/bash
# deploy-notebooklm-auth.sh
# Deploy NotebookLM authentication file to server

# Configuration
SERVER="root@76.13.219.143"
PASSWORD="Whj001.Whj001"
LOCAL_FILE="/tmp/storage_state.json"
REMOTE_PATH="/root/.notebooklm/storage_state.json"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "  NotebookLM Auth Deployment"
echo "========================================"
echo ""
echo "Target Server: $SERVER"
echo "Local File:   $LOCAL_FILE"
echo "Remote Path:  $REMOTE_PATH"
echo ""

# Check if local file exists
if [ ! -f "$LOCAL_FILE" ]; then
    echo -e "${RED}❌ Error: Local file not found: $LOCAL_FILE${NC}"
    echo "Please generate storage_state.json first:"
    echo "  1. browser-cookies-exporter .google.com /tmp/google-cookies.txt"
    echo "  2. python3 ~/.openclaw/skills/notebooklm-auth-exporter/scripts/convert_cookies.py /tmp/google-cookies.txt /tmp/storage_state.json"
    exit 1
fi

echo -e "${YELLOW}📤 Deploying to server...${NC}"

# Create directory on server
echo "Creating directory..."
sshpass -p "$PASSWORD" ssh "$SERVER" "mkdir -p /root/.notebooklm" 2>/dev/null

# Copy file
echo "Copying file..."
sshpass -p "$PASSWORD" scp "$LOCAL_FILE" "$SERVER:$REMOTE_PATH" 2>/dev/null

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to copy file${NC}"
    exit 1
fi

# Verify file exists on server
echo "Verifying deployment..."
FILE_INFO=$(sshpass -p "$PASSWORD" ssh "$SERVER" "ls -lh $REMOTE_PATH 2>/dev/null")

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to verify file on server${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Deployment successful!${NC}"
echo ""
echo "Server file info:"
echo "$FILE_INFO"
echo ""

# Test authentication
echo -e "${YELLOW}🧪 Testing authentication...${NC}"
TEST_RESULT=$(sshpass -p "$PASSWORD" ssh "$SERVER" "python3 -c \"
import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state='$REMOTE_PATH')
        page = await context.new_page()
        await page.goto('https://notebooklm.google.com/', timeout=60000)
        title = await page.title()
        await browser.close()
        print(title)

asyncio.run(test())
\" 2>/dev/null")

if [ $? -eq 0 ] && [ "$TEST_RESULT" = "NotebookLM" ]; then
    echo -e "${GREEN}✅ Authentication test PASSED!${NC}"
else
    echo -e "${RED}❌ Authentication test FAILED${NC}"
    echo "Result: $TEST_RESULT"
fi

echo ""
echo "========================================"
echo "  Deployment Complete"
echo "========================================"
