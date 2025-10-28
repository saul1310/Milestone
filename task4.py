#!/usr/bin/env python3
"""
Task 4: Print out all the tags that have an id attribute (using single API call).
Usage: python task4.py <input_file>
"""

import sys
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings

def print_tags_with_id(input_file):
    """Find and print all tags with an id attribute using a single API call."""
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser')
        
        # Single API call to find all tags with id attribute
        tags_with_id = soup.find_all(id=True)
        
        print(f"Found {len(tags_with_id)} tags with 'id' attribute in '{input_file}':\n")
        print("=" * 80)
        
        for i, tag in enumerate(tags_with_id, 1):
            tag_id = tag.get('id')
            text = tag.get_text(strip=True)[:60]
            
            print(f"\n{i}. Tag: <{tag.name}>")
            print(f"   ID: {tag_id}")
            print(f"   Content preview: {text}...")
            
            # Show other attributes if present
            other_attrs = {k: v for k, v in tag.attrs.items() if k != 'id'}
            if other_attrs:
                # Limit display of attributes
                attrs_str = ', '.join(f"{k}={v}" for k, v in list(other_attrs.items())[:3])
                print(f"   Other attributes: {attrs_str}")
        
        if not tags_with_id:
            print("\nNo tags with 'id' attribute found in the document.")
        
        print("\n" + "=" * 80)
        print(f"\nTotal tags with ID: {len(tags_with_id)}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    print_tags_with_id(input_file)