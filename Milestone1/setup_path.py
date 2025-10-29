import sys
import os

# Add the local beautifulsoup directory to Python's path
beautifulsoup_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'beautifulsoup'))
if beautifulsoup_dir not in sys.path:
    sys.path.insert(0, beautifulsoup_dir)