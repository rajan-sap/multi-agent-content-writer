"""
Editor Agent for Multi-Agent Content Writer
Responsible for final editing, grammar, style, and formatting
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_editor_agent():
    """Create and configure the editor agent"""
    
    editor_agent = Agent(
        role="Content Editor",
        goal="Perform final editing to ensure perfect grammar, style, formatting, and overall polish of the content",
        backstory="""You are a meticulous content editor with an exceptional eye for detail. You specialize in 
        grammar, punctuation, style consistency, and formatting. You understand various style guides and can 
        adapt your editing approach based on the content type and target audience. You ensure that the final 
        content is polished, professional, and ready for publication. You also optimize readability and flow 
        while preserving the author's voice and the content's core message.""",
        
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(model="gpt-4", temperature=0.1)
    )
    
    return editor_agent
