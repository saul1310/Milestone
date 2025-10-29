#!/usr/bin/env python3
"""
Task 5: Use find_parent() meaningfully given your test file.
This script finds all <a> tags and shows their parent elements using find_parent().
Usage: python task5.py <input_file>
"""

import sys
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings


def use_find_parent(input_file):
    """Demonstrate find_parent() by finding parents of hyperlinks and other elements."""
    try:
  
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        try:
            soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser')
        
        print(f"Demonstrating find_parent() with '{input_file}':\n")
        print("=" * 80)
        
    
        print("\n1. Finding parent elements of hyperlinks (<a> tags):\n")
        links = soup.find_all('a')
        
        for i, link in enumerate(links, 1):
            href = link.get('href', 'No href')
            parent = link.find_parent()
            
            print(f"   Link {i}: {link.get_text(strip=True)[:40]}")
            print(f"   URL: {href}")
            if parent:
                print(f"   Parent tag: <{parent.name}>")
                parent_id = parent.get('id', 'no id')
                parent_class = parent.get('class', 'no class')
                print(f"   Parent attributes: id='{parent_id}', class='{parent_class}'")
            print()
        
     
        print("\n" + "=" * 80)
        print("\n2. Finding specific parent types (e.g., <div> parents of <p> tags):\n")
        paragraphs = soup.find_all('p')
        
        for i, p in enumerate(paragraphs, 1):
      
            div_parent = p.find_parent('div')
            
            print(f"   Paragraph {i}: {p.get_text(strip=True)[:50]}...")
            if div_parent:
                div_id = div_parent.get('id', 'no id')
                div_class = div_parent.get('class', 'no class')
                print(f"   Found <div> parent: id='{div_id}', class='{div_class}'")
            else:
                print(f"   No <div> parent found")
            print()
        
      
        print("\n" + "=" * 80)
        print("\n3. Finding parents with specific attributes:\n")
        all_tags = soup.find_all(True)[:50]  # Limit to first 50 for readability
        
        for tag in all_tags:
           
            parent_with_id = tag.find_parent(id=True)
            
            if parent_with_id:
                print(f"   Tag <{tag.name}> has parent <{parent_with_id.name}> with id='{parent_with_id.get('id')}'")
        
        print("\n" + "=" * 80)
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task5.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    use_find_parent(input_file)