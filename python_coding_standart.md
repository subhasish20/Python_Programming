# Python Coding Standards 

## 1. PEP 8 and Why Coding Standards Matter
- **Rule:** Follow **PEP 8**, Python's official style guide.
- **Why:** Consistent code is easier to read, review, and maintain; code is read far more often than it is written.
- **Good example:**
```python
def calculate_total(price, tax_rate):
    return price * (1 + tax_rate)
```
- **Bad example:**
```python
def CalculateTotal( p,tr ):
  return p*(1+tr)
```

## 2. Naming Conventions
- **Rule:** Variables/functions use **snake_case**; classes use **PascalCase**; constants use **UPPER_CASE**.
- **Why:** Naming style instantly signals what a name represents.
- **Good example:**
```python
user_count = 10

def get_user_name():
    pass

class UserAccount:
    pass

MAX_RETRIES = 3
```
- **Bad example:**
```python
UserCount = 10      # looks like a class
def GetUserName():  # looks like a class
    pass
class user_account: # looks like a variable
    pass
max_retries = 3     # looks like a mutable variable
```

## 3. Indentation and Whitespace
- **Rule:** Use **4 spaces per indentation level** — never tabs; surround operators with single spaces; no trailing whitespace.
- **Why:** Mixed indentation breaks code or hides logic errors; Python relies on indentation for structure.
- **Good example:**
```python
if is_active:
    total = price + tax
```
- **Bad example:**
```python
if is_active:
        total=price+tax   # 8 spaces, no operator spacing
```

## 4. Line Length and Code Formatting
- **Rule:** Keep lines to **79 characters** (PEP 8) — up to 99 is a common team convention; break long lines with parentheses.
- **Why:** Long lines force horizontal scrolling and are hard to review side by side.
- **Good example:**
```python
result = calculate_report(
    start_date, end_date,
    include_tax=True,
)
```
- **Bad example:**
```python
result = calculate_report(start_date, end_date, include_tax=True, currency="USD", region="EU", verbose=True)
```

## 5. Writing Clean and Readable Code
- **Rule:** Prefer **explicit, simple code** over clever tricks; use descriptive names.
- **Why:** Readability beats brevity — others (and future you) must understand it.
- **Good example:**
```python
is_adult = age >= 18
```
- **Bad example:**
```python
is_adult = not (age < 18) != False
```

## 6. Writing Small, Focused Functions
- **Rule:** Each function does **one thing**; keep functions short.
- **Why:** Small functions are easier to test, name, reuse, and debug.
- **Good example:**
```python
def validate_email(email):
    return "@" in email and "." in email

def send_welcome_email(user):
    if validate_email(user.email):
        mailer.send(user.email, "Welcome!")
```
- **Bad example:**
```python
def process_user(user):
    # validates, saves to DB, sends email, logs — all in one function
    ...
```

## 7. Avoiding Duplicate Code (DRY)
- **Rule:** **Don't Repeat Yourself** — extract repeated logic into functions.
- **Why:** Duplicated code means fixing the same bug in many places.
- **Good example:**
```python
def area(radius):
    return 3.14159 * radius ** 2

a1 = area(5)
a2 = area(10)
```
- **Bad example:**
```python
a1 = 3.14159 * 5 ** 2
a2 = 3.14159 * 10 ** 2
```

## 8. Avoiding Magic Numbers
- **Rule:** Replace unexplained literals with **named constants**.
- **Why:** Names explain intent and make values easy to change in one place.
- **Good example:**
```python
SECONDS_PER_DAY = 86400
timeout = SECONDS_PER_DAY
```
- **Bad example:**
```python
timeout = 86400  # what is 86400?
```

## 9. Proper Use of Data Structures
- **Rule:** Choose the right structure: **list** (ordered items), **tuple** (fixed records), **dict** (key→value lookup), **set** (uniqueness/membership).
- **Why:** The right structure gives clarity and correct performance (e.g., `in` is O(1) for sets, O(n) for lists).
- **Good example:**
```python
seen_ids = set()
if user_id not in seen_ids:
    seen_ids.add(user_id)
```
- **Bad example:**
```python
seen_ids = []
if user_id not in seen_ids:  # slow linear scan for large lists
    seen_ids.append(user_id)
```

## 10. Type Hints
- **Rule:** Add **type annotations** to function parameters and return values.
- **Why:** Catches bugs early (with tools like mypy) and documents expected types.
- **Good example:**
```python
def greet(name: str, times: int = 1) -> str:
    return (name + "! ") * times
```
- **Bad example:**
```python
def greet(name, times=1):
    return (name + "! ") * times
```

## 11. Docstrings
- **Rule:** Every **public module, class, and function** gets a docstring (triple quotes, first line is a summary).
- **Why:** Docstrings power `help()`, IDEs, and documentation tools.
- **Good example:**
```python
def calculate_tax(price: float, rate: float) -> float:
    """Return the tax amount for a price at the given rate."""
    return price * rate
```
- **Bad example:**
```python
def calculate_tax(price, rate):
    # this calculates tax
    return price * rate
```

## 12. Exception Handling
- **Rule:** Catch **specific exceptions**; keep `try` blocks small; never use bare `except:`.
- **Why:** Bare/blanket catches hide real bugs and swallow errors like `KeyboardInterrupt`.
- **Good example:**
```python
try:
    value = int(user_input)
except ValueError:
    print("Please enter a number.")
```
- **Bad example:**
```python
try:
    value = int(user_input)
except:  # catches everything, including real bugs
    pass   # silently ignores the error
```

