# Trees & Binary Search Trees

A **tree** is a hierarchical structure of nodes connected by parent → child edges, with one designated root and no cycles. A **binary tree** restricts each node to at most two children (`left`, `right`). A **binary search tree (BST)** adds an *ordering invariant* on top of binary trees: every node's left subtree contains only smaller values, every node's right subtree only larger values.

Trees are the data structure where **recursion stops being scary** and starts being the natural way to think. If you internalize one thing from this doc, make it that.

---

## Why trees change how you think

- **No linear order.** Unlike arrays or linked lists, there's no "next" element — each node branches. You don't iterate a tree, you *traverse* it (and there are multiple traversal orders).
- **Recursive by definition.** A binary tree is either empty (`None`) or a node with two subtrees, *which are themselves binary trees*. Your code mirrors this — base case for empty, recursive case for node-with-subtrees.
- **Pointer rewiring instead of arithmetic.** Like linked lists, mutations are about reassigning `.left` and `.right`. No indices, no shifting.
- **Depth matters more than size.** Many tree algorithms are `O(h)` where h = height. Balanced → `O(log n)`. Skewed → `O(n)`. The difference between "fast" and "linked list with extra steps" is balance.

---

## The recursion mindset (the most important section)

Every tree problem you'll see follows this template:

```python
def solve(node):
    # 1. Base case — what happens when node is None?
    if not node:
        return <something_neutral>

    # 2. Recurse on children — TRUST that they return correct answers
    left_result  = solve(node.left)
    right_result = solve(node.right)

    # 3. Combine — what does THIS node contribute, given its children's results?
    return <combine(node, left_result, right_result)>
```

Three lines of mental work per problem:

| Step | Question to ask yourself |
|------|--------------------------|
| Base case | What's the right answer for an empty subtree? |
| Recurse | What do I need from each child? |
| Combine | Given my children's answers, what's MY answer? |

**The "trust" part is everything.** When you write `solve(node.left)`, *do not trace into the call mentally*. Just assume it returns the right answer. Your job is only to handle this one node correctly, given that assumption. The recursion handles the rest by induction.

> **Why this works.** If your function is correct for an empty tree (base case) AND correct for any node assuming it's correct on smaller subtrees (inductive step), then it's correct for *every* tree. This is mathematical induction in code form.

---

## The recursion playbook — what to do when you sit down with a new problem

Tracing recursion mentally is a trap. Instead, run this 4-step workflow every single time. You'll never feel "lost" if you follow it.

### Step 1 — State the contract (out loud or in a comment)

> "Given [input], this function returns [output meaning]."

For maxDepth: "Given a tree, this function returns the number of nodes on the longest path from root to leaf."

For isSameTree: "Given two trees p and q, this function returns True if they're identical, False otherwise."

The contract is a **promise** the function makes. Every recursive call obeys the same promise — including calls on subtrees.

### Step 2 — Identify the trivial / base case(s)

Two heuristics for finding base cases:

**Heuristic A — "Trivial answer."**
What's the smallest input where you can answer immediately without any work?
- Empty tree depth = 0
- Two empty trees same? → True
- Empty tree symmetric? → True

**Heuristic B — "What would crash on the next line?"**
Look at the body of your function. Every `node.val`, `node.left`, etc. assumes `node` exists. Each potential `NoneType has no attribute ...` crash needs a base case to guard it.

For two-tree problems (isSameTree, isSymmetric): typically 3 base cases —
1. Both None → trivially same
2. Exactly one None → can't be same (and would crash on `.val`)
3. Both exist but values differ → not same (no need to recurse)

### Step 3 — Write the recursive case as a *definition*

**The single biggest mindset shift:** stop reading recursive code as instructions. Read it as a **definition**.

Instead of:
> "First do this, then call myself, then..."

Read:
> "The depth of a tree IS DEFINED AS 1 plus the max of its subtrees' depths."

That's a *definition*, not a procedure. Same as `f(x) = x²` — you don't trace it, you state the relationship. Recursion is identical.

The recursive case writes itself once you ask: **"Given my children's answers (which I trust), what's my answer?"**

