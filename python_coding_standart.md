# Python Coding Standards and Best Practices

**Professional Study Notes — Beginner to Intermediate**

> These notes are a working reference, not a style manifesto. Where a rule comes from PEP 8, it is marked. Where it comes from common industry practice, it is marked. Personal preference is labelled as such so you can tell the difference.

---

## Table of Contents

1. [How to Use These Notes](#0-how-to-use-these-notes)
2. [Python Coding Standards](#1-python-coding-standards)
3. [Writing Good Comments](#2-writing-good-comments)
4. [Good vs Bad Comments](#3-good-vs-bad-comments)
5. [Docstrings](#4-docstrings)
6. [Writing Self-Documenting Code](#5-writing-self-documenting-code)
7. [Professional Code Review Rules](#6-professional-code-review-rules)
8. [Common Mistakes](#7-common-mistakes)
9. [Real-World Examples](#8-real-world-examples)
10. [Professional Python Commenting Rules — Quick Reference](#professional-python-commenting-rules--quick-reference)
11. [Code Review Checklist](#code-review-checklist)
12. [Golden Rule](#golden-rule)

---

## 0. How to Use These Notes

Each important rule in this document follows the same structure:

> **Rule → Why it matters → Bad example → Good example → Professional takeaway**

Read the **Why** even when the rule seems obvious. Senior engineers follow rules because they understand the cost of breaking them, not because a linter complains.

Two terms used throughout:

- **PEP 8** — the official Python style guide (Python Enhancement Proposal 8). It is the baseline for the standard library and most professional Python codebases.
- **Industry practice** — conventions that are not in PEP 8 but are widespread in production code (e.g., using `black` for formatting, choosing 88-character line length, Google-style docstrings).

---

## 1. Python Coding Standards

### 1.1 PEP 8 and Why Coding Standards Matter

**Rule:** Follow PEP 8 for formatting and naming unless your team has an explicit, documented reason to deviate.

**Why it matters:**

- Code is read far more often than it is written. Standards reduce the cognitive cost of reading unfamiliar code.
- Consistent style makes diffs smaller and code reviews faster — reviewers discuss logic, not spacing.
- Tools (`black`, `ruff`, `flake8`, `isort`, `mypy`) can only automate what is predictable.
- PEP 8 is the shared vocabulary of the Python community. Deviating without reason signals inexperience.

**Bad example:**

```python
def  calcTotal( price, qty ):
    return price*qty
```

**Good example:**

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

**Professional takeaway:** Standards are not about aesthetics. They are about reducing the cost of every future read of the code — including your own six months from now.

---

### 1.2 Naming Conventions

**Rule:** Use the naming convention appropriate to the kind of name. PEP 8 defines the defaults.

| Kind | Convention | Example |
|---|---|---|
| Module / package | `snake_case`, short | `user_service.py` |
| Function / method | `snake_case` | `fetch_invoice()` |
| Variable | `snake_case` | `retry_count` |
| Class | `PascalCase` | `InvoiceRepository` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_RETRIES = 3` |
| "Private" internal | leading underscore | `_cache`, `_normalize()` |
| Name-mangled | double leading underscore | `__internal_state` |
| Type variable | `PascalCase`, often `T` | `T = TypeVar("T")` |

**Why it matters:**

- The reader can tell at a glance whether a name is a class, a function, or a constant.
- Python has no compiler-enforced privacy; naming is the only signal.

**Bad example:**

```python
class user_account:          # class should be PascalCase
    pass

MAXRETRIES = 3               # hard to read
Def calculateTotal():        # invalid, but shows the intent problem
    ...
```

**Good example:**

```python
class UserAccount:
    pass

MAX_RETRIES = 3

def calculate_total() -> float:
    ...
```

**Professional takeaway:** A name should reveal *what the thing is*, not *how it is implemented*. Prefer `active_users` over `list_of_users_that_are_active`.

> **Note:** PEP 8 recommends `snake_case` for functions and variables. Some codebases inherit `camelCase` from other languages; that is a team decision, not a PEP 8 recommendation.

---

### 1.3 Indentation and Whitespace

**Rule:** Use 4 spaces per indentation level. Never mix tabs and spaces. Use blank lines to separate logical blocks.

**Why it matters:**

- Python uses indentation semantically. Inconsistent indentation is a bug, not a style issue.
- Mixing tabs and spaces causes `TabError` and makes code unreadable in some editors.
- Whitespace around operators and after commas improves scanability.

**Bad example:**

```python
def process(items):
  total=0
  for i in items:
        total+=i
  return total
```

**Good example:**

```python
def process(items: list[int]) -> int:
    total = 0
    for item in items:
        total += item
    return total
```

**Professional takeaway:** Let a formatter (`black`, `ruff format`) handle whitespace. You should never spend review time discussing spaces.

> **PEP 8 note:** Use blank lines sparingly. Two blank lines around top-level functions and classes; one blank line between methods inside a class.

---

### 1.4 Line Length

**Rule:** Keep lines reasonably short. PEP 8's traditional limit is **79 characters**; many modern teams use **88** (Black's default) or **100**.

**Why it matters:**

- Short lines fit side-by-side diffs and narrow terminals.
- Long lines hide nesting and make expressions hard to parse.
- A consistent limit lets tools wrap code automatically.

**Bad example:**

```python
result = calculate_invoice_total(customer_id, invoice_id, apply_discount=True, include_tax=True, currency="USD")
```

**Good example:**

```python
result = calculate_invoice_total(
    customer_id,
    invoice_id,
    apply_discount=True,
    include_tax=True,
    currency="USD",
)
```

**Professional takeaway:** The exact number matters less than consistency. Pick one, encode it in `pyproject.toml`, and let the formatter enforce it.

> **PEP 8** recommends 79. **Industry practice** increasingly uses 88 or 100. Both are acceptable; document your choice.

---

### 1.5 Imports

**Rule:** Group imports in this order, separated by blank lines:

1. Standard library
2. Third-party packages
3. Local application / package imports

Prefer absolute imports. Avoid wildcard imports.

**Why it matters:**

- Grouping makes dependencies obvious at a glance.
- Absolute imports are unambiguous and survive refactors better than relative imports.
- `from module import *` pollutes the namespace and hides where names come from.

**Bad example:**

```python
import os, sys
from .models import *
import requests
from myapp.utils import parse
import json
```

**Good example:**

```python
import json
import os
import sys

import requests

from myapp.models import User
from myapp.utils import parse
```

**Professional takeaway:** `isort` or `ruff` can enforce import order automatically. Run it before review.

---

### 1.6 Functions and Classes

**Rule:** A function should do one thing. A class should have one reason to change. Keep functions short enough to read without scrolling.

**Why it matters:**

- Small functions are testable, reusable, and easy to name.
- Classes with a single responsibility are easier to mock, extend, and reason about.
- Long functions accumulate hidden state and branching that is hard to test.

**Bad example:**

```python
def handle_request(request):
    # validate, parse, query DB, send email, log, format response...
    ...
```

**Good example:**

```python
def handle_request(request: Request) -> Response:
    payload = parse_payload(request)
    user = fetch_user(payload.user_id)
    send_welcome_email(user)
    return build_response(user)
```

**Professional takeaway:** If you cannot name a function without using "and", it is probably doing too much. Split it.

---

### 1.7 Constants and Variables

**Rule:** Use `UPPER_SNAKE_CASE` for module-level constants. Use `snake_case` for local variables. Avoid magic numbers and strings in logic.

**Why it matters:**

- A named constant documents intent and gives you one place to change a value.
- Magic numbers force readers to guess what `86400` means.

**Bad example:**

```python
if elapsed > 86400:
    expire_session()
```

**Good example:**

```python
SECONDS_PER_DAY = 86_400

if elapsed > SECONDS_PER_DAY:
    expire_session()
```

**Professional takeaway:** A constant is a comment that the interpreter understands. Prefer it over an explanatory comment.

---

### 1.8 File and Project Organization

**Rule:** Organize code by responsibility, not by accident. A typical professional layout:

```
my_project/
├── pyproject.toml
├── README.md
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── models.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── billing.py
│       └── utils/
│           └── dates.py
└── tests/
    ├── test_billing.py
    └── test_dates.py
```

**Why it matters:**

- New contributors find code by convention, not by searching.
- Tests mirror source structure, so a failing test points to the relevant module.
- `src/` layout prevents accidental imports of the working directory.

**Professional takeaway:** Project layout is a team convention. The important thing is that it is *consistent* and *documented* in the README.

---

### 1.9 Type Hints

**Rule:** Add type hints to public functions, methods, and module-level data. Use modern syntax where your Python version supports it.

**Why it matters:**

- Type hints are executable documentation: they tell readers and tools what is expected.
- `mypy` / `pyright` catch entire classes of bugs before runtime.
- IDEs autocomplete more accurately.

**Bad example:**

```python
def get_user(id):
    return db.fetch("users", id)
```

**Good example:**

```python
from typing import Optional

def get_user(user_id: int) -> Optional[dict]:
    return db.fetch("users", user_id)
```

**Modern (Python 3.10+):**

```python
def get_user(user_id: int) -> dict | None:
    return db.fetch("users", user_id)
```

**Professional takeaway:** Type hints are not optional in professional Python. They are the cheapest form of documentation you can write, and they are checked by tools.

> **PEP 484** introduced type hints. **PEP 604** introduced `X | Y`. **PEP 585** introduced `list[int]` instead of `List[int]`.

---

### 1.10 Docstrings (Overview)

Docstrings are covered in depth in [Section 4](#4-docstrings). The rule of thumb:

- **Every public module, class, and function** should have a docstring.
- **Private helpers** may skip docstrings if the name and signature are self-explanatory.

---

### 1.11 Code Readability

**Rule:** Optimize for the reader. Prefer explicit over implicit, simple over clever, and flat over nested.

**Why it matters:**

- Clever code is a liability. It is hard to debug, hard to review, and hard to change.
- Readable code reduces onboarding time and the frequency of "what does this do?" questions.

**Bad example:**

```python
result = [x for x in y if x if x > 0 if x % 2 == 0]
```

**Good example:**

```python
positive_evens = [
    number
    for number in numbers
    if number > 0 and number % 2 == 0
]
```

**Professional takeaway:** If you are proud of how clever a line is, rewrite it. Cleverness is not a virtue in production code.

---

## 2. Writing Good Comments

Comments are not decoration. They are a maintenance cost. Every comment must earn its place.

### 2.1 When a Comment Is Necessary

**Rule:** Write a comment when the *why* is not obvious from the code.

Necessary comments explain:

- **Intent** the code cannot express (business rules, regulatory requirements).
- **Trade-offs** ("we use this O(n²) algorithm because n < 50 and clarity matters more").
- **Workarounds** for bugs in dependencies or the interpreter.
- **Non-obvious invariants** ("this list is always sorted by `created_at`").
- **Warnings** ("this call must happen before `commit()`").

```python
# Stripe requires the idempotency key to be stable across retries;
# regenerating it here would cause duplicate charges.
idempotency_key = f"order-{order.id}"
```

### 2.2 When a Comment Is Unnecessary

**Rule:** Do not comment what the code already says clearly.

Unnecessary comments:

- Restate the next line.
- Explain the language itself.
- Compensate for bad naming.
- Describe *what* instead of *why*.

```python
# Bad: restates the code
i += 1  # increment i

# Bad: compensates for a bad name
d = 7  # number of days in a week

# Good: the name carries the meaning
DAYS_PER_WEEK = 7
```

### 2.3 What a Comment Should Contain

A good comment contains one of:

- A reason.
- A constraint.
- A consequence.
- A reference (issue tracker, RFC, commit hash).

A good comment does **not** contain:

- A restatement of the code.
- A history of the code (that is what git is for).
- A personal opinion about the code.
- A TODO with no owner or context.

### 2.4 Explain *Why*, Not *What*

**Rule:** The code explains *what*. The comment explains *why*.

**Bad example:**

```python
# Sort the users by signup date
users.sort(key=lambda u: u.signup_date)
```

**Good example:**

```python
# Newest users first: the onboarding banner only applies to accounts
# created in the last 30 days, so we avoid scanning the full list.
users.sort(key=lambda u: u.signup_date, reverse=True)
```

**Professional takeaway:** If a comment could be replaced by a better variable name, replace the name instead.

### 2.5 Keep Comments Short and Meaningful

**Rule:** A comment should be as short as it can be while still conveying the reason.

**Bad example:**

```python
# This function loops over all the items in the list and checks whether
# each item is valid by calling validate() on it, and if the item is
# valid it appends it to the output list, otherwise it skips the item.
```

**Good example:**

```python
# Skip invalid rows rather than failing the whole batch.
```

### 2.6 Avoid Outdated or Misleading Comments

**Rule:** A wrong comment is worse than no comment. Update or delete comments whenever the code changes.

**Bad example:**

```python
# Cache for 60 seconds
CACHE_TTL = 300
```

The comment is now a lie. A future reader will trust it and be wrong.

**Good example:**

```python
CACHE_TTL_SECONDS = 300
```

The name is the comment, and it cannot drift.

### 2.7 Maintain Comments When Code Changes

**Rule:** Treat comments as part of the code. If you change the code, change the comment in the same commit.

**Professional takeaway:** Reviewers should reject a PR that leaves a stale comment. It is a correctness issue, not a cosmetic one.

### 2.8 Inline Comments

**Rule:** Use inline comments sparingly, for short clarifications. Place them at least two spaces after the code.

**When to use:**

- A non-obvious constant.
- A workaround.
- A surprising side effect.

```python
timeout = 30  # matches the upstream API's documented limit
```

**When not to use:**

- To explain every line.
- To restate the code.
- To hold long explanations (use a block comment above the code).

### 2.9 Block Comments

**Rule:** Use block comments above the code they describe. Indent them to match the code.

```python
def retry_request(request: Request) -> Response:
    # The upstream service returns 503 during its nightly maintenance
    # window (02:00–02:15 UTC). We retry with exponential backoff rather
    # than failing the user's request.
    for attempt in range(MAX_RETRIES):
        ...
```

### 2.10 When to Use Docstrings Instead of Comments

**Rule:** If the information describes *what a function/class/module does*, use a docstring. If it describes *why a specific line exists*, use a comment.

| Use a docstring for | Use a comment for |
|---|---|
| Purpose of a function | Why a specific line is there |
| Parameters and return values | Non-obvious constants |
| Raised exceptions | Workarounds |
| Usage examples | Invariants and warnings |

---

## 3. Good vs Bad Comments

Each example shows a bad comment, an improved comment, and a professional version — with the reasoning.

### Example 1 — Restating the code

**Bad:**

```python
# Increment the retry counter
retry_count += 1
```

**Improved:**

```python
# Track retries so we can back off after the third failure.
retry_count += 1
```

**Professional:**

```python
# Back off after the third failure; the upstream service rate-limits
# aggressively and further retries make the outage worse.
retry_count += 1
```

**Why the professional version is better:** It explains the *reason* for the counter and the threshold, which is the information a future maintainer actually needs.

---

### Example 2 — Compensating for a bad name

**Bad:**

```python
# Number of seconds in a day
d = 86400
```

**Improved:**

```python
SECONDS_PER_DAY = 86400
```

**Professional:**

```python
SECONDS_PER_DAY = 24 * 60 * 60  # readable and self-checking
```

**Why the professional version is better:** The name replaces the comment, and the arithmetic makes the value auditable at a glance.

---

### Example 3 — A misleading comment

**Bad:**

```python
# Returns the user's full name.
def display_name(user: User) -> str:
    return user.email.split("@")[0]
```

**Improved:**

```python
def display_name(user: User) -> str:
    return user.email.split("@")[0]
```

**Professional:**

```python
def email_local_part(user: User) -> str:
    """Return the local part of the user's email (before the '@')."""
    return user.email.split("@")[0]
```

**Why the professional version is better:** The bad comment claimed something the code does not do. Renaming the function removes the need for a misleading comment and makes the behaviour obvious.

---

### Example 4 — A long comment that hides the point

**Bad:**

```python
# This block iterates over the orders and checks whether each order
# has been paid, and if it has not been paid and the order is older
# than 30 days, it marks the order as expired and sends a notification
# to the customer, otherwise it skips the order and continues.
for order in orders:
    if not order.paid and order.age_days > 30:
        order.expire()
        notify(order.customer)
```

**Improved:**

```python
# Expire unpaid orders older than 30 days and notify the customer.
for order in orders:
    if not order.paid and order.age_days > 30:
        order.expire()
        notify(order.customer)
```

**Professional:**

```python
UNPAID_EXPIRY_DAYS = 30

def expire_stale_unpaid_orders(orders: list[Order]) -> None:
    """Expire unpaid orders older than UNPAID_EXPIRY_DAYS and notify customers."""
    for order in orders:
        if not order.paid and order.age_days > UNPAID_EXPIRY_DAYS:
            order.expire()
            notify(order.customer)
```

**Why the professional version is better:** The intent is now in the function name, the threshold is a named constant, and the docstring describes the contract. The inline comment is no longer needed.

---

### Example 5 — A workaround comment

**Bad:**

```python
time.sleep(0.1)
```

**Improved:**

```python
# Sleep briefly to let the file system catch up.
time.sleep(0.1)
```

**Professional:**

```python
# Some network file systems (notably NFS) return stale directory listings
# immediately after a write. A short sleep avoids a race condition that
# causes intermittent "file not found" errors in CI. See issue #4821.
time.sleep(0.1)
```

**Why the professional version is better:** It documents the constraint, the consequence, and a reference. A future maintainer can decide whether the workaround is still needed.

---

## 4. Docstrings

### 4.1 What a Docstring Is

A docstring is a string literal that appears as the first statement in a module, function, class, or method. It becomes the object's `__doc__` attribute and is used by `help()`, IDEs, and documentation generators.

```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b
```

### 4.2 When to Use One

**Rule (PEP 257):** Write a docstring for every public module, function, class, and method. Private helpers may skip one if the name and signature are self-explanatory.

### 4.3 Function, Class, and Module Docstrings

**Function docstring** — describes purpose, parameters, return value, and exceptions.

**Class docstring** — describes the class's responsibility and public attributes.

**Module docstring** — describes the module's purpose and contents.

### 4.4 What a Good Docstring Contains

- A one-line summary ending with a period.
- A blank line, then a longer description if needed.
- `Args:` / `Parameters:` section.
- `Returns:` section.
- `Raises:` section.
- `Example:` section for non-obvious usage.

### 4.5 Professional Docstring Examples

**Google style (widely used, readable):**

```python
def calculate_invoice_total(
    line_items: list[LineItem],
    tax_rate: float,
    discount: float = 0.0,
) -> float:
    """Calculate the total for an invoice.

    Args:
        line_items: The items on the invoice. Must not be empty.
        tax_rate: Tax rate as a decimal (e.g., 0.08 for 8%).
        discount: Discount as a decimal, applied before tax.

    Returns:
        The total amount in the invoice's currency, rounded to two decimals.

    Raises:
        ValueError: If line_items is empty or tax_rate is negative.

    Example:
        >>> calculate_invoice_total([LineItem(price=10, qty=2)], tax_rate=0.08)
        21.6
    """
```

**NumPy style (common in scientific Python):**

```python
def calculate_invoice_total(line_items, tax_rate, discount=0.0):
    """
    Calculate the total for an invoice.

    Parameters
    ----------
    line_items : list[LineItem]
        The items on the invoice. Must not be empty.
    tax_rate : float
        Tax rate as a decimal (e.g., 0.08 for 8%).
    discount : float, optional
        Discount as a decimal, applied before tax. Default is 0.0.

    Returns
    -------
    float
        The total amount in the invoice's currency.

    Raises
    ------
    ValueError
        If line_items is empty or tax_rate is negative.
    """
```

**Class docstring:**

```python
class InvoiceRepository:
    """Persistence layer for invoices.

    Wraps the database and exposes invoice-specific queries. All methods
    are synchronous and assume a single-threaded caller.

    Attributes:
        session: The SQLAlchemy session used for all queries.
    """

    def __init__(self, session: Session) -> None:
        self.session = session
```

**Module docstring:**

```python
"""Billing services.

This module contains the business logic for creating, calculating, and
finalising invoices. It depends on `myapp.models` and `myapp.db` but
must not import from `myapp.api` (that would create a cycle).
"""
```

**Professional takeaway:** Pick one docstring style and use it everywhere. Google style is the most common in application code; NumPy style is common in data/science libraries. Consistency matters more than the choice.

---

## 5. Writing Self-Documenting Code

The best comment is the one you did not have to write because the code explains itself.

### 5.1 Naming Does the Work

**Rule:** Choose names that describe intent, not implementation.

**Bad:**

```python
# Check if the user can access the report
if u.r == "admin" or u.r == "manager":
    ...
```

**Good:**

```python
def can_access_report(user: User) -> bool:
    return user.role in {"admin", "manager"}

if can_access_report(user):
    ...
```

### 5.2 Simple Code Needs Fewer Comments

**Rule:** Replace nested conditionals and clever one-liners with named intermediate values.

**Bad:**

```python
# Only process orders that are paid, not refunded, and older than 30 days
if o.p and not o.r and (now - o.c).days > 30:
    ...
```

**Good:**

```python
is_paid = order.paid
is_refunded = order.refunded
is_older_than_30_days = (now - order.created_at).days > 30

if is_paid and not is_refunded and is_older_than_30_days:
    ...
```

**Professional takeaway:** A well-named variable is a comment that cannot go stale.

### 5.3 Refactoring Example

**Before (needs comments to be understood):**

```python
def p(u):
    # Check if user is active and has a verified email
    if u.s == 1 and u.ev == True:
        # Send the welcome email
        send(u.em, "Welcome")
        # Update the last login time
        u.ll = now()
        return True
    return False
```

**After (no comments needed):**

```python
def send_welcome_email_if_eligible(user: User) -> bool:
    """Send a welcome email to active users with verified emails.

    Returns True if the email was sent, False otherwise.
    """
    if not user.is_active or not user.email_verified:
        return False

    send_email(user.email, subject="Welcome")
    user.last_login_at = now()
    return True
```

**Professional takeaway:** Renaming and extracting removed every comment except the docstring — and the docstring now describes the *contract*, not the implementation.

---

## 6. Professional Code Review Rules

Use this as a mental checklist before submitting a PR. The full checklist is at the end.

1. **Read your own diff first.** You will catch half the issues before anyone else sees them.
2. **Keep PRs small.** A 200-line PR gets a real review; a 2,000-line PR gets a rubber stamp.
3. **One concern per PR.** Do not mix a refactor with a feature.
4. **Run the formatter and linter locally.** Do not make reviewers comment on whitespace.
5. **Write a meaningful PR description.** Explain *what* changed and *why*.
6. **Add or update tests.** A behaviour change without a test is a regression waiting to happen.
7. **Update docstrings and comments** affected by the change.
8. **Check for secrets.** No API keys, tokens, or credentials in the diff.
9. **Consider the reader.** If a reviewer has to ask "why?", the code or the PR description is not clear enough.
10. **Respond to review comments with changes, not defensiveness.** The goal is a better codebase, not a winning argument.

---

## 7. Common Mistakes

### 7.1 Too Many Comments

Comments add maintenance cost. A file where every line has a comment is harder to read, not easier.

**Fix:** Delete comments that restate the code. Keep only the ones that add information.

### 7.2 Obvious Comments

```python
# Bad
x = x + 1  # add one to x
```

**Fix:** Remove it. If you feel the need to explain `x = x + 1`, rename `x`.

### 7.3 Commenting Out Unused Code

```python
# Bad
# def old_calculate_total():
#     ...
```

**Fix:** Delete it. Git remembers. Commented-out code confuses readers, rots, and is never restored correctly.

### 7.4 Long Comments

A ten-line comment above a three-line block usually means the block should be a function with a docstring.

**Fix:** Extract a function. Let the docstring carry the explanation.

### 7.5 Outdated Comments

```python
# Bad — the code now caches for 10 minutes, not 60 seconds
# Cache for 60 seconds
CACHE_TTL_SECONDS = 600
```

**Fix:** Update the comment in the same commit as the code change, or replace it with a name that cannot drift.

### 7.6 Using Comments Instead of Better Names

```python
# Bad
# total price including tax
t = p * (1 + r)
```

**Fix:**

```python
total_price_with_tax = price * (1 + tax_rate)
```

### 7.7 Describing Implementation Instead of Intent

```python
# Bad — describes the loop, not the goal
# Loop over users and check the flag
for user in users:
    if user.flag:
        ...
```

**Fix:**

```python
# Only notify users who opted in to product updates.
for user in users:
    if user.opted_in_to_updates:
        ...
```

### 7.8 Using Comments to Justify Bad Code

```python
# Bad — the comment is an excuse, not an explanation
# I know this is O(n²) but I don't have time to fix it
```

**Fix:** Either fix it, or write a TODO with an owner and a ticket: `# TODO(alice): replace with indexed lookup — see JIRA-1234`.

---

## 8. Real-World Examples

### 8.1 A Retry Decorator

```python
import functools
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry(
    max_attempts: int = 3,
    backoff_seconds: float = 0.5,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Retry a function with exponential backoff.

    Args:
        max_attempts: Total number of attempts, including the first.
        backoff_seconds: Base delay between attempts. Doubles each retry.
        exceptions: Exception types that trigger a retry.

    Returns:
        A decorator that wraps the target function.

    Raises:
        The last exception raised by the wrapped function if all attempts fail.
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> T:
            delay = backoff_seconds
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == max_attempts:
                        raise
                    # Exponential backoff: 0.5s, 1s, 2s, ...
                    time.sleep(delay)
                    delay *= 2
            raise RuntimeError("unreachable")
        return wrapper
    return decorator
```

**What is good here:** The docstring describes the contract. The inline comment explains the *why* of the backoff. The names (`max_attempts`, `backoff_seconds`) make the call site readable.

---

### 8.2 A Payment Service

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PaymentResult:
    """Outcome of a payment attempt.

    Attributes:
        success: True if the payment was captured.
        transaction_id: The processor's transaction ID, or None on failure.
        error: Human-readable error message, or None on success.
    """
    success: bool
    transaction_id: str | None
    error: str | None


class PaymentService:
    """Coordinates payments with the external processor.

    This service is intentionally stateless. Idempotency is the caller's
    responsibility: the same `idempotency_key` must be reused across retries
    to avoid duplicate charges.
    """

    def __init__(self, client: PaymentClient, max_retries: int = 3) -> None:
        self._client = client
        self._max_retries = max_retries

    def charge(
        self,
        amount: Decimal,
        currency: str,
        idempotency_key: str,
    ) -> PaymentResult:
        """Charge the customer.

        Args:
            amount: Amount to charge. Must be positive.
            currency: ISO 4217 currency code (e.g., "USD").
            idempotency_key: Stable key reused across retries.

        Returns:
            A PaymentResult describing the outcome.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError(f"amount must be positive, got {amount}")

        # The processor requires the idempotency key to be sent on every
        # attempt; generating a new one on retry would cause duplicate charges.
        for attempt in range(1, self._max_retries + 1):
            response = self._client.charge(
                amount=amount,
                currency=currency,
                idempotency_key=idempotency_key,
            )
            if response.ok:
                return PaymentResult(True, response.transaction_id, None)
            if not response.retryable or attempt == self._max_retries:
                return PaymentResult(False, None, response.error)

        return PaymentResult(False, None, "retries exhausted")
```

**What is good here:** The class docstring states the idempotency contract. The inline comment explains a subtle, non-obvious requirement. Type hints and `Decimal` make the interface unambiguous.

---

### 8.3 A Data Pipeline Function

```python
from datetime import datetime, timedelta
from typing import Iterable

STALE_THRESHOLD = timedelta(days=7)


def find_stale_records(
    records: Iterable[Record],
    now: datetime,
    threshold: timedelta = STALE_THRESHOLD,
) -> list[Record]:
    """Return records that have not been updated within `threshold`.

    Args:
        records: The records to inspect.
        now: The reference time. Injected so the function is testable.
        threshold: Maximum allowed age. Defaults to 7 days.

    Returns:
        A list of stale records, in the original order.
    """
    # `now` is injected rather than read from the clock so tests can
    # simulate time without monkey-patching datetime.
    cutoff = now - threshold
    return [r for r in records if r.updated_at < cutoff]
```

**What is good here:** The comment explains the *design decision* (dependency injection for testability), not the code. Without it, a future maintainer might "simplify" by reading the clock inside the function — and break every test.

---

### 8.4 A Configuration Loader

```python
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Application settings loaded from the environment.

    Raises:
        KeyError: If a required environment variable is missing.
    """
    database_url: str
    api_key: str
    debug: bool = False

    @classmethod
    def from_env(cls) -> "Settings":
        """Load settings from environment variables.

        Required: DATABASE_URL, API_KEY. Optional: DEBUG (default "false").
        """
        return cls(
            database_url=os.environ["DATABASE_URL"],
            api_key=os.environ["API_KEY"],
            # Only the literal string "true" enables debug mode; this avoids
            # accidental truthiness from values like "0" or "false".
            debug=os.environ.get("DEBUG", "false").lower() == "true",
        )
```

**What is good here:** The inline comment prevents a future "fix" that would introduce a subtle bug. It explains a *why* that is invisible in the code.

---

## Professional Python Commenting Rules — Quick Reference

1. **Comment the *why*, not the *what*.** The code already says what it does.
2. **Prefer a better name over a comment.** `SECONDS_PER_DAY` beats `# 86400 seconds`.
3. **Delete commented-out code.** Git remembers; readers should not have to.
4. **Do not restate the code.** `i += 1  # increment i` adds nothing.
5. **Keep comments short.** If it needs a paragraph, extract a function with a docstring.
6. **Update comments with the code.** A stale comment is worse than no comment.
7. **Use docstrings for contracts, comments for reasons.** Public APIs get docstrings.
8. **Document workarounds and invariants.** These are the highest-value comments.
9. **Reference issues and tickets.** `# See JIRA-1234` gives future readers a trail.
10. **Avoid TODOs without owners.** `# TODO(alice): ...` is actionable; `# TODO: fix` is noise.
11. **Do not use comments to excuse bad code.** Fix it or file a ticket.
12. **Inline comments are for short clarifications.** Long explanations go above the block.
13. **Match the comment's indentation to the code.** Misindented comments are confusing.
14. **Write comments for the next reader, not for yourself.** You will forget the context.
15. **When in doubt, delete the comment and improve the code.** The best comment is often no comment.

---

## Code Review Checklist

Use this before requesting review. It is grouped by concern.

### Formatting
- [ ] Code is formatted with the project's formatter (`black`, `ruff format`).
- [ ] Line length matches the project's configured limit.
- [ ] No trailing whitespace, no mixed tabs/spaces.
- [ ] Blank lines separate logical blocks (2 around top-level defs, 1 between methods).

### Naming
- [ ] Functions and variables use `snake_case`.
- [ ] Classes use `PascalCase`.
- [ ] Constants use `UPPER_SNAKE_CASE`.
- [ ] Names describe intent, not implementation.
- [ ] No single-letter names outside of short loops or math.

### Comments
- [ ] Comments explain *why*, not *what*.
- [ ] No commented-out code.
- [ ] No obvious or restating comments.
- [ ] No stale comments contradicting the code.
- [ ] Workarounds and invariants are documented.

### Docstrings
- [ ] Public modules, classes, and functions have docstrings.
- [ ] Docstrings describe purpose, args, returns, and raises.
- [ ] Docstring style is consistent across the project.
- [ ] Examples in docstrings are correct and runnable.

### Readability
- [ ] Functions do one thing and are short enough to read.
- [ ] Nesting is shallow; early returns are used where appropriate.
- [ ] Complex expressions are broken into named intermediates.
- [ ] No clever one-liners that require explanation.

### Maintainability
- [ ] No duplicated logic that should be extracted.
- [ ] Magic numbers and strings are named constants.
- [ ] Dependencies are injected where it improves testability.
- [ ] Public interfaces are stable and documented.

### Error Handling
- [ ] Exceptions are specific, not bare `except:`.
- [ ] Errors are logged with enough context to debug.
- [ ] Resources are cleaned up (`with`, `try/finally`).
- [ ] Failure modes are documented in the docstring.

### Type Hints
- [ ] Public functions and methods have type hints.
- [ ] `Optional` / `| None` is used correctly.
- [ ] `mypy` or `pyright` passes with the project's configuration.
- [ ] Type hints match the docstring's description.

### Imports
- [ ] Imports are grouped: stdlib, third-party, local.
- [ ] No wildcard imports (`from module import *`).
- [ ] No unused imports.
- [ ] Import order matches the project's `isort` / `ruff` configuration.

---

## Golden Rule

> **"Good code explains what it is doing; good comments explain why it is doing it."**

Code is a description of behaviour. A reader can see *what* happens by reading the code — that is what code is for. What the code cannot tell you is **why** it was written that way: the business rule, the constraint, the workaround, the trade-off, the incident that motivated it.

That is the job of a comment.

When you are about to write a comment, ask:

1. **Can the code say this instead?** If a better name, a named constant, or an extracted function would carry the meaning, do that. Code that cannot go stale is better than a comment that can.
2. **Is this a *why* or a *what*?** If it is a *what*, delete it. If it is a *why*, keep it — but keep it short.
3. **Will this still be true after the next change?** If not, either make it impossible to drift (a name, a constant) or commit to maintaining it.

The goal is not "more comments" or "fewer comments". The goal is **code that a stranger can safely change**. Every naming decision, every docstring, every comment is measured against that standard.

Write code for the person who will read it at 2 a.m. during an incident. That person is usually you.
