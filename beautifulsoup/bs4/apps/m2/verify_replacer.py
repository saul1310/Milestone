#!/usr/bin/env python3
"""
Verification script to test if SoupReplacer is working correctly.
This tests your modifications to the BeautifulSoup source code.

Location: beautifulsoup/bs4/apps/m2/verify_replacer.py
Run from: beautifulsoup/ directory
Command: python bs4/apps/m2/verify_replacer.py
"""

import sys
import os

# Add repository root to path to import local modified bs4
current_dir = os.path.dirname(os.path.abspath(__file__))
bs4_dir = os.path.abspath(os.path.join(current_dir, '../..'))  # Point to local bs4 directory
repo_root = os.path.dirname(os.path.dirname(bs4_dir))  # beautifulsoup directory
print(f"BS4 directory: {bs4_dir}")
sys.path.insert(0, repo_root)

print("="*70)
print("SoupReplacer Verification Script")
print("="*70)
print(f"Repository root: {repo_root}")
print()

# Test 1: Import check
print("Test 1: Checking if SoupReplacer can be imported...")
print("-"*70)
try:
    from bs4 import BeautifulSoup, SoupReplacer
    print("✓ SUCCESS: SoupReplacer imported successfully")
    print(f"  SoupReplacer class: {SoupReplacer}")
except ImportError as e:
    print(f"✗ FAILED: Could not import SoupReplacer")
    print(f"  Error: {e}")
    print("\n  Fix: Make sure you:")
    print("    1. Added SoupReplacer class to bs4/filter.py")
    print("    2. Added 'SoupReplacer' to import in bs4/__init__.py")
    sys.exit(1)

# Test 2: Create SoupReplacer object
print("\nTest 2: Creating SoupReplacer object...")
print("-"*70)
try:
    replacer = SoupReplacer("b", "strong")
    print(f"✓ SUCCESS: Created {replacer}")
    print(f"  Original tag: {replacer.original_tag}")
    print(f"  Replacement tag: {replacer.replacement_tag}")
except Exception as e:
    print(f"✗ FAILED: Could not create SoupReplacer")
    print(f"  Error: {e}")
    sys.exit(1)

# Test 3: Test replace_if_needed method
print("\nTest 3: Testing replace_if_needed() method...")
print("-"*70)
try:
    replacer = SoupReplacer("b", "strong")
    result_b = replacer.replace_if_needed("b")
    result_i = replacer.replace_if_needed("i")
    result_div = replacer.replace_if_needed("div")
    
    if result_b == "strong" and result_i == "i" and result_div == "div":
        print("✓ SUCCESS: replace_if_needed() works correctly")
        print(f"  'b' -> '{result_b}' (expected 'strong')")
        print(f"  'i' -> '{result_i}' (expected 'i')")
        print(f"  'div' -> '{result_div}' (expected 'div')")
    else:
        print("✗ FAILED: replace_if_needed() not working correctly")
        print(f"  'b' -> '{result_b}' (expected 'strong')")
        print(f"  'i' -> '{result_i}' (expected 'i')")
        print(f"  'div' -> '{result_div}' (expected 'div')")
except Exception as e:
    print(f"✗ FAILED: Error in replace_if_needed()")
    print(f"  Error: {e}")

# Test 4: Parse with replacer parameter
print("\nTest 4: Parsing HTML with replacer parameter...")
print("-"*70)
html = "<html><body><b>Bold text</b></body></html>"
print(f"Input HTML: {html}")

try:
    replacer = SoupReplacer("b", "strong")
    soup = BeautifulSoup(html, 'html.parser', replacer=replacer)
    result = str(soup)
    print(f"Output HTML: {result}")
    
    if "<strong>" in result and "<b>" not in result:
        print("✓ SUCCESS: BeautifulSoup accepted replacer parameter")
    else:
        print("✗ FAILED: replacer parameter accepted but not working")
        print("  Fix: Check bs4/__init__.py - did you:")
        print("    1. Add 'replacer' parameter to __init__()?")
        print("    2. Add 'self.replacer = replacer'?")
except TypeError as e:
    print(f"✗ FAILED: BeautifulSoup doesn't accept 'replacer' parameter")
    print(f"  Error: {e}")
    print("\n  Fix: Add 'replacer' parameter to BeautifulSoup.__init__()")
    sys.exit(1)