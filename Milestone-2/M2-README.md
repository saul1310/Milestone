# Mapping of BeautifulSoup API functions used in Milestone-1 and Milestone-2 (Part 1)

Lists every BeautifulSoup API function/class that I used in the the Milestone-1 tasks and the Milestone-2 (Part-1 only so far) scripts in this repository, and points to the file+line where each function is defined in the local `beautifulsoup/bs4` source tree.

## Summary table (project file -> BeautifulSoup API items used -> bs4 source file : line)

### Milestone-1

#### `task1.py`
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.prettify()`
  - `bs4/element.py` : def prettify at line 2601

#### `task2.py`
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.find_all('a')`
  - `bs4/element.py` : def find_all at line 2715
- `link.get('href')`
  - `bs4/element.py` : def get at line 2160
- `link.get_text(strip=True)`
  - `bs4/element.py` : def get_text at line 524
- `link.attrs` / `link.attrs.items()`
  - `bs4/element.py` : Tag `self.attrs` created in `Tag.__init__` at lines ~1560-1682 

#### `task3.py`
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.find_all(True)` (find all tags)
  - `bs4/element.py` : def find_all at line 2715
- `tag.get_text()`
  - `bs4/element.py` : def get_text at line 524

#### `task4.py`
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.find_all(id=True)`
  - `bs4/element.py` : def find_all at line 2715
- `tag.get('id')`, `tag.get_text()`
  - `bs4/element.py` : def get at line 2160; def get_text at line 524

#### `task5.py`
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.find_all('a')`
  - `bs4/element.py` : def find_all at line 2715
- `link.find_parent()`
  - `bs4/element.py` : def find_parent at line 992
- `tag.has_attr('class')` and `tag['class']` (setting/getting attributes)
  - `bs4/element.py` : def has_attr at line 2196; def __setitem__ at line 2216; def __getitem__ at line 2210+ (see below)

#### `task6.py` (Milestone-1)
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.find_all('b')`
  - `bs4/element.py` : def find_all at line 2715
- `b_tag.name = 'blockquote'` (Tag name assignment)
  - Tag name stored on `Tag` objects; Tag constructor and attribute assignment at `bs4/element.py` : `Tag.__init__` starts at line ~1569 and assigns `self.name` at line ~1598 (see below)
- `str(soup)` used to write output (stringify the tree)
  - `bs4/element.py` : encoding/decoding output handled by `Tag.decode`/`PageElement` methods and `prettify` (`prettify` at 2601; decode/encode helpers are also defined in `element.py`)

