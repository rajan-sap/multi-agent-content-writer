"""
Editing Task for Multi-Agent Content Writer
Defines the editing task for the editor agent
"""

from crewai import Task


def create_editing_task(agent):
    """Create and configure the editing task"""
    
    editing_task = Task(
        description="""
        Perform final editing of the content to ensure it meets professional publication standards.
        
        Editing Focus Areas:
        1. Grammar and Syntax:
           - Check for grammatical errors
           - Ensure proper sentence structure
           - Verify correct punctuation usage
           - Fix any syntax issues
        
        2. Style and Consistency:
           - Ensure consistent tone throughout
           - Check for consistent formatting
           - Verify proper use of style conventions
           - Maintain voice consistency
        
        3. Clarity and Readability:
           - Improve sentence clarity where needed
           - Enhance word choice and vocabulary
           - Ensure smooth transitions between paragraphs
           - Optimize for readability
        
        4. Formatting and Structure:
           - Apply proper heading hierarchy
           - Ensure consistent formatting
           - Check bullet points and lists
           - Verify proper spacing and layout
        
        5. Final Polish:
           - Remove redundancies
           - Enhance flow and coherence
           - Ensure the content is publication-ready
           - Add any necessary formatting for presentation
        
        Incorporate feedback from the review phase and produce the final, polished version.
        """,
        
        expected_output="""
        The final, polished content that is ready for publication, including:
        - Perfect grammar, punctuation, and syntax
        - Consistent style and formatting
        - Optimized readability and flow
        - Professional presentation
        - All reviewer feedback incorporated
        - Publication-ready formatting
        - Final word count and content specifications met
        """,
        
        agent=agent
    )
    
    return editing_task
