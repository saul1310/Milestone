#!/usr/bin/env python3
"""
Task 4 (Milestone 2): Print all tags with id attribute using SoupStrainer
Uses SoupStrainer to parse only tags that have an id attribute
"""

import sys
from bs4 import BeautifulSoup, SoupStrainer

def extract_tags_with_id(filename):
    """
    Extract and print all tags that have an id attribute.
    Uses SoupStrainer to parse only elements with id attributes for efficiency.
    """
    try:
        # Create a SoupStrainer that only parses tags with an 'id' attribute
        only_tags_with_id = SoupStrainer(id=True)
        
        # Parse the file with the strainer
        with open(filename, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser', parse_only=only_tags_with_id)
        
        # Find all tags with id attribute (should be all tags due to strainer)
        tags_with_id = soup.find_all(id=True)
        
        print(f"Found {len(tags_with_id)} tags with id attributes in {filename}:\n")
        
        for i, tag in enumerate(tags_with_id, 1):
            tag_name = tag.name
            tag_id = tag.get('id', '')
            # Get a preview of the tag content (first 50 chars)
            tag_text = tag.get_text(strip=True)[:50]
            if len(tag.get_text(strip=True)) > 50:
                tag_text += "..."
            
            print(f"{i}. <{tag_name}> id='{tag_id}'")
            if tag_text:
                print(f"   Preview: {tag_text}")
            print()
        
        if not tags_with_id:
            print("No tags with id attributes found in the document.")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <html_or_xml_file>")
        sys.exit(1)
    
    extract_tags_with_id(sys.argv[1])