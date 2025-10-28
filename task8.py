#!/usr/bin/env python3
"""
Task 8: Exercise at least one more function of the API not covered in previous tasks.
This script demonstrates select() with CSS selectors.
Usage: python task8.py <input_file>
"""

import sys
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings

def demonstrate_css_selectors(input_file):
    """Demonstrate CSS selectors with select()."""
    try:

        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser')
        

        print(f"Demonstrating select() with CSS selectors on '{input_file}':\n")
        print("=" * 80)
        
  
        print("\n1. Selecting elements with a specific class:")
        class_elements = soup.select('.mw-body')
        print(f"   Found {len(class_elements)} elements with class 'mw-body'")
        for i, elem in enumerate(class_elements[:3], 1):
            print(f"   {i}. <{elem.name}> - {elem.get_text(strip=True)[:50]}...")
        

        print("\n2. Selecting nested elements (div p):")
        nested = soup.select('div p')
        print(f"   Found {len(nested)} <p> tags inside <div> tags")
        for i, elem in enumerate(nested[:3], 1):
            print(f"   {i}. {elem.get_text(strip=True)[:60]}...")
        

        print("\n3. Selecting links with href starting with 'http':")
        http_links = soup.select('a[href^="http"]')
        print(f"   Found {len(http_links)} links starting with 'http'")
        for i, link in enumerate(http_links[:5], 1):
            print(f"   {i}. {link.get_text(strip=True)[:40]} - {link.get('href')}")
        
    
        print("\n4. Selecting element by ID:")
        id_element = soup.select('#mw-content-text')
        if id_element:
            print(f"   Found element with id 'mw-content-text': <{id_element[0].name}>")
        else:
            print("   No element found with id 'mw-content-text'")
        
    
        print("\n5. Selecting divs with class attribute:")
        divs_with_class = soup.select('div[class]')
        print(f"   Found {len(divs_with_class)} <div> tags with class attribute")
        for i, div in enumerate(divs_with_class[:3], 1):
            classes = div.get('class', [])
            print(f"   {i}. <div> with classes: {classes}")
        
        print("\n" + "=" * 80)
        print(f"\nTotal elements found using CSS selectors: {len(class_elements) + len(nested) + len(http_links) + len(id_element) + len(divs_with_class)}")
        print("\nCSS selectors demonstrated successfully!")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task8.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    demonstrate_css_selectors(input_file)