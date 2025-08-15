#!/usr/bin/env python3
"""
Multi-Agent Content Writer
A CrewAI-based application for autonomous content generation
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crewai import Crew
from agents.research_agent import create_research_agent
from agents.writer_agent import create_writer_agent
from agents.reviewer_agent import create_reviewer_agent
from agents.editor_agent import create_editor_agent
from tasks.research_task import create_research_task
from tasks.writing_task import create_writing_task
from tasks.review_task import create_review_task
from tasks.editing_task import create_editing_task
from utils.file_utils import save_content, create_output_directory


def get_user_input():
    """Get user input for content generation parameters"""
    print("🤖 Welcome to Multi-Agent Content Writer!")
    print("=" * 50)
    
    topic = input("\n📝 Enter the topic for content generation: ").strip()
    if not topic:
        print("❌ Topic cannot be empty!")
        return None
    
    content_type = input("📄 Enter content type (article/blog/report/essay) [article]: ").strip() or "article"
    target_audience = input("🎯 Enter target audience (general/technical/academic/business) [general]: ").strip() or "general"
    
    try:
        word_count = input("📊 Enter approximate word count [1000]: ").strip()
        word_count = int(word_count) if word_count else 1000
    except ValueError:
        word_count = 1000
    
    return {
        "topic": topic,
        "content_type": content_type,
        "target_audience": target_audience,
        "word_count": word_count
    }


def main():
    """Main application function"""
    # Load environment variables
    load_dotenv()
    
    # Check for required API keys
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables!")
        print("Please copy .env.example to .env and add your API keys.")
        return
    
    # Get user input
    user_input = get_user_input()
    if not user_input:
        return
    
    print(f"\n🚀 Starting content generation for: '{user_input['topic']}'")
    print("⏳ This may take a few minutes...")
    
    try:
        # Create agents
        print("\n👥 Creating agents...")
        research_agent = create_research_agent()
        writer_agent = create_writer_agent()
        reviewer_agent = create_reviewer_agent()
        editor_agent = create_editor_agent()
        
        # Create tasks
        print("📋 Creating tasks...")
        research_task = create_research_task(research_agent, user_input)
        writing_task = create_writing_task(writer_agent, user_input)
        review_task = create_review_task(reviewer_agent)
        editing_task = create_editing_task(editor_agent)
        
        # Set task dependencies
        writing_task.context = [research_task]
        review_task.context = [writing_task]
        editing_task.context = [review_task]
        
        # Create and run crew
        print("🎭 Assembling crew...")
        crew = Crew(
            agents=[research_agent, writer_agent, reviewer_agent, editor_agent],
            tasks=[research_task, writing_task, review_task, editing_task],
            verbose=True
        )
        
        print("🏃‍♂️ Running content generation workflow...")
        result = crew.kickoff()
        
        # Save the result
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{user_input['topic'].replace(' ', '_')}_{timestamp}.md"
        
        create_output_directory()
        file_path = save_content(result, filename, user_input)
        
        print(f"\n✅ Content generation completed!")
        print(f"📁 Output saved to: {file_path}")
        print(f"📊 Content type: {user_input['content_type']}")
        print(f"🎯 Target audience: {user_input['target_audience']}")
        print(f"📝 Approximate word count: {user_input['word_count']}")
        
    except Exception as e:
        print(f"\n❌ Error during content generation: {str(e)}")
        print("Please check your API keys and internet connection.")


if __name__ == "__main__":
    main()
