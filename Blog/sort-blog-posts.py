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

def update_links_in_file(file_path, rename_maps, is_blog_post=False):
    """Update blog post links in a markdown or org-mode file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes_made = False

        # Pattern 1: Wiki-style links with Blog/ prefix
        # [[Blog/blog-en/...]] or [[Blog/blog-ru/...]]
        for blog_dir in ['blog-en', 'blog-ru']:
            if blog_dir not in rename_maps or not rename_maps[blog_dir]:
                continue

            pattern = rf'\[\[Blog/{blog_dir}/([^\]]+)\]\]'

            def replace_link(match):
                nonlocal changes_made
                old_link = match.group(1)

                if old_link in rename_maps[blog_dir]:
                    new_link = rename_maps[blog_dir][old_link]
                    if new_link != old_link:
                        changes_made = True
                        return f'[[Blog/{blog_dir}/{new_link}]]'

                return match.group(0)

            content = re.sub(pattern, replace_link, content)

        # Pattern 2: Root-folder style links
        # /Blog/blog-en/...md or [text](/Blog/blog-en/...md)
        for blog_dir in ['blog-en', 'blog-ru']:
            if blog_dir not in rename_maps or not rename_maps[blog_dir]:
                continue

            # Match both bare links and markdown links
            pattern = rf'(\[([^\]]*)\])?\(/Blog/{blog_dir}/([^)]+\.md)\)'

            def replace_root_link(match):
                nonlocal changes_made
                link_text = match.group(2) if match.group(1) else None
                old_filename = match.group(3)
                old_link = old_filename.rsplit('.', 1)[0]  # Remove .md

                if old_link in rename_maps[blog_dir]:
                    new_link = rename_maps[blog_dir][old_link]
                    if new_link != old_link:
                        changes_made = True
                        new_filename = f"{new_link}.md"
                        if link_text is not None:
                            return f'[{link_text}](/Blog/{blog_dir}/{new_filename})'
                        else:
                            return f'(/Blog/{blog_dir}/{new_filename})'

                return match.group(0)

            content = re.sub(pattern, replace_root_link, content)

        # Pattern 3: Footnote-style reference links with ../blog-XX/ prefix
        # [1]: ../blog-ru/2012-02-22-title.md
        for blog_dir in ['blog-en', 'blog-ru']:
            if blog_dir not in rename_maps or not rename_maps[blog_dir]:
                continue

            pattern = rf'(\[[^\]]+\]:\s+)\.\./{blog_dir}/([^\s]+\.md)'

            def replace_footnote_link(match):
                nonlocal changes_made
                link_prefix = match.group(1)
                old_filename = match.group(2)
                old_link = old_filename.rsplit('.', 1)[0]  # Remove .md

                if old_link in rename_maps[blog_dir]:
                    new_link = rename_maps[blog_dir][old_link]
                    if new_link != old_link:
                        changes_made = True
                        new_filename = f"{new_link}.md"
                        return f'{link_prefix}../{blog_dir}/{new_filename}'

                return match.group(0)

            content = re.sub(pattern, replace_footnote_link, content)

        # If this is a blog post file, also handle relative links
        if is_blog_post:
            # Determine which blog directory this file is in
            file_blog_dir = None
            for blog_dir in ['blog-en', 'blog-ru']:
                if blog_dir in str(file_path):
                    file_blog_dir = blog_dir
                    break

            if file_blog_dir and file_blog_dir in rename_maps:
                # Pattern 4: Relative wiki-style links (without Blog/ or / prefix)
                # [[2007-08-12-title]] or [[aa-2007-08-12-title]]
                pattern = r'\[\[(?!Blog/)(?!/)([^\]]+)\]\]'

                def replace_relative_link(match):
                    nonlocal changes_made
                    old_link = match.group(1)

                    if old_link in rename_maps[file_blog_dir]:
                        new_link = rename_maps[file_blog_dir][old_link]
                        if new_link != old_link:
                            changes_made = True
                            return f'[[{new_link}]]'

                    return match.group(0)

                content = re.sub(pattern, replace_relative_link, content)

                # Pattern 5: Relative markdown links with ./
                # [text](./2007-08-12-title.md) or [text](./aa-2007-08-12-title.md)
                pattern = r'\[([^\]]+)\]\(\./([^)]+\.md)\)'

                def replace_relative_md_link(match):
                    nonlocal changes_made
                    link_text = match.group(1)
                    old_filename = match.group(2)
                    old_link = old_filename.rsplit('.', 1)[0]  # Remove .md

                    if old_link in rename_maps[file_blog_dir]:
                        new_link = rename_maps[file_blog_dir][old_link]
                        if new_link != old_link:
                            changes_made = True
                            new_filename = f"{new_link}.md"
                            return f'[{link_text}](./{new_filename})'

                    return match.group(0)

                content = re.sub(pattern, replace_relative_md_link, content)

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

    print(f"\nUpdating links in files:")
    print("-" * 80)

    updated_count = 0

    # Separate blog post files from other files
    blog_post_files = []
    other_files = []

    for f in all_files:
        if 'blog-en' in str(f) or 'blog-ru' in str(f):
            blog_post_files.append(f)
        else:
            other_files.append(f)

    # Update blog post files (with relative link handling)
    for file_path in blog_post_files:
        if update_links_in_file(file_path, rename_maps, is_blog_post=True):
            print(f"Updated: {file_path.relative_to(workspace)}")
            updated_count += 1

    # Update other files (only absolute links)
    for file_path in other_files:
        if update_links_in_file(file_path, rename_maps, is_blog_post=False):
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