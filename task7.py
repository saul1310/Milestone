#!/usr/bin/env python3
"""
Task 7: Find all <p> tags and add (or replace) a class attribute class="test",
then write the tree to a file.
Usage: python task7.py <input_file>
"""

import sys
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings
import os


def add_class_to_paragraphs(input_file):
    """Add class='test' to all <p> tags and save to file."""
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser')
        
        # Find all <p> tags
        p_tags = soup.find_all('p')
        
        print(f"Processing '{input_file}'...")
        print(f"Found {len(p_tags)} <p> tags.\n")
        
        replaced_count = 0
        added_count = 0
        
        # Add or replace class attribute for each <p> tag
        for p_tag in p_tags:
            if p_tag.has_attr('class'):
                old_class = p_tag['class']
                print(f"Replacing class {old_class} with 'test' in: {p_tag.get_text(strip=True)[:50]}...")
                replaced_count += 1
            else:
                print(f"Adding class='test' to: {p_tag.get_text(strip=True)[:50]}...")
                added_count += 1
            
            # Set class to 'test' (replaces existing or adds new)
            p_tag['class'] = 'test'
        
        # Generate output filename
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_p_with_class.html"
        
        # Write modified content to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        # Write modified content to file (preserve .xml extension for XML inputs)
        
        print(f"\nSuccessfully modified {len(p_tags)} <p> tags:")
        print(f"  - Added class='test' to {added_count} tags")
        print(f"  - Replaced existing class in {replaced_count} tags")
        print(f"Output written to: {output_file}")
        
        # Verify via same parsing approach
        with open(output_file, 'r', encoding='utf-8-sig') as f:
            new_content = f.read()
        new_content = new_content.lstrip()
        try:
            new_soup = BeautifulSoup(new_content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            new_soup = BeautifulSoup(new_content, 'html.parser')
        p_with_test_class = new_soup.find_all('p', class_='test')
        
        print(f"\nVerification:")
        print(f"  <p> tags with class='test': {len(p_with_test_class)}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task7.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    add_class_to_paragraphs(input_file)