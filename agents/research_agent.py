"""
Research Agent for Multi-Agent Content Writer
Responsible for gathering comprehensive information about the topic
"""

from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI


def create_research_agent():
    """Create and configure the research agent"""
    
    # Initialize tools
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    
    # Create the research agent
    research_agent = Agent(
        role="Content Researcher",
        goal="Conduct comprehensive research on the given topic to provide accurate, up-to-date, and relevant information",
        backstory="""You are an expert researcher with years of experience in gathering information from various sources. 
        You have access to search engines and can scrape websites to find the most current and reliable information. 
        You excel at identifying credible sources, fact-checking information, and organizing research findings 
        in a structured manner that writers can easily use.""",
        
        tools=[search_tool, scrape_tool],
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(model="gpt-4", temperature=0.1)
    )
    
    return research_agent
