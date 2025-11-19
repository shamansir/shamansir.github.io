#!/usr/bin/env python3
# filepath: Blog/sort-blog-posts.py

import os
import re
from pathlib import Path
from datetime import datetime

def generate_prefix(index):
    """Generate prefix: aa, ab, ac, ..., az, ba, bb, ..., zz"""
    first = chr(ord('a') + index // 26)
    second = chr(ord('a') + index % 26)
    return f"{first}{second}-"

def extract_date_from_filename(filename):
    """Extract date from filename format: YYYY-MM-DD-title.md"""
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    if match:
        try:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
        except ValueError:
            return None
    return None

def remove_existing_prefix(filename):
    """Remove existing aa-, ab-, etc. prefix if present"""
    match = re.match(r'^[a-z]{2}-(.+)$', filename)
    if match:
        return match.group(1)
    return filename

def process_directory(directory_path):
    """Process all markdown files in directory and add prefixes"""
    directory = Path(directory_path)

    if not directory.exists():
        print(f"Error: Directory {directory_path} does not exist")
        return

    # Get all markdown files
    md_files = list(directory.glob('*.md'))

    if not md_files:
        print(f"No markdown files found in {directory_path}")
        return

    # Parse files and extract dates
    file_info = []
    for file_path in md_files:
        original_name = file_path.name
        clean_name = remove_existing_prefix(original_name)
        date = extract_date_from_filename(clean_name)

        if date:
            file_info.append({
                'path': file_path,
                'original_name': original_name,
                'clean_name': clean_name,
                'date': date
            })
        else:
            print(f"Warning: Could not parse date from {original_name}")

    # Sort by date (newest first)
    file_info.sort(key=lambda x: x['date'], reverse=True)

    # Assign prefixes and rename
    print(f"\nProcessing {len(file_info)} files in {directory_path}:")
    print("-" * 80)

    for index, info in enumerate(file_info):
        prefix = generate_prefix(index)
        new_name = f"{prefix}{info['clean_name']}"
        new_path = info['path'].parent / new_name

        if info['path'] != new_path:
            print(f"{info['original_name']:50} -> {new_name}")
            info['path'].rename(new_path)
        else:
            print(f"{new_name:50} (no change)")

    print("-" * 80)
    print(f"Done! Processed {len(file_info)} files.\n")

def main():
    import sys

    if len(sys.argv) > 1:
        directories = sys.argv[1:]
    else:
        # Default directories
        directories = [
            'Blog/blog-ru',
            'Blog/blog-en'
        ]

    for directory in directories:
        process_directory(directory)

if __name__ == '__main__':
    main()