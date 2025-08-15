"""
Search Tools for Multi-Agent Content Writer
Custom tools for web searching and information gathering
"""

import requests
from bs4 import BeautifulSoup
from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class SearchInput(BaseModel):
    """Input schema for SearchTool."""
    query: str = Field(..., description="Search query to find information")


class SearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = "Useful for searching information on the internet about any topic"
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        """Execute the search query."""
        try:
            # This is a simple example using DuckDuckGo's API
            # In production, you might want to use more sophisticated search APIs
            url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                results = []
                
                # Extract search results
                if 'RelatedTopics' in data:
                    for topic in data['RelatedTopics'][:5]:  # Limit to 5 results
                        if 'Text' in topic and 'FirstURL' in topic:
                            results.append(f"- {topic['Text']}\n  Source: {topic['FirstURL']}")
                
                return "\n\n".join(results) if results else "No relevant results found."
            else:
                return "Search request failed."
                
        except Exception as e:
            return f"Error performing search: {str(e)}"


class WebScrapeTool(BaseTool):
    name: str = "Web Scrape Tool"
    description: str = "Useful for extracting content from web pages"
    
    def _run(self, url: str) -> str:
        """Scrape content from a webpage."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Get text content
                text = soup.get_text()
                
                # Clean up the text
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = ' '.join(chunk for chunk in chunks if chunk)
                
                # Limit text length to avoid overwhelming the model
                return text[:3000] + "..." if len(text) > 3000 else text
            else:
                return f"Failed to access webpage. Status code: {response.status_code}"
                
        except Exception as e:
            return f"Error scraping webpage: {str(e)}"