### Step 4 — Type it. Don't trace. Submit.

Once Steps 1–3 are correct, the function is correct on **every** input. By induction. You don't need to trace it, you don't need to mentally run the call stack — the math has already proven it works.

If you get nervous and want to check, ask only **two questions:**

1. Is the function correct for the BASE case? (Empty tree → 0. Yes ✓)
2. Is the function correct for ONE node, ASSUMING the recursive calls return correct answers? (At node 1: if maxDepth(node2) returns the right number and maxDepth(node3) returns the right number, does my code give the right answer for node 1? Yes ✓)

If both are yes — submit. The math handles the rest.

> **The replacement for "let me trace it":**
> ❌ Bad question: "What does the call stack look like step by step?"
> ✅ Good question: "Assuming the recursive call returns the correct answer for the smaller subtree, does my code produce the correct answer for THIS node?"

---

## Decision: do I `return` the recursive call?

A common confusion. The rule:

**Return / capture the recursive call when** your function's answer DEPENDS on what the recursive call gives back.
```python
return 1 + max(self.maxDepth(left), self.maxDepth(right))   # need depths to compute
return same(p.left, q.left) and same(p.right, q.right)      # need bools to AND
```

**Don't capture the recursive call when** the recursion is just doing side-effect work (mutation) and you don't need its return value.
```python
self.invertTree(root.left)    # mutates in place, no return needed
self.invertTree(root.right)
return root
```

