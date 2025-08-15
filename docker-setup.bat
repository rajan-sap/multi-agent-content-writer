@echo off
REM Docker Setup Script for Multi-Agent Content Writer (Windows)
echo 🐳 Setting up Multi-Agent Content Writer with Docker
echo ============================================================

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed. Please install Docker Desktop first.
    echo    Visit: https://docs.docker.com/desktop/windows/
    pause
    exit /b 1
)

echo ✅ Docker is installed

REM Create .env file if it doesn't exist
if not exist .env (
    if exist .env.example (
        echo 📝 Creating .env file from template...
        copy .env.example .env
        echo ⚠️  Please edit .env file and add your API keys before running the container
    ) else (
        echo ❌ .env.example file not found
        pause
        exit /b 1
    )
) else (
    echo ✅ .env file already exists
)

REM Create output directory if it doesn't exist
if not exist output mkdir output

echo.
echo 🎉 Docker setup completed!
echo.
echo Next steps:
echo 1. Edit .env file and add your API keys:
echo    - OPENAI_API_KEY=your_key_here
echo    - SERPER_API_KEY=your_key_here (optional)
echo.
echo 2. Build and run the container:
echo    docker-compose up --build
echo.
echo 3. For development mode:
echo    docker-compose up dev
echo.
echo 4. To run specific commands:
echo    docker-compose run --rm multi-agent-content-writer python main.py
echo.
echo For API key help:
echo - OpenAI: https://platform.openai.com/api-keys
echo - Serper: https://serper.dev/api-key

pause
