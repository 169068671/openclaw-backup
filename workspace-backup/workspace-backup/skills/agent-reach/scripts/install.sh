#!/bin/bash
# Agent Reach Installation Script
# This script installs agent-reach and all its dependencies

set -e

echo "🚀 Installing Agent Reach..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    exit 1
fi

# Install agent-reach
echo "📦 Installing agent-reach via pip..."
pip3 install agent-reach

# Install Node.js if not available (for xreach)
if ! command -v node &> /dev/null; then
    echo "📦 Installing Node.js (required for xreach)..."
    curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Install xreach CLI globally (for Twitter/X)
if ! command -v xreach &> /dev/null; then
    echo "📦 Installing xreach CLI (for Twitter/X)..."
    npm install -g xreach-cli
fi

# Install undici (required by xreach)
npm install -g undici

# Install FFmpeg (for video/audio processing)
if ! command -v ffmpeg &> /dev/null; then
    echo "📦 Installing FFmpeg (for video/audio)..."
    sudo apt-get update
    sudo apt-get install -y ffmpeg
fi

# Install gh CLI (for GitHub)
if ! command -v gh &> /dev/null; then
    echo "📦 Installing gh CLI (for GitHub)..."
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
    sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
    sudo apt-get update
    sudo apt-get install -y gh
fi

# Install feedparser (for RSS)
echo "📦 Installing feedparser (for RSS)..."
pip3 install feedparser

# Install mcporter (for小红书, 抖音, LinkedIn, Boss直聘)
if ! command -v mcporter &> /dev/null; then
    echo "📦 Installing mcporter (for 小红书, 抖音, LinkedIn, Boss直聘)..."
    npm install -g @mcporter/mcporter
fi

# Create config directory
mkdir -p ~/.agent-reach

# Run doctor to check status
echo "🔍 Checking installation status..."
agent-reach doctor

echo ""
echo "✅ Agent Reach installation complete!"
echo ""
echo "Next steps:"
echo "1. Run 'agent-reach doctor' to check which channels are available"
echo "2. Configure channels that need authentication (Twitter, 小红书, etc.)"
echo "3. See SKILL.md for usage examples"
echo ""
