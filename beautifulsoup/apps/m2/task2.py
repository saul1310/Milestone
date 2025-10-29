#!/usr/bin/env python3
"""
Task 2 (Milestone 2): Print all hyperlinks using SoupStrainer
Uses SoupStrainer to parse only <a> tags for better performance
"""

import sys
from bs4 import BeautifulSoup, SoupStrainer

def extract_hyperlinks(filename):
    """
    Extract and print all hyperlinks from an HTML/XML file.
    Uses SoupStrainer to parse only <a> tags.
    """
    try:
        # Create a SoupStrainer that only parses <a> tags
        only_a_tags = SoupStrainer("a")
        
        # Parse the file with the strainer
        with open(filename, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser', parse_only=only_a_tags)
        
        # Find all <a> tags (should be all tags in the soup due to strainer)
        links = soup.find_all('a')
        
        print(f"Found {len(links)} hyperlinks in {filename}:\n")
        
        for i, link in enumerate(links, 1):
            href = link.get('href', 'No href attribute')
            text = link.get_text(strip=True) or 'No text'
            print(f"{i}. Text: '{text}' -> URL: {href}")
        
        if not links:
            print("No hyperlinks found in the document.")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task2.py <html_or_xml_file>")
        sys.exit(1)
    
    extract_hyperlinks(sys.argv[1])