## 13. Imports and Import Organization
- **Rule:** Order imports: **standard library → third-party → local**, one per line, at the top of the file; avoid `from x import *`.
- **Why:** Organized imports prevent name collisions and make dependencies obvious.
- **Good example:**
```python
import os
import sys

import requests

from myapp.utils import format_date
```
- **Bad example:**
```python
from myapp.utils import *
import requests, os, sys  # wildcard + multiple imports on one line
```

## 14. Avoiding Unnecessary Global Variables
- **Rule:** Avoid globals for mutable state; **pass data through parameters and return values**.
- **Why:** Globals create hidden dependencies and make code hard to test and reason about.
- **Good example:**
```python
def add_score(scores, points):
    return scores + points

total = add_score(total, 10)
```
- **Bad example:**
```python
total = 0

def add_score(points):
    global total
    total += points
```

## 15. Mutable Default Arguments
- **Rule:** **Never use mutable objects** (list, dict, set) as default arguments; use `None` instead.
- **Why:** Defaults are created once at function definition — mutations persist between calls.
- **Good example:**
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```
- **Bad example:**
```python
def add_item(item, items=[]):  # shared list across calls!
    items.append(item)
    return items
```

## 16. Boolean and None Comparisons
- **Rule:** Use **`is` / `is not`** for `None`; use truthiness (`if x:`) instead of `== True`.
- **Why:** `None` is a singleton — identity comparison is correct and faster; `== True` is redundant and can misfire.
- **Good example:**
```python
if result is None:
    ...
if items:  # non-empty
    ...
```
- **Bad example:**
```python
if result == None:
    ...
if items == True:
    ...
```

## 17. Using Context Managers
- **Rule:** Use **`with`** for files, locks, and connections.
- **Why:** Guarantees cleanup (closing/releasing) even if an exception occurs.
- **Good example:**
```python
with open("data.txt") as f:
    content = f.read()
```
- **Bad example:**
```python
f = open("data.txt")
content = f.read()
f.close()  # never runs if read() raises
```

## 18. Testing and Code Quality
- **Rule:** Write **unit tests** (pytest/unittest) and run linters/formatters (**ruff, flake8, black**).
- **Why:** Tests catch regressions; automated tools enforce standards so reviews focus on logic.
- **Good example:**
```python
def test_calculate_tax():
    assert calculate_tax(100, 0.2) == 20
```
- **Bad example:**
```python
# no tests, style checked by hand "when there's time"
```

---

# Special Section: How to Write Better Comments

1. **Explain WHY, not the obvious WHAT** — code already shows what it does.
2. **Keep comments short and specific** — one clear idea per comment.
3. **Add information not visible in the code** — reasons, constraints, sources.
4. **Keep comments up to date** — a stale comment is worse than none.
5. **Avoid redundant comments** — don't restate the code in English.
6. **Explain complex business logic** — rules readers can't infer.
7. **Explain unusual decisions or workarounds** — why the non-obvious approach was chosen.
8. **Clarify assumptions** — e.g., expected input format or units.
9. **Prefer clear code over excessive comments** — rename or refactor first.
10. **Use TODO/FIXME appropriately** — mark future work, with context.
11. **Don't comment every line** — it adds noise, not clarity.
12. **Use docstrings for functions/classes**, not ordinary `#` comments.

### Core example

```python
# Bad
# Add 1 to count
count = count + 1

# Good
# Retry because the API occasionally returns a temporary 503 error.
retry_count += 1
```

### Comment types

- **Inline comment** — short note on the same line as code (use sparingly, separated by 2+ spaces).
```python
timeout = 30  # seconds; payment gateway times out at 45s
```
- **Block comment** — one or more full lines explaining the code that follows.
```python
# Prices are stored in cents to avoid floating-point
# rounding errors when summing large orders.
total_cents = sum(item.price_cents for item in cart)
```
- **Docstring** — triple-quoted string documenting a module, class, or function; visible via `help()`.
```python
def fetch_user(user_id: int) -> User:
    """Fetch a user by ID. Raises UserNotFound if missing."""
```
- **TODO / FIXME** — marks planned work or known problems.
```python
# TODO: cache this query — it's called on every request
# FIXME: breaks when the list is empty
```

---

## Quick Revision Checklist

- [ ] Follow **PEP 8**; run a linter (ruff/flake8) and formatter (black).
- [ ] **snake_case** functions/variables, **PascalCase** classes, **UPPER_CASE** constants.
- [ ] **4 spaces** indentation; lines ≤ **79 characters**.
- [ ] Functions are **small and do one thing**.
- [ ] **DRY** — no duplicated logic; no **magic numbers** (use named constants).
- [ ] Right **data structure** for the job (set for membership, dict for lookup).
- [ ] **Type hints** and **docstrings** on public functions/classes.
- [ ] Catch **specific exceptions**; never bare `except:`.
- [ ] Imports ordered **stdlib → third-party → local**; no wildcard imports.
- [ ] Avoid **global variables** and **mutable default arguments** (use `None`).
- [ ] Compare with **`is None`**; use truthiness instead of `== True`.
- [ ] Use **`with`** for files and resources.
- [ ] Write **tests**; comments explain **WHY**, not what; keep comments current.
