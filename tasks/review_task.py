"""
Review Task for Multi-Agent Content Writer
Defines the review task for the reviewer agent
"""

from crewai import Task


def create_review_task(agent):
    """Create and configure the review task"""
    
    review_task = Task(
        description="""
        Review the written content for accuracy, coherence, quality, and overall effectiveness.
        
        Review Criteria:
        1. Content Accuracy:
           - Verify facts and data points
           - Check for any misleading information
           - Ensure claims are properly supported
        
        2. Structure and Organization:
           - Assess logical flow and progression
           - Review section organization and transitions
           - Check if the content meets the intended structure
        
        3. Audience Appropriateness:
           - Evaluate if the content suits the target audience
           - Check language complexity and terminology
           - Assess if the tone is appropriate
        
        4. Completeness:
           - Ensure all key points are covered
           - Check if the content meets the specified word count
           - Verify that the content fulfills the original requirements
        
        5. Engagement and Readability:
           - Assess how engaging the content is
           - Check for variety in sentence structure
           - Evaluate overall readability
        
        Provide specific feedback on areas that need improvement and suggest enhancements.
        If the content is satisfactory, indicate what works well.
        """,
        
        expected_output="""
        A comprehensive review report that includes:
        - Overall assessment of content quality
        - Specific feedback on accuracy, structure, and audience appropriateness
        - Identification of strengths and areas for improvement
        - Specific suggestions for enhancements
        - Recommendations for the editing phase
        - Final approval status or list of required changes
        """,
        
        agent=agent
    )
    
    return review_task
