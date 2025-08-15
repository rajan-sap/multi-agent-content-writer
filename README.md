# Multi-Agent Content Writer

A sophisticated content generation system using CrewAI framework with multiple specialized agents for research, writing, reviewing, and editing high-quality content.

## Features

- **Research Agent**: Conducts comprehensive research on the given topic
- **Writer Agent**: Creates engaging and well-structured content
- **Reviewer Agent**: Reviews content for accuracy, coherence, and quality
- **Editor Agent**: Performs final editing for grammar, style, and formatting

## Agents Overview

### 1. Research Agent
- **Role**: Content Researcher
- **Goal**: Gather comprehensive and accurate information about the topic
- **Backstory**: Expert researcher with access to various information sources

### 2. Writer Agent
- **Role**: Content Writer
- **Goal**: Create engaging, well-structured, and informative content
- **Backstory**: Professional writer with expertise in various content formats

### 3. Reviewer Agent
- **Role**: Content Reviewer
- **Goal**: Ensure content accuracy, coherence, and quality
- **Backstory**: Senior editor with years of experience in content review

### 4. Editor Agent
- **Role**: Content Editor
- **Goal**: Polish content for grammar, style, and final presentation
- **Backstory**: Meticulous editor focused on perfection and readability

## Installation

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your API keys:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env` file with your actual API keys

## Usage

Run the content writer application:

```bash
python main.py
```

The application will prompt you to enter:
- Topic for content generation
- Content type (article, blog post, report, etc.)
- Target audience
- Word count (optional)

## Project Structure

```
multi-agent-content-writer/
├── main.py                 # Main application entry point
├── agents/                 # Agent definitions
│   ├── __init__.py
│   ├── research_agent.py
│   ├── writer_agent.py
│   ├── reviewer_agent.py
│   └── editor_agent.py
├── tasks/                  # Task definitions
│   ├── __init__.py
│   ├── research_task.py
│   ├── writing_task.py
│   ├── review_task.py
│   └── editing_task.py
├── tools/                  # Custom tools
│   ├── __init__.py
│   └── search_tools.py
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── file_utils.py
├── output/                 # Generated content output
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md             # This file
```

## API Keys Required

- **OpenAI API Key**: For LLM capabilities
- **Serper API Key**: For web search functionality (optional but recommended)

## Output

Generated content will be saved in the `output/` directory with timestamps and topic names.

## Contributing

Feel free to contribute by adding new agents, improving existing ones, or enhancing the workflow.

## License

This project is created by https://rajan-sap.github.io/rajendra-portfolio/.
