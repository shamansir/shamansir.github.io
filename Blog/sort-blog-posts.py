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
        return {}

    # Get all markdown files
    md_files = list(directory.glob('*.md'))

    if not md_files:
        print(f"No markdown files found in {directory_path}")
        return {}

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

    # Create mapping from clean names to new names (with prefixes)
    rename_map = {}

    # Assign prefixes and rename
    print(f"\nProcessing {len(file_info)} files in {directory_path}:")
    print("-" * 80)

    for index, info in enumerate(file_info):
        prefix = generate_prefix(index)
        new_name = f"{prefix}{info['clean_name']}"
        new_path = info['path'].parent / new_name

        # Store mapping for link updates (without .md extension)
        clean_name_no_ext = info['clean_name'].rsplit('.', 1)[0]
        new_name_no_ext = new_name.rsplit('.', 1)[0]
        original_name_no_ext = info['original_name'].rsplit('.', 1)[0]

        # Map both clean name and original name to new name
        rename_map[clean_name_no_ext] = new_name_no_ext
        rename_map[original_name_no_ext] = new_name_no_ext

        if info['path'] != new_path:
            print(f"{info['original_name']:50} -> {new_name}")
            info['path'].rename(new_path)
        else:
            print(f"{new_name:50} (no change)")

    print("-" * 80)
    print(f"Done! Processed {len(file_info)} files.\n")

    return rename_map

def update_links_in_file(file_path, rename_maps):
    """Update blog post links in a markdown or org-mode file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = False

        # Pattern for wiki-style links: [[Blog/blog-en/...]] or [[Blog/blog-ru/...]]
        # Matches both with and without prefixes
        for blog_dir in ['blog-en', 'blog-ru']:
            if blog_dir not in rename_maps or not rename_maps[blog_dir]:
                continue

            # Pattern to match: [[Blog/blog-XX/anything]]
            pattern = rf'\[\[Blog/{blog_dir}/([^\]]+)\]\]'

            def replace_link(match):
                nonlocal changes_made
                old_link = match.group(1)

                # Check if this link needs updating
                if old_link in rename_maps[blog_dir]:
                    new_link = rename_maps[blog_dir][old_link]
                    if new_link != old_link:
                        changes_made = True
                        return f'[[Blog/{blog_dir}/{new_link}]]'

                return match.group(0)

            content = re.sub(pattern, replace_link, content)

        # Write back if changes were made
        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def update_all_links(workspace_root, rename_maps):
    """Update links in all markdown and org-mode files in the workspace"""
    workspace = Path(workspace_root)

    if not workspace.exists():
        print(f"Error: Workspace {workspace_root} does not exist")
        return

    # Find all markdown and org files
    md_files = list(workspace.rglob('*.md'))
    org_files = list(workspace.rglob('*.org'))
    all_files = md_files + org_files

    # Exclude blog post files themselves
    all_files = [f for f in all_files
                 if 'blog-en' not in str(f) and 'blog-ru' not in str(f)]

    print(f"\nUpdating links in {len(all_files)} files:")
    print("-" * 80)

    updated_count = 0
    for file_path in all_files:
        if update_links_in_file(file_path, rename_maps):
            print(f"Updated: {file_path.relative_to(workspace)}")
            updated_count += 1

    print("-" * 80)
    print(f"Updated links in {updated_count} files.\n")

def main():
    import sys

    # Get workspace root (parent of Blog directory)
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent

    # Process directories
    directories = {
        'blog-en': workspace_root / 'Blog' / 'blog-en',
        'blog-ru': workspace_root / 'Blog' / 'blog-ru'
    }

    # Store rename mappings for each directory
    rename_maps = {}

    for blog_name, blog_path in directories.items():
        rename_maps[blog_name] = process_directory(blog_path)

    # Update all links in the workspace
    if any(rename_maps.values()):
        update_all_links(workspace_root, rename_maps)
    else:
        print("No files were renamed, skipping link updates.")

if __name__ == '__main__':
    main()