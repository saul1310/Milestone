"""
SoupReplacer - Tag replacement during parsing for BeautifulSoup

Add this class to bs4/__init__.py (near where SoupStrainer is defined)
"""

class SoupReplacer:
    """
    Encapsulates tag replacement rules to be applied during parsing.
    
    Similar to SoupStrainer which filters elements during parsing,
    SoupReplacer modifies tag names during parsing, avoiding the need
    to traverse the parse tree after parsing is complete.
    
    Example usage:
        # Replace all <b> tags with <blockquote> during parsing
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html_doc, 'html.parser', replacer=replacer)
        # All <b> tags are now <blockquote> tags in the parse tree
    """
    
    def __init__(self, original_tag, replacement_tag):
        """
        Create a SoupReplacer that replaces one tag type with another.
        
        Args:
            original_tag (str): The tag name to be replaced (e.g., "b")
            replacement_tag (str): The tag name to use instead (e.g., "blockquote")
        
        Example:
            replacer = SoupReplacer("i", "em")
            # This will replace all <i> tags with <em> tags during parsing
        """
        self.original_tag = original_tag
        self.replacement_tag = replacement_tag
    
    def replace_if_needed(self, tag_name):
        """
        Check if a tag name should be replaced and return the appropriate name.
        
        This method is called during parsing when the parser encounters a tag.
        If the tag matches original_tag, it returns replacement_tag.
        Otherwise, it returns the tag unchanged.
        
        Args:
            tag_name (str): The name of the tag being processed
        
        Returns:
            str: Either the replacement_tag (if matched) or the original tag_name
        
        Example:
            replacer = SoupReplacer("b", "strong")
            replacer.replace_if_needed("b")      # Returns "strong"
            replacer.replace_if_needed("i")      # Returns "i" (unchanged)
            replacer.replace_if_needed("div")    # Returns "div" (unchanged)
        """
        if tag_name == self.original_tag:
            return self.replacement_tag
        return tag_name
    
    def __repr__(self):
        """String representation for debugging."""
        return f"SoupReplacer('{self.original_tag}' -> '{self.replacement_tag}')"