#!/bin/bash

# Docker Setup Script for Multi-Agent Content Writer
echo "🐳 Setting up Multi-Agent Content Writer with Docker"
echo "=" * 60

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

echo "✅ Docker is installed"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        echo "📝 Creating .env file from template..."
        cp .env.example .env
        echo "⚠️  Please edit .env file and add your API keys before running the container"
    else
        echo "❌ .env.example file not found"
        exit 1
    fi
else
    echo "✅ .env file already exists"
fi

# Create output directory if it doesn't exist
mkdir -p output

echo ""
echo "🎉 Docker setup completed!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your API keys:"
echo "   - OPENAI_API_KEY=your_key_here"
echo "   - SERPER_API_KEY=your_key_here (optional)"
echo ""
echo "2. Build and run the container:"
echo "   docker-compose up --build"
echo ""
echo "3. For development mode:"
echo "   docker-compose up dev"
echo ""
echo "4. To run specific commands:"
echo "   docker-compose run --rm multi-agent-content-writer python main.py"
echo ""
echo "For API key help:"
echo "- OpenAI: https://platform.openai.com/api-keys"
echo "- Serper: https://serper.dev/api-key"
