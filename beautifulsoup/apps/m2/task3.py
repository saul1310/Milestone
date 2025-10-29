#!/usr/bin/env python3
"""
Task 3 (Milestone 2): Print all tags using SoupStrainer
NOTE: This task is challenging with SoupStrainer because we need ALL tags.
SoupStrainer is designed to filter/restrict parsing, not to get everything.

For this task, we have two approaches:
1. Don't use SoupStrainer at all (parse everything normally)
2. Use SoupStrainer with a function that accepts all tags (minimal optimization)

This implementation uses approach #2 to demonstrate SoupStrainer usage,
though the optimization benefit is minimal for this specific task.
"""

import sys
from bs4 import BeautifulSoup, SoupStrainer

def extract_all_tags(filename):
    """
    Extract and print all unique tag names from an HTML/XML file.
    Uses SoupStrainer with a permissive filter (demonstrates API usage).
    """
    try:
        # SoupStrainer that accepts all tags (minimal filtering)
        # This demonstrates the API but provides little optimization
        all_tags_strainer = SoupStrainer(True)  # True accepts everything
        
        with open(filename, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser', parse_only=all_tags_strainer)
        
        # Collect all tags
        all_tags = soup.find_all(True)  # True finds all tags
        
        # Get unique tag names
        unique_tags = set(tag.name for tag in all_tags if tag.name)
        
        print(f"Found {len(all_tags)} total tags with {len(unique_tags)} unique tag types in {filename}:\n")
        
        print("Unique tag names (sorted):")
        for tag_name in sorted(unique_tags):
            count = sum(1 for tag in all_tags if tag.name == tag_name)
            print(f"  <{tag_name}>: {count} occurrence(s)")
        
        if not all_tags:
            print("No tags found in the document.")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task3.py <html_or_xml_file>")
        sys.exit(1)
    
    extract_all_tags(sys.argv[1])