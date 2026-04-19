# Stacks

A stack is a **Last In, First Out (LIFO)** data structure. The last thing you push on is the first thing you pop off — like a stack of plates.

In Python, a regular list works as a stack:
- `stack.append(x)` — push (add to top)
- `stack.pop()` — pop (remove from top)
- `stack[-1]` — peek (look at top without removing)

Use a stack when the problem involves **matching**, **nesting**, or **undoing** — anywhere the most recent thing matters most.

---

## When to reach for a stack

- **Parentheses / bracket problems** — you need to match an open bracket to its corresponding close bracket. The key is that the *most recently opened* bracket must be closed first. Two pointers fail here because brackets can be sequential, not just nested (e.g. `"()[]{}"` is valid but `l` and `r` point to non-matching chars).

- **Nested problems (e.g. Basic Calculator)** — when you hit an inner expression, you need to pause the outer one, solve the inner one, then resume. A stack lets you save the outer context and come back to it — exactly like a call stack in recursion.

- **Order of operations / manual evaluation** — when operators have precedence (e.g. `*` before `+`), a stack lets you defer lower-priority operations until higher-priority ones are resolved first.

- **Undo / history problems** — any time you need to reverse a sequence of actions or look at what happened before, a stack naturally stores history in reverse order. The last action is always on top.

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
