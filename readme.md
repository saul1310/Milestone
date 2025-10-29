# XML Processing and BeautifulSoup Projects

This repository contains two main projects:
1. XML Processing Tasks (Milestone 1)
2. BeautifulSoup Library Modifications (Milestone 2)

## XML Processing Tasks (Milestone 1)

My project contains eight Python scripts (`task1.py` to `task8.py`) that perform various XML processing operations such as formatting, tag analysis, and element modification.

### Requirements

- **Python 3.8+** installed  
- A valid XML file (for example: `test.xml`)

### How to Run Each Task

Open a terminal in the project directory (`Milestone-1`) and run the following command:

```bash
python taskx.py test.xml
```

where x is the number 1-8 of the task you would like to run.

Note: The code has been tested on a 1 GB file and works successfully (takes about 10 minutes to compile).

## BeautifulSoup Modifications (Milestone 2)

### Repository Structure

```
beautifulsoup/          # Modified BeautifulSoup library
├── bs4/                # Core library code
│   ├── __init__.py    # BeautifulSoup class and imports
│   ├── filter.py      # SoupStrainer and SoupReplacer implementations
│   └── tests/         # Unit tests
└── apps/
    └── m2/            # Milestone 2 applications
        ├── task2.py   # Hyperlink extraction using SoupStrainer
        ├── task3.py   # Tag counting using SoupStrainer
        ├── task4.py   # ID attribute detection using SoupStrainer
        └── verify_replacer.py  # SoupReplacer verification script
```

### Running the Tests

#### SoupReplacer Verification

To verify the SoupReplacer functionality:

1. Navigate to the beautifulsoup directory:
```bash
cd beautifulsoup
```

2. Run the verification script:
```bash
python bs4/apps/m2/verify_replacer.py
```

The script will run several tests to verify:
- SoupReplacer can be imported
- SoupReplacer objects can be created
- Tag replacement works correctly
- BeautifulSoup accepts and uses the replacer parameter

### Milestone 2 Files Documentation

#### Part 1: SoupReplacer Implementation

1. `bs4/filter.py`
   - Contains the implementation of the `SoupReplacer` class
   - Used for replacing specified HTML tags with alternative tags during parsing
   - Example: Replacing `<b>` tags with `<strong>` tags

2. `bs4/__init__.py`
   - Modified to expose the `SoupReplacer` class
   - Added replacer parameter to BeautifulSoup constructor
   - Integrated tag replacement functionality into parsing process

3. `bs4/apps/m2/verify_replacer.py`
   - Test script to verify SoupReplacer functionality
   - Runs through various test cases
   - Provides detailed feedback on test results

4. `Milestone-2/M2-README.md`
   - Documentation of BeautifulSoup API function mappings
   - Lists all BeautifulSoup functions used in Milestone 1 and Part 1 of Milestone 2
   - Maps functions to their source code locations

### Issues and Support

If you encounter any issues or need support:
1. Check the error messages from the verification script
2. Review the comments in the source code files
3. Consult the M2-README.md for API function documentation