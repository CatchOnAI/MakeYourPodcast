#!/bin/bash

# Setup script for AI Podcast Creator

echo "🎙️  Setting up AI Podcast Creator..."
echo ""

# Create log directory
echo "Creating log directory..."
mkdir -p log
echo "✓ Log directory created"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Set environment variables if not already set
if [ -z "$ALIBABA_WORKSPACE_ID" ]; then
    echo ""
    echo "Setting ALIBABA_WORKSPACE_ID..."
    export ALIBABA_WORKSPACE_ID="llm-dhanwfov9gf37wez"
    echo "✓ ALIBABA_WORKSPACE_ID set"
fi

if [ -z "$AGENT_KEY" ]; then
    echo "Setting AGENT_KEY..."
    export AGENT_KEY="619d235c738a483088ac2830e69189be_p_efm"
    echo "✓ AGENT_KEY set"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "You can now run the examples:"
echo "  python create_podcast.py              # Run the default example"
echo "  python examples/simple_example.py     # Run simple example"
echo "  python examples/custom_podcast.py     # Run custom examples"
echo ""
echo "For more information, see PODCAST_README.md"


