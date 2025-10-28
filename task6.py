#!/usr/bin/env python3
"""
Task 6: Change all the <b> tags to <blockquote> tags and write the tree to a file.
Usage: python task6.py <input_file>
"""

import sys
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings
import os

def change_b_to_blockquote(input_file):
    """Replace all <b> tags with <blockquote> tags and save to file."""
    try:
      
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser')
     
        b_tags = soup.find_all('b')
        
        print(f"Processing '{input_file}'...")
        print(f"Found {len(b_tags)} <b> tags to replace.\n")

        for b_tag in b_tags:
            b_tag.name = 'blockquote'

        base_name = os.path.splitext(input_file)[0]
        # Use .xml extension if input was XML, else .html
        output_file = f"{base_name}_b_to_blockquote{'.xml' if input_file.lower().endswith('.xml') else '.html'}"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"Successfully replaced {len(b_tags)} <b> tags with <blockquote> tags.")
        print(f"Output written to: {output_file}")
        
    
        # Verify the changes by reloading with same parsing approach
        with open(output_file, 'r', encoding='utf-8-sig') as f:
            new_content = f.read()
        new_content = new_content.lstrip()
        try:
            new_soup = BeautifulSoup(new_content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            new_soup = BeautifulSoup(new_content, 'html.parser')
        new_b_count = len(new_soup.find_all('b'))
        new_blockquote_count = len(new_soup.find_all('blockquote'))
        
        print(f"\nVerification:")
        print(f"  <b> tags in output: {new_b_count}")
        print(f"  <blockquote> tags in output: {new_blockquote_count}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task6.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    change_b_to_blockquote(input_file)