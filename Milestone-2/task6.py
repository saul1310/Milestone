#!/usr/bin/env python3
"""
Second test case for SoupReplacer API
This demonstrates replacing <i> (italic) tags with <em> (emphasis) tags during parsing.

Usage: python test_replacer_demo.py <input_file>
"""

import sys
import os
from bs4 import BeautifulSoup, SoupReplacer, XMLParsedAsHTMLWarning
import warnings

def replace_i_with_em(input_file):
    """
    Replace all <i> tags with <em> tags using SoupReplacer.
    Demonstrates the SoupReplacer API with a different tag pair.
    """
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.lstrip()
        
        print(f"Test Case 2: SoupReplacer Demo")
        print(f"=" * 50)
        print(f"Input file: '{input_file}'")
        print(f"Operation: Replace <i> tags with <em> tags during parsing\n")
        
        # First, parse w/o replacer to see original counts
        print("Step 1: Parsing without replacer (baseline)...")
        try:
            baseline_soup = BeautifulSoup(content, 'xml')
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            baseline_soup = BeautifulSoup(content, 'html.parser')
        
        original_i_count = len(baseline_soup.find_all('i'))
        original_em_count = len(baseline_soup.find_all('em'))
        
        print(f"  Original <i> tags: {original_i_count}")
        print(f"  Original <em> tags: {original_em_count}")
        
        # parse w replacer
        print("\nStep 2: Parsing WITH SoupReplacer...")
        i_to_em = SoupReplacer("i", "em")
        
        try:
            soup = BeautifulSoup(content, 'xml', replacer=i_to_em)
        except Exception:
            warnings.filterwarnings('ignore', category=XMLParsedAsHTMLWarning)
            soup = BeautifulSoup(content, 'html.parser', replacer=i_to_em)
        
        new_i_count = len(soup.find_all('i'))
        new_em_count = len(soup.find_all('em'))
        
        print(f"  After replacement <i> tags: {new_i_count}")
        print(f"  After replacement <em> tags: {new_em_count}")
        
        # Verify the replacement worked
        expected_em_count = original_i_count + original_em_count
        if new_i_count == 0 and new_em_count == expected_em_count:
            print("\n✓ SUCCESS: All <i> tags were replaced with <em> during parsing!")
        else:
            print("\n✗ WARNING: Unexpected counts after replacement")
        
        # Determine output filename
        base_name = os.path.splitext(input_file)[0]
        ext = '.xml' if input_file.lower().endswith('.xml') else '.html'
        output_file = f"{base_name}_i_to_em{ext}"
        
        # Write the modified tree to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"\nOutput written to: {output_file}")
        
        # Show a sample of the changes
        print("\nSample output (first 500 characters):")
        print("-" * 50)
        print(str(soup)[:500])
        if len(str(soup)) > 500:
            print("...")
        print("-" * 50)
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except AttributeError as e:
        print(f"Error: SoupReplacer not found. Make sure you've implemented it in BeautifulSoup source code.")
        print(f"Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_replacer_demo.py <input_file>")
        print("\nThis is test case 2 for SoupReplacer API.")
        print("It replaces <i> tags with <em> tags during parsing.")
        print("\nMake sure you've implemented SoupReplacer in the BeautifulSoup source code.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    replace_i_with_em(input_file)