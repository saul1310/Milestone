"""
Task 1: Read an HTML/XML file into a tree and write it back as a prettified file.
Usage: python task1.py <input_file>
"""

import sys
from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
from xml.dom.minidom import parseString
import warnings
import os

def prettify_file(input_file):
    """Read HTML/XML file and write prettified version."""
    try:
        # Read the input file (use utf-8-sig to strip BOM if present)
        with open(input_file, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        # Remove leading whitespace/newlines which can break XML parsers
        content = content.lstrip()
        
        # Parse and prettify depending on file type
        base_name = os.path.splitext(input_file)[0]
        if input_file.endswith('.xml'):
            # Use stdlib minidom to pretty-print XML so we don't require lxml
            try:
                # parseString expects a text string (not bytes) in Python
                dom = parseString(content)
                pretty = dom.toprettyxml(indent="   ")
            except Exception:
                # Fallback to BeautifulSoup if minidom fails for some reason
                # Suppress the XML-parsed-as-HTML warning for the fallback parser
                warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
                soup = BeautifulSoup(content, 'html.parser')
                pretty = soup.prettify()

            output_file = f"{base_name}_prettified.xml"
        else:
            soup = BeautifulSoup(content, 'html.parser')
            pretty = soup.prettify()
            output_file = f"{base_name}_prettified.html"

        # Write prettified content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(pretty)
        
        print(f"Successfully prettified '{input_file}'")
        print(f"Output written to: {output_file}")
        print(f"Original size: {len(content)} bytes")
        print(f"Prettified size: {len(pretty)} bytes")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task1.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    prettify_file(input_file)