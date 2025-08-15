# Local Docker Usage Guide

## Quick Start

1. **Setup (one-time)**:
   ```bash
   # Windows
   docker-setup.bat
   
   # Linux/Mac
   ./docker-setup.sh
   ```

2. **Edit `.env` file** with your API keys:
   ```
   OPENAI_API_KEY=sk-your-openai-key-here
   SERPER_API_KEY=your-serper-key-here
   ```

3. **Run the application**:
   ```bash
   docker-compose up --build
   ```

## Common Commands

### Build and Run
```bash
# Build and run (first time or after code changes)
docker-compose up --build

# Run in background
docker-compose up -d

# Stop the container
docker-compose down
```

### Development Mode
```bash
# Access shell for development/debugging
docker-compose up dev

# Run specific commands
docker-compose run --rm multi-agent-content-writer python main.py
```

### Maintenance
```bash
# View logs
docker-compose logs

# Clean up unused Docker resources
docker system prune

# Remove all containers and images (fresh start)
docker-compose down --rmi all
```

## How It Works

- **Isolated Environment**: Your app runs in a container, separate from your host system
- **Volume Mapping**: 
  - `./output` → `/app/output` (generated content persists on your machine)
  - `./.env` → `/app/.env` (API keys read from your local file)
- **Interactive Mode**: Container stays open for user input during content generation

## File Structure
```
├── Dockerfile              # Container build instructions
├── docker-compose.yml      # Service orchestration
├── docker-setup.bat        # Windows setup script
├── docker-setup.sh         # Linux/Mac setup script
├── .dockerignore           # Files to exclude from container
└── .env                    # Your API keys (created by setup script)
```

## Troubleshooting

**Container won't start?**
- Check if Docker Desktop is running
- Verify `.env` file exists with valid API keys

**Permission errors?**
- On Linux/Mac: `chmod +x docker-setup.sh`

**Port conflicts?**
- Change the port in docker-compose.yml if needed

**Need fresh start?**
```bash
docker-compose down --rmi all
docker-compose up --build
```
