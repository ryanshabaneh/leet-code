# Hashing, Hash Tables, and Python dict

## Terms

**Hash function**
A function that takes a key and returns an integer.

```python
hash("apple")
```

**Hash**
The integer output produced by the hash function.

**Hashing**
The process of applying the hash function to a key.

**Hash table / hash map**
A data structure that stores key-value pairs using hashing for fast average-case insert and lookup.

**Python dict**
Python's built-in hash table implementation.

---

## The goal

A normal list uses integer indexes:

```python
arr[3]
```

But a dictionary lets you do:

```python
d["apple"] = 5
```

The problem is that `"apple"` is not an array index. Hashing solves this by turning the key into a number.

---

## High-level idea

A dictionary works like this:

1. Take the key
2. Hash it into an integer
3. Convert that integer into a valid array index
4. Store the key-value pair there
5. If that spot is already occupied, handle the collision

---

## Why modulo is used

Suppose the internal table has size 8.

If:

```python
hash("apple") = 839274
```

you cannot do:

```python
table[839274]
```

because the table only has indexes 0 through 7.

So Python computes:

```python
index = hash("apple") % 8
```

This forces the result into the valid range 0 to 7.

In general:

```python
index = hash(key) % table_size
```

---

## Insert process

For:

```python
d["apple"] = 5
```

the simplified process is:

1. Compute the hash:
    ```python
    h = hash("apple")
    ```
2. Compute the starting index:
    ```python
    index = h % table_size
    ```
3. Check that slot in the internal table.
4. If the slot is empty, store the pair there:
    ```
    ("apple", 5)
    ```
5. If the slot is occupied, a collision has happened. Python then probes for another slot.

---

## Collision

A collision happens when two different keys map to the same starting index.

```python
hash("apple") % 8 = 2
hash("banana") % 8 = 2
```

This does not mean the keys are equal. It only means they want the same slot.

---

## How Python handles collisions

The important mental model for LeetCode is:

> Python dict uses **open addressing**, not "a list of lists."

That means each slot holds one entry, and if a collision happens, Python checks other slots according to a probing strategy.

Simplified example:

- `"apple"` hashes to index 2, so it goes in slot 2
- `"banana"` also hashes to index 2, but slot 2 is full
- Python checks the next slot, then the next, until it finds an empty one

So you can think of it like:

```python
table = [
    None,
    None,
    ("apple", 5),
    ("banana", 7),
    None,
    None,
    None,
    None
]
```

Even if both `"apple"` and `"banana"` originally hashed to index 2.

---

## Lookup process

For:

```python
d["banana"]
```

Python does:

1. Hash the key again:
    ```python
    h = hash("banana")
    ```
2. Compute the same starting index:
    ```python
    index = h % table_size
    ```
3. Check that slot
4. If it is not the key, Python follows the same probing path used during insertion until it finds the key

So if `"banana"` started at index 2 but was placed at index 3 after a collision, lookup still works because Python starts at 2 and probes the same way.

> Python does not need to remember where the key was moved. It recomputes the same path.

---

## Update vs collision

These are different cases.

**Collision** — different keys want the same starting index:

```python
"apple" != "banana"
# but:
hash("apple") % 8 == hash("banana") % 8
```

**Update** — same key inserted again:

```python
d["apple"] = 5
d["apple"] = 10  # not a collision — replaces the value
```

---

## Why dictionaries are fast

Without hashing, to find `"apple"` you might have to scan every stored pair:

```python
[("cat", 9), ("banana", 7), ("apple", 5)]
```

That is linear search: **O(n)**.

With hashing, Python jumps directly to a small part of the table by computing the index first.

| Operation | Average case |
|-----------|-------------|
| Insert    | O(1)        |
| Lookup    | O(1)        |
| Delete    | O(1)        |

Worst case can be O(n), but average case is O(1) because Python resizes the table and keeps it from getting too crowded.

---

## Resizing

Python grows the internal table when it gets too full:

```
size 8 → 16 → 32 → 64 → ...
```

When Python resizes, it recomputes positions using the new table size, which spreads entries out and keeps average operations fast.

---

## Important correction about "buckets"

A common teaching model shows this:

```python
table[2] = [("apple", 5), ("banana", 7)]
```

This is called **chaining**. It is useful for learning hash tables in general.

But Python's real dict does not work like that. For your LeetCode mental model, assume:

- Python dict is a hash table
- It uses hashing to get a starting index
- It uses probing to resolve collisions
- It resizes to keep average operations O(1)