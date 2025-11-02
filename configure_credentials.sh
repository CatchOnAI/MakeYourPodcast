#!/bin/bash

# Alibaba Cloud Credentials Configuration Script

echo "🔐 Alibaba Cloud Credentials Configuration"
echo "==========================================="
echo ""
echo "Please get your credentials from:"
echo "https://ram.console.aliyun.com/users"
echo "or"
echo "https://usercenter.console.aliyun.com/#/manage/ak"
echo ""

# Prompt for credentials
read -p "Enter your Access Key ID: " access_key_id
read -sp "Enter your Access Key Secret: " access_key_secret
echo ""
echo ""

if [ -z "$access_key_id" ] || [ -z "$access_key_secret" ]; then
    echo "❌ Error: Both Access Key ID and Secret are required!"
    exit 1
fi

# Create credentials directory
mkdir -p ~/.alibabacloud

# Write credentials file
cat > ~/.alibabacloud/credentials.ini << EOF
[default]
type = access_key
access_key_id = ${access_key_id}
access_key_secret = ${access_key_secret}
EOF

echo "✅ Credentials saved to ~/.alibabacloud/credentials.ini"
echo ""

# Also export for current session
export ALIBABA_CLOUD_ACCESS_KEY_ID="${access_key_id}"
export ALIBABA_CLOUD_ACCESS_KEY_SECRET="${access_key_secret}"

echo "✅ Environment variables set for current session"
echo ""

# Suggest adding to shell config
echo "📝 To make these permanent, add to your shell config:"
echo ""

if [ -n "$FISH_VERSION" ] || [ "$SHELL" = "/opt/homebrew/bin/fish" ]; then
    echo "For Fish shell (~/.config/fish/config.fish):"
    echo "----------------------------------------"
    echo "set -gx ALIBABA_CLOUD_ACCESS_KEY_ID \"${access_key_id}\""
    echo "set -gx ALIBABA_CLOUD_ACCESS_KEY_SECRET \"${access_key_secret}\""
else
    echo "For Bash/Zsh (~/.bashrc or ~/.zshrc):"
    echo "----------------------------------------"
    echo "export ALIBABA_CLOUD_ACCESS_KEY_ID=\"${access_key_id}\""
    echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET=\"${access_key_secret}\""
fi

echo ""
echo "🎉 Configuration complete!"
echo ""
echo "You can now run: python create_podcast.py"


