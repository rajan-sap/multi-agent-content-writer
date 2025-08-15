"""
Reviewer Agent for Multi-Agent Content Writer
Responsible for reviewing content for accuracy, coherence, and quality
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_reviewer_agent():
    """Create and configure the reviewer agent"""
    
    reviewer_agent = Agent(
        role="Content Reviewer",
        goal="Review content for accuracy, coherence, quality, and alignment with the intended purpose and audience",
        backstory="""You are a senior content reviewer with years of experience in evaluating written content. 
        You have a keen eye for detail and can quickly identify issues with accuracy, logical flow, coherence, 
        and audience appropriateness. You understand different content formats and can assess whether the content 
        meets its intended objectives. You provide constructive feedback and suggestions for improvement while 
        maintaining the author's voice and intent.""",
        
        verbose=True,
        allow_delegation=False,
        llm=ChatOpenAI(model="gpt-4", temperature=0.2)
    )
    
    return reviewer_agent
