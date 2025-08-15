"""
Writer Agent for Multi-Agent Content Writer
Responsible for creating engaging and well-structured content
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_writer_agent():
    """Create and configure the writer agent"""
    
    writer_agent = Agent(
        role="Content Writer",
        goal="Create engaging, well-structured, and informative content based on research findings",
        backstory="""You are a professional content writer with expertise in various content formats including 
        articles, blog posts, reports, and essays. You have a talent for translating complex research into 
        accessible, engaging content that resonates with the target audience. You understand the importance 
        of structure, flow, and maintaining reader engagement throughout the piece. You excel at crafting 
        compelling headlines, introductions, and conclusions.""",
        
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(model="gpt-4", temperature=0.7)
    )
    
    return writer_agent
