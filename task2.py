#!/usr/bin/env python3
"""
Task 2: Print out all the hyperlinks (<a> tags).
Usage: python task2.py <input_file>
"""

import sys
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings

def print_hyperlinks(input_file):
    """Find and print all hyperlinks in the HTML/XML file."""
    try:
        # Read file safely (strip BOM and leading whitespace) and parse
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser')
        
        # Find all <a> tags
        links = soup.find_all('a')
        
        print(f"Found {len(links)} hyperlinks in '{input_file}':\n")
        print("-" * 80)
        
        for i, link in enumerate(links, 1):
            href = link.get('href', 'No href attribute')
            text = link.get_text(strip=True) or 'No text'
            print(f"{i}. Text: {text}")
            print(f"   URL: {href}")
            
            # Show other attributes if present
            other_attrs = {k: v for k, v in link.attrs.items() if k != 'href'}
            if other_attrs:
                print(f"   Other attributes: {other_attrs}")
            print()
        
        if not links:
            print("No hyperlinks found in the document.")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task2.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    print_hyperlinks(input_file)