**Quick test:** ask "do I need INFORMATION from this recursive call to compute MY answer?"
- Yes → return / capture it
- No (it's just doing work elsewhere) → call it bare

90% of tree problems return the call. Mutation problems (invert-tree style) are the exception.

---

## Practical drill habits (recursion clicks through reps, not understanding)

- **Solve the SAME problem 3 times, days apart.** Re-do maxDepth tomorrow with a blank file. Then again the day after. Spaced repetition > new problems for cementing the template.
- **Practice 1D recursion first if trees feel hard.** `factorial(n)`, `sum_list(arr)`, `reverse_str(s)`. Same mental model, half the complexity (one recursive call per frame instead of two).
- **Read recursive code aloud, in plain English.** "If the tree is empty, return 0. Otherwise, return 1 plus the bigger of the depths of the left and right subtrees." That sentence is the function. Trust it like you'd trust the sentence.
- **Use the template religiously.** Every tree problem is `base case + trust recursion + combine`. You don't have to invent recursion each time.
- **When stuck, draw it on paper.** Boxes for each call, arrows for calls and returns. Once is enough — physical drawing forces slow thinking that screen-staring doesn't.

---

## Three DFS traversal orders (memorize)

DFS = "go deep first." The three orders differ only in *when you visit the current node* relative to its children.

```python
def preorder(node):     # node → left → right
    if not node: return
    visit(node)
    preorder(node.left)
    preorder(node.right)

def inorder(node):      # left → node → right
    if not node: return
    inorder(node.left)
    visit(node)
    inorder(node.right)

def postorder(node):    # left → right → node
    if not node: return
    postorder(node.left)
    postorder(node.right)
    visit(node)
```

**When to use each:**
- **Pre-order** — when you need to process a node *before* its children. E.g., copying/serializing a tree, building from a description.
- **In-order** — **for BSTs, in-order traversal yields values in sorted order.** Massive. Use this for "kth smallest," "validate BST," "convert to sorted array."
- **Post-order** — when you need children's results to compute the node's value. E.g., "size of subtree," "max path sum," "diameter."

**Mnemonic:** the prefix tells you where the node visit happens — *pre*-order = visit node before recursion, *post*-order = visit node after recursion.

---

## BFS / level-order traversal

DFS uses the call stack. BFS uses an explicit queue and processes nodes level by level.

```python
from collections import deque

def level_order(root):
    if not root: return []
    q = deque([root])
    while q:
        next_level = []                 # buffer-swap pattern (see linked_list / merge-k-lists)
        for _ in range(len(q)):         # process exactly one level
            node = q.popleft()
            next_level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        # do something with next_level (or yield it as the level's result)
```

**When to use BFS over DFS:**
- "Level-order" or "by-level" anywhere in the problem (level sums, right-side view, zigzag).
- Shortest path / minimum depth — BFS finds shortest first.
- When the tree is so deep (skewed) that recursion would hit Python's stack limit.

---

## What makes a BST a BST

The BST invariant: **for every node `n`, all values in the left subtree < `n.val` < all values in the right subtree.** Strict on both sides (no duplicates by default — problems vary).

This *one rule* gives you `O(log n)` average lookup, insertion, and deletion — assuming the tree stays balanced. Without balance, the BST degenerates into a linked list and operations become `O(n)`.

```python
def search(node, target):
    if not node: return None
    if node.val == target: return node
    if target < node.val:  return search(node.left,  target)   # half the tree disappears
    else:                  return search(node.right, target)
```

That `target < node.val` decision throws away an entire subtree at every step — that's the source of the `O(log n)`.

**Three properties of BSTs you'll exploit constantly:**

1. **In-order traversal = sorted ascending.** This is *the* go-to trick for BST problems. Kth smallest? In-order, take the kth value. Validate BST? In-order should be strictly increasing. Convert to sorted list? In-order, append to list.

2. **Searching is binary search on a tree.** Compare to root, recurse into one side. Same `O(log h)` mental model as binary search on an array.

3. **Range pruning.** When recursing, you can pass *bounds* `(low, high)` representing valid value ranges for that subtree. Lets you validate or filter without traversing irrelevant branches.

> **Balanced ≠ guaranteed.** Plain BSTs aren't self-balancing. AVL trees and red-black trees add rotations to maintain `O(log n)` height. For interviews, you usually don't implement balancing yourself — you assume input is reasonable, OR you use Python's `sortedcontainers.SortedList` if you actually need a balanced BST in practice.

---

## The problem types you'll encounter

Every tree problem on LeetCode falls into one of these buckets. Knowing the bucket tells you the template.

### 1. Traversal / collection
*"Return all values in [some] order."*

Templates: pre/in/post-order DFS, or BFS for level-order. Just walk and append.

Examples: 94 In-order Traversal, 102 Level Order, 199 Right Side View, 144 Pre-order.

### 2. Single-value summary (post-order aggregation)
*"Compute one number/bool that depends on the whole tree."*

Template: post-order. Recurse on both children, combine their results, return.

```python
def solve(node):
    if not node: return BASE_VALUE
    left  = solve(node.left)
    right = solve(node.right)
    return combine(node, left, right)
```

Examples: 104 Max Depth (`return 1 + max(left, right)`), 110 Balanced Tree, 111 Min Depth, 222 Count Nodes, 226 Invert Tree (mutates in place).

### 3. Path problems (carry state down)
*"Find a property along a root-to-leaf or root-to-node path."*

Template: pass accumulators *down* via parameters; check the property at leaves. Or carry an explicit list and pop on the way back up (backtracking).

Examples: 112 Path Sum, 113 Path Sum II, 257 All Root-to-Leaf Paths, 129 Sum Root to Leaf Numbers.

### 4. "Best path" problems (combine subtree results in tricky ways)
*"Maximum/minimum over any path in the tree."*

Template: post-order, BUT the recursive function returns a "path-extending" value while a separate variable tracks the global best.

```python
self.best = float('-inf')
def dfs(node):
    if not node: return 0
    l = max(0, dfs(node.left))   # ignore negative-contribution branches
    r = max(0, dfs(node.right))
    self.best = max(self.best, node.val + l + r)   # path through THIS node
    return node.val + max(l, r)                    # path EXTENDING upward (only one side)
dfs(root)
return self.best
```

Examples: 124 Binary Tree Maximum Path Sum, 543 Diameter of Binary Tree, 687 Longest Univalue Path.

> **Why two values?** The path *through* this node uses both subtrees; the path *continuing through* this node to a parent can only use one. Different return shape from "best so far."

### 5. BST validation / property checks
*"Is this a valid BST?" "Find kth smallest." "Closest value."*

Two main tools:
- **In-order traversal** (sorted property)
- **Range-based recursion** with `(lo, hi)` bounds

```python
def is_valid_bst(node, lo=float('-inf'), hi=float('inf')):
    if not node: return True
    if not (lo < node.val < hi): return False
    return is_valid_bst(node.left,  lo, node.val) \
       and is_valid_bst(node.right, node.val, hi)
```

Examples: 98 Validate BST, 230 Kth Smallest, 270 Closest Value, 235 LCA of BST.

### 6. Lowest Common Ancestor (LCA)
*"Find the lowest node that has both targets in its subtree."*

For BST: just walk down comparing values — first node where targets split is the LCA.

For general binary tree: post-order, return whichever target you found in each subtree; the first node where both come back is the LCA.

```python
# General binary tree
def lca(node, p, q):
    if not node or node == p or node == q: return node
    l = lca(node.left,  p, q)
    r = lca(node.right, p, q)
    if l and r: return node      # split point — this is the LCA
    return l or r                # both came from one side
```

Examples: 235 LCA of BST, 236 LCA of Binary Tree.

### 7. Construction problems
*"Build a tree from [traversal arrays / serialized string]."*

Template: pre-order or in-order recursion that consumes the input as it goes. Often uses a hashmap for `O(1)` lookups in `inorder` to find the split point.

Examples: 105 Build from Preorder + Inorder, 106 Build from Inorder + Postorder, 297 Serialize/Deserialize.

### 8. Two-tree comparison
*"Are these trees the same? Is one a subtree of the other? Mirror?"*

Template: recurse on both trees in lockstep.

```python
def same(a, b):
    if not a and not b: return True
    if not a or not b:  return False
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
```

Examples: 100 Same Tree, 101 Symmetric Tree, 226 Invert (mirror of self).

> **Symmetric tree twist:** mirror-checking recurses **diagonally** instead of straight-down — `helper(left.left, right.right)` and `helper(left.right, right.left)`. The criss-cross is what makes it "mirror" instead of "same."

### 9. Search-then-match (two-layer recursion)
*"Does X appear anywhere in this tree?" "How many subtrees satisfy property P?"*

Two recursive functions working together:
- **Outer** — walks every node in the big tree (DFS).
- **Inner** — at each node, checks "does the subtree starting here satisfy the property?"

The outer function calls the inner as a *helper* at each node. This is the first time you'll see two recursions in the same problem, and it can feel disorienting — but the pattern is just **"search using recursion #1, ask a yes/no question using recursion #2."**

```python
def isSubtree(root, subRoot):
    if not root: return False                              # outer: ran out of tree to search
    if isSameTree(root, subRoot): return True              # inner: hit at this node?
    return isSubtree(root.left, subRoot) \
        or isSubtree(root.right, subRoot)                  # outer: keep searching elsewhere

def isSameTree(p, q):
    # standard pattern from section 8
    ...
```

**Mental model:** "find a needle in a haystack."
- Outer recursion = flipping through every page of the book.
- Inner recursion (the helper) = comparing a page to the paragraph.
- You find a hit if the inner returns True at *any* page.

**Complexity flavor:** outer visits `m` nodes, inner walks up to `n` nodes per call → `O(m * n)` time. Two recursion stacks → `O(m + n)` space worst-case.

Examples: 572 Subtree of Another Tree, 250 Count Univalue Subtrees, 663 Equal Tree Partition.

> **Why this pattern needs TWO functions:** the outer's job is *"search every starting point"* — it needs to recurse on `root.left` and `root.right`. The inner's job is *"compare two trees from a fixed pair of starting points"* — it needs to recurse on `(p.left, q.left)` and `(p.right, q.right)`. Different questions, different recursion shapes, can't fit in one function. You need a tool (helper) and a worker (outer) that uses the tool.

---

## Recursion patterns: how to carry state

Most pitfalls in tree problems come from "where do I store the result?" Three options:

### A. Return values up
Cleanest. Each call returns what its parent needs. Use this when the answer naturally bubbles up.
```python
def depth(node):
    if not node: return 0
    return 1 + max(depth(node.left), depth(node.right))
```

### B. Pass state down via parameters
For path/range problems where the *context from above* matters at each node.
```python
def has_path_sum(node, remaining):
    if not node: return False
    if not node.left and not node.right: return remaining == node.val
    return has_path_sum(node.left,  remaining - node.val) \
        or has_path_sum(node.right, remaining - node.val)
```

### C. Carry global state via `self.x` or `nonlocal x`
For "best so far" problems where the answer doesn't fit cleanly in a single return value.
```python
def diameter(self, root):
    self.best = 0
    def dfs(node):
        if not node: return 0
        l, r = dfs(node.left), dfs(node.right)
        self.best = max(self.best, l + r)   # diameter THROUGH this node
        return 1 + max(l, r)                # depth FROM this node
    dfs(root)
    return self.best
```

> **Rule of thumb:** if the function's return value answers the problem at every subtree, use (A). If you need parent context, use (B). If the recursive return shape differs from the answer shape (e.g., return depth but track diameter), use (C).

---

## Common pitfalls

- **Forgetting the `None` base case.** Then you `NoneType has no attribute 'left'` your way to a crash.
- **Returning the wrong base value.** Empty tree depth = 0, not 1. Empty path sum = 0, not None. Empty subtree size = 0.
- **Mutating when you should rebuild (or vice versa).** Some problems require a *new* tree (e.g., "construct a balanced BST"); others mutate in place (e.g., invert). Read the problem.
- **Ignoring the BST invariant when given a BST.** If the problem gives you a BST and you do generic tree DFS, you're probably doing `O(n)` instead of `O(log n)`. Always ask: "can I use the BST property here?"
- **Using `<=` instead of `<` for BST validation.** Standard BST has strict inequalities — duplicates aren't allowed. (Check the problem; some allow them on the right.)
- **Stack overflow on skewed trees.** A worst-case skewed tree of 10⁴ nodes will blow Python's default recursion limit (1000). For deep trees, switch to iterative BFS or `sys.setrecursionlimit`.

---

## Complexity cheatsheet

| Operation             | Balanced BST | Worst-case (skewed) | General Binary Tree |
|-----------------------|--------------|---------------------|---------------------|
| Search                | O(log n)     | O(n)                | O(n)                |
| Insert / Delete       | O(log n)     | O(n)                | n/a                 |
| Traversal (any order) | O(n)         | O(n)                | O(n)                |
| Height                | O(log n)     | O(n)                | O(n) to compute     |
| Recursion stack       | O(log n)     | O(n)                | O(h) where h=height |

---

## Mental shortcuts for interview problems

1. **First question to ask the interviewer:** "Is this a BST or just a binary tree?" If BST, the in-order = sorted trick is on the table.
2. **"Kth smallest in BST" → in-order traversal, stop at k.** Don't sort, don't heap.
3. **"Validate BST" → range recursion** with `(-inf, inf)` initial bounds. Don't just check `node.left.val < node.val`; that fails on grandchildren.
4. **"Path sum / longest path" → think "global best + local return"** (pattern C above).
5. **"Same tree / symmetric / subtree" → lockstep recursion** on two trees.
6. **"Level order anything" → BFS with `len(q)` to bound each level**.
7. **"Build a tree from inorder + X" → use a hashmap** of `value → index in inorder` for O(1) split lookups.

---

## Problems to drill (in order)

For locking in the recursion mindset before BST-specific stuff:

1. **104 Maximum Depth of Binary Tree** — simplest post-order aggregation
2. **226 Invert Binary Tree** — mutation + recursion
3. **100 Same Tree** — lockstep recursion
4. **543 Diameter of Binary Tree** — global state + local return
5. **102 Level Order Traversal** — BFS with buffer-swap

Then BST-specific:

6. **700 Search in BST** — uses the invariant
7. **98 Validate BST** — range recursion classic
8. **230 Kth Smallest in BST** — in-order trick
9. **235 LCA of BST** — invariant-based traversal
10. **108 Sorted Array → Balanced BST** — construction with recursion
11. **236 LCA of Binary Tree** — generalize LCA without invariant
12. **124 Binary Tree Max Path Sum** — the boss-level recursion problem
