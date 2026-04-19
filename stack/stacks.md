# Stacks

A stack is a **Last In, First Out (LIFO)** data structure. The last thing you push on is the first thing you pop off — like a stack of plates.

In Python, a regular list works as a stack:
- `stack.append(x)` — push (add to top)
- `stack.pop()` — pop (remove from top)
- `stack[-1]` — peek (look at top without removing)

Use a stack when the problem involves **matching**, **nesting**, or **undoing** — anywhere the most recent thing matters most.

---

## When to reach for a stack

- Matching brackets / parentheses
- Evaluating or parsing expressions
- "Previous greater/smaller element" problems
- Undo/redo, browser back button, call stack analogies

---

## Patterns from Problems Solved

### 1. Bracket matching
**Problem:** Valid Parentheses

Push open brackets onto the stack. When you see a closing bracket, check if it matches the top of the stack. If it does, pop. If it doesn't (or the stack is empty), return false. At the end, the stack should be empty.

```
stack = []
matching = {')': '(', '}': '{', ']': '['}

for c in s:
    if c in matching:                        # closing bracket
        if not stack or stack[-1] != matching[c]:
            return False
        stack.pop()
    else:
        stack.append(c)                      # open bracket

return len(stack) == 0
```

- Time: O(n)
- Space: O(n) — worst case all open brackets
