"""
File Utilities for Multi-Agent Content Writer
Utility functions for file operations and content management
"""

import os
from datetime import datetime
from pathlib import Path


def create_output_directory():
    """Create the output directory if it doesn't exist"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def save_content(content, filename, user_input):
    """Save the generated content to a file"""
    output_dir = create_output_directory()
    file_path = output_dir / filename
    
    # Create a header with metadata
    header = f"""# {user_input['topic']}

**Content Type:** {user_input['content_type'].title()}  
**Target Audience:** {user_input['target_audience'].title()}  
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Approximate Word Count:** {user_input['word_count']}

---

"""
    
    # Combine header with content
    full_content = header + str(content)
    
    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    return str(file_path)


def get_word_count(text):
    """Get the word count of a text"""
    return len(text.split())


def clean_filename(filename):
    """Clean filename by removing invalid characters"""
    import re
    # Remove invalid characters for filenames
    cleaned = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove multiple underscores
    cleaned = re.sub(r'_+', '_', cleaned)
    return cleaned.strip('_')


def create_backup(file_path):
    """Create a backup of an existing file"""
    if os.path.exists(file_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{file_path}.backup_{timestamp}"
        os.rename(file_path, backup_path)
        return backup_path
    return None


def list_output_files():
    """List all files in the output directory"""
    output_dir = Path("output")
    if output_dir.exists():
        return list(output_dir.glob("*.md"))
    return []


def get_file_info(file_path):
    """Get information about a file"""
    file_path = Path(file_path)
    if file_path.exists():
        stat = file_path.stat()
        return {
            "name": file_path.name,
            "size": stat.st_size,
            "created": datetime.fromtimestamp(stat.st_ctime),
            "modified": datetime.fromtimestamp(stat.st_mtime),
            "word_count": get_word_count(file_path.read_text(encoding='utf-8'))
        }
    return None
