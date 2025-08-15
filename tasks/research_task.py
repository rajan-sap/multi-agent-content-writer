"""
Research Task for Multi-Agent Content Writer
Defines the research task for the research agent
"""

from crewai import Task


def create_research_task(agent, user_input):
    """Create and configure the research task"""
    
    research_task = Task(
        description=f"""
        Conduct comprehensive research on the topic: '{user_input['topic']}'
        
        Research Requirements:
        - Content type: {user_input['content_type']}
        - Target audience: {user_input['target_audience']}
        - Approximate word count: {user_input['word_count']}
        
        Your research should include:
        1. Current and relevant information about the topic
        2. Key facts, statistics, and data points
        3. Different perspectives and viewpoints
        4. Recent developments and trends
        5. Credible sources and references
        6. Important subtopics and related concepts
        
        Organize your findings in a structured format that will help the writer create comprehensive content.
        Include source URLs and publication dates where available.
        
        Ensure all information is accurate, up-to-date, and appropriate for the {user_input['target_audience']} audience.
        """,
        
        expected_output="""
        A comprehensive research report containing:
        - Executive summary of key findings
        - Detailed information organized by subtopics
        - Key facts, statistics, and data points with sources
        - Recent developments and trends
        - List of credible sources with URLs and dates
        - Suggested content structure and key points to cover
        """,
        
        agent=agent
    )
    
    return research_task
