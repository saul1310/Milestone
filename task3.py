#!/usr/bin/env python3
"""
Task 3: Print out all the tags in the document.
Usage: python task3.py <input_file>
"""

import sys
from collections import Counter
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings

def print_all_tags(input_file):
    """Find and print all tags in the HTML/XML file."""
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser')
        
        # Find all tags (excluding NavigableString and other non-tag elements)
        all_tags = soup.find_all(True)
        
        print(f"Found {len(all_tags)} total tags in '{input_file}':\n")
        
        # Count occurrences of each tag
        tag_counts = Counter(tag.name for tag in all_tags)
        
        print("Tag Statistics:")
        print("-" * 80)
        for tag_name, count in sorted(tag_counts.items()):
            print(f"{tag_name:20s}: {count:5d} occurrence(s)")
        
        print("\n" + "=" * 80)
        print(f"\nUnique tags: {len(tag_counts)}")
        print(f"Total tags: {len(all_tags)}")
        
        # Print all tags with their content
        print("\n" + "=" * 80)
        print("\nAll tags in document (showing tag names and sample content):\n")
        for i, tag in enumerate(all_tags, 1):
            text = tag.get_text(strip=True)[:50]
            attrs = ', '.join(f"{k}={v}" for k, v in list(tag.attrs.items())[:2])
            if attrs:
                print(f"{i:3d}. <{tag.name}> [{attrs}] - {text}...")
            else:
                print(f"{i:3d}. <{tag.name}> - {text}...")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task3.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    print_all_tags(input_file)