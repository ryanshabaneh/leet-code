I will book a trip to iceland when I finish blind 75 + neetcode 150.
This repo is my leetcode journey

Notes I refer to (theres a notes md in each folder these are just for quicker reference)

A hash function = a machine that turns anything into a number

"apple"  →  5231
"dog"    →  9123
"car"    →  1288

What if:

"Ryan" → 7
"Bob"  → ALSO 7

Now we have:
arr[7] = ??? (conflict)
We just store BOTH:

arr[7] = [("Ryan", "123-456"), ("Bob", "555-000")]

“what is hashable?” Means: can we safely convert it to a number?
string → yes
int → yes
list → ❌ (can change, breaks system)
