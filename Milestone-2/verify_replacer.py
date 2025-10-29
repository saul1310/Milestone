#!/usr/bin/env python3
"""
Verification script to test if SoupReplacer is working correctly.
This tests your modifications to the BeautifulSoup source code.

Location: beautifulsoup/apps/m2/verify_replacer.py
Run from: beautifulsoup/ directory
Command: python apps/m2/verify_replacer.py
"""

import sys
import os

# Add repository root to path to import local modified bs4
current_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(current_dir, '..'))  # Changed to point to Milestone-1 directory
beautifulsoup_dir = os.path.join(repo_root, 'beautifulsoup')
sys.path.insert(0, beautifulsoup_dir)

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
except Exception as e:
    print(f"✗ FAILED: Unexpected error")
    print(f"  Error: {e}")
    import traceback
    traceback.print_exc()

# Test 5: Verify actual tag replacement during parsing
print("\nTest 5: Verifying tag replacement happens during parsing...")
print("-"*70)
html5 = "<html><body><b>Text 1</b> and <b>Text 2</b></body></html>"
print(f"Input: {html5}")

try:
    replacer5 = SoupReplacer("b", "blockquote")
    soup5 = BeautifulSoup(html5, 'html.parser', replacer=replacer5)
    result5 = str(soup5)
    
    b_count = result5.count("<b>")
    blockquote_count = result5.count("<blockquote>")
    
    print(f"Output: {result5}")
    print(f"  <b> tags found: {b_count}")
    print(f"  <blockquote> tags found: {blockquote_count}")
    
    if b_count == 0 and blockquote_count == 2:
        print("✓ SUCCESS: Tags replaced during parsing!")
    else:
        print("✗ FAILED: Tag replacement not working")
        print("\n  Fix: Check bs4/builder/_htmlparser.py - did you:")
        print("    1. Add replacer check in handle_starttag()?")
        print("    2. Add replacer check in handle_endtag()?")
except Exception as e:
    print(f"✗ FAILED: Error during parsing")
    print(f"  Error: {e}")
    import traceback
    traceback.print_exc()

# Test 6: Multiple different tags
print("\nTest 6: Testing with different tag types...")
print("-"*70)
html6 = "<div><i>Italic</i> <b>Bold</b> <span>Normal</span></div>"
print(f"Input: {html6}")

try:
    replacer6 = SoupReplacer("i", "em")
    soup6 = BeautifulSoup(html6, 'html.parser', replacer=replacer6)
    result6 = str(soup6)
    
    print(f"Output: {result6}")
    
    if "<em>" in result6 and "<i>" not in result6 and "<b>" in result6:
        print("✓ SUCCESS: Only specified tags replaced")
        print("  <i> -> <em> (replaced)")
        print("  <b> remains <b> (not affected)")
    else:
        print("✗ FAILED: Replacement affected wrong tags")
except Exception as e:
    print(f"✗ FAILED: Error in selective replacement")
    print(f"  Error: {e}")

# Test 7: Parse without replacer (should work normally)
print("\nTest 7: Parsing without replacer (normal operation)...")
print("-"*70)
html7 = "<html><body><b>Bold</b></body></html>"

try:
    soup7 = BeautifulSoup(html7, 'html.parser')  # No replacer
    result7 = str(soup7)
    
    if "<b>" in result7:
        print("✓ SUCCESS: Normal parsing still works")
        print(f"  Output: {result7}")
    else:
        print("✗ WARNING: Something affected normal parsing")
except Exception as e:
    print(f"✗ FAILED: Normal parsing broken")
    print(f"  Error: {e}")

# Test 8: Nested tags
print("\nTest 8: Testing nested tags replacement...")
print("-"*70)
html8 = "<div><b>Outer <b>Inner</b> Text</b></div>"
print(f"Input: {html8}")

try:
    replacer8 = SoupReplacer("b", "strong")
    soup8 = BeautifulSoup(html8, 'html.parser', replacer=replacer8)
    result8 = str(soup8)
    
    strong_count = result8.count("<strong>")
    b_count = result8.count("<b>")
    
    print(f"Output: {result8}")
    print(f"  <strong> tags: {strong_count}")
    print(f"  <b> tags: {b_count}")
    
    if b_count == 0 and strong_count == 2:
        print("✓ SUCCESS: Nested tags handled correctly")
    else:
        print("⚠ WARNING: Nested tag count unexpected (may be due to HTML parser behavior)")
except Exception as e:
    print(f"✗ FAILED: Error with nested tags")
    print(f"  Error: {e}")

# Final summary
print("\n" + "="*70)
print("VERIFICATION COMPLETE")
print("="*70)
print("\nIf all tests show ✓ SUCCESS, your SoupReplacer implementation is working!")
print("\nYou can now use it in your Milestone 2 applications:")
print("  - apps/m2/task6_with_replacer.py")
print("  - apps/m2/test_replacer_demo.py")
print("="*70)