#### `task7.py`
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.find_all('p')`
  - `bs4/element.py` : def find_all at line 2715
- attribute access/assignment `p_tag['class'] = 'test'`
  - `bs4/element.py` : def __setitem__ at line 2216
- `new_soup.find_all('p', class_='test')` uses `find_all`
  - `bs4/element.py` : def find_all at line 2715

#### `task8.py`
- BeautifulSoup(...) (constructor)
  - `bs4/__init__.py` : def __init__ at line 211
- `soup.select('.mw-body')`, `soup.select('div p')`, etc. (CSS selectors)
  - `bs4/element.py` : def select_one at line 2782; def select at line 2799
- `elem.get('class')`, `.get_text(strip=True)`
  - `bs4/element.py` : def get at line 2160; def get_text at line 524


### Milestone-2 (Part-1)

#### `Milestone-2/task2.py`
- `SoupStrainer("a")` instantiation
  - `bs4/filter.py` : class `SoupStrainer` defined at line 313; constructor `def __init__` at line ~345
- BeautifulSoup(..., parse_only=only_a_tags)
  - `bs4/__init__.py` : BeautifulSoup constructor handles `parse_only` parameter; constructor at line 211 and uses `parse_only` internally (see `if parse_only is not None:` near lines ~260 in file)
- `soup.find_all('a')` etc.
  - `bs4/element.py` : def find_all at line 2715

#### `Milestone-2/task3.py`
- `SoupStrainer(True)`
  - `bs4/filter.py` : class `SoupStrainer` at line 313; `__init__` around line 345
- `soup.find_all(True)`
  - `bs4/element.py` : def find_all at line 2715

#### `Milestone-2/task4.py`
- `SoupStrainer(id=True)`
  - `bs4/filter.py` : class `SoupStrainer` at line 313; `__init__` around line 345
- `soup.find_all(id=True)`
  - `bs4/element.py` : def find_all at line 2715

#### `Milestone-2/task6.py` (SoupReplacer helper in M2)
- `class SoupReplacer(...)` — NOTE: this is an added helper that is included in `Milestone-2/task6.py` (this file contains a light copy/definition used by the tests). The `SoupReplacer` class is also implemented in this repository inside `bs4/filter.py` as part of the changes done during the milestone work. This class did not exist in upstream BeautifulSoup 4.13.0 unless you add it.
  - Local copy in `Milestone-2/task6.py` : `def __init__` at line 22 (file-local)
  - Local implementation in `bs4/filter.py` : class `SoupReplacer` defined at line ~701 (this is an added class in this repo)

#### `Milestone-2/verify_replacer.py`
- `from bs4 import BeautifulSoup, SoupReplacer`
  - `bs4/__init__.py` : `SoupReplacer` is imported from `bs4/filter.py` in the package `__init__` (see `from .filter import (ElementFilter, SoupStrainer, SoupReplacer,)` in `bs4/__init__.py` around lines ~70-80)
- `BeautifulSoup(..., replacer=replacer)` (passing replacer into constructor)
  - `bs4/__init__.py` : the local constructor was extended to accept a `replacer` parameter; this parameter is stored on the `BeautifulSoup` instance (see `self.replacer = replacer` at line ~437 in current copy). Note: this is a local modification added while implementing the Milestone change.
- The actual replacement during parsing was implemented by adding replacer checks in the `html.parser`-based parser:
  - `bs4/builder/_htmlparser.py` : `BeautifulSoupHTMLParser.handle_startendtag` and `handle_starttag` and `handle_endtag` were updated to call `self.soup.replacer.replace_if_needed(name)` if `self.soup.replacer` is present. These lines are local modifications made during the milestone.


---

## Exact bs4 source locations (selected, with context)
(These are the concrete locations in the repository's `beautifulsoup/bs4` directory that implement the API items above.)

- `bs4/__init__.py`:
  - `class BeautifulSoup(Tag):` — starts at line 134
  - `def __init__(...):` — starts at line 211
  - `self.replacer = replacer` (local modification) — currently on line ~437

- `bs4/element.py`:
  - `def get_text(...)` — line 524
  - `def prettify(...)` — line 2601
  - `def find_all(...)` — line 2715
  - `def select_one(...)` — line 2782
  - `def select(...)` — line 2799
  - `def get(...)` — line 2160
  - `def find_parent(...)` — line 992
  - `def has_attr(...)` — line 2196
  - `def __setitem__(...)` — line 2216
  - `Tag.__init__` (where `self.attrs` and `self.name` are set) — starts at line ~1569; `self.attrs = attr_dict_class()` at lines ~1675-1682

- `bs4/filter.py`:
  - `class ElementFilter` — at top of file
  - `class SoupStrainer(ElementFilter)` — starts at line 313
  - `SoupStrainer.__init__` — starts at line ~345
  - (Added) `class SoupReplacer` — starts at line ~701 (this is an added class in this repo; not in vanilla upstream 4.13.0)

- `bs4/_warnings.py`:
  - `class XMLParsedAsHTMLWarning(UnusualUsageWarning):` — starts at line 83

- `bs4/builder/_htmlparser.py`:
  - `class BeautifulSoupHTMLParser(HTMLParser, DetectsXMLParsedAsHTML):` — near line 1..100
  - `def handle_startendtag(...)` — present and contains replacer check (local modification)
  - `def handle_starttag(...)` — present and now contains replacer check (local modification)
  - `def handle_endtag(...)` — present and now contains replacer check (local modification)


---

If you'd like, next steps I can take for you:
1. Fetch the original upstream BeautifulSoup 4.13.0 source and provide verified upstream file+line numbers (so the references truly match "before any local edits").
2. Generate a compact CSV or machine-readable mapping instead of a Markdown README.
3. Include code snippets showing the exact lines from the bs4 source for each API item.

Which of the next steps would you like me to take? (I can continue and fetch upstream sources to provide exact upstream line numbers if you want fully original references.)
