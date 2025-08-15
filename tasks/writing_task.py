"""
Writing Task for Multi-Agent Content Writer
Defines the writing task for the writer agent
"""

from crewai import Task


def create_writing_task(agent, user_input):
    """Create and configure the writing task"""
    
    writing_task = Task(
        description=f"""
        Based on the research findings, write a comprehensive {user_input['content_type']} on the topic: '{user_input['topic']}'
        
        Writing Requirements:
        - Content type: {user_input['content_type']}
        - Target audience: {user_input['target_audience']}
        - Approximate word count: {user_input['word_count']} words
        
        Content Structure Guidelines:
        1. Compelling headline/title
        2. Engaging introduction that hooks the reader
        3. Well-organized main body with clear sections
        4. Use of subheadings for better readability
        5. Integration of research findings and data
        6. Practical examples or case studies where relevant
        7. Strong conclusion that summarizes key points
        
        Writing Style Guidelines:
        - Write for {user_input['target_audience']} audience
        - Use clear, concise language
        - Maintain consistent tone throughout
        - Include relevant keywords naturally
        - Use active voice when possible
        - Ensure logical flow between paragraphs
        
        Use the research findings to create accurate, informative, and engaging content.
        Include citations or references where appropriate.
        """,
        
        expected_output=f"""
        A well-written {user_input['content_type']} of approximately {user_input['word_count']} words that includes:
        - Compelling title
        - Engaging introduction
        - Well-structured main content with subheadings
        - Integration of research findings and data
        - Practical examples or insights
        - Strong conclusion
        - Proper citations and references
        - Content optimized for {user_input['target_audience']} audience
        """,
        
        agent=agent
    )
    
    return writing_task
