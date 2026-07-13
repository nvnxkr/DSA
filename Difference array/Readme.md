# Difference Array Technique

The **Difference Array Technique** is an optimization used for performing **multiple range updates** efficiently.

Instead of updating every element in a range `[l, r]`, we update only **two positions** and reconstruct the final array using a **prefix sum**.

---
# Algorithm

1. Create a difference array initialized with zeros.
2. For every update `(l, r, val)`:
   - Add `val` at index `l`.
   - Subtract `val` at index `r + 1` (if it exists).
3. Compute the prefix sum (Cumulative sum   ) of the difference array.
4. The prefix sum array is the final updated array.

---

# Python Implementation

```python
def rangeAddition(n, updates):
    diff = [0] * n

    for l, r, val in updates:
        diff[l] += val

        if r + 1 < n:
            diff[r + 1] -= val

    arr = [0] * n
    arr[0] = diff[0]

    for i in range(1, n):
        arr[i] = arr[i - 1] + diff[i]

    return arr


n = 5

updates = [
    (1, 3, 10),
    (2, 4, 5)
]

print(rangeAddition(n, updates))
```

### Output

```
[0, 10, 15, 15, 5]
```

---

## Why Use It?

Suppose you have an array of size `N` and `Q` range update queries.

### Brute Force

For each query:

```python
for i in range(l, r + 1):
    arr[i] += val
```

- Time Complexity: **O(Q × N)** (Worst Case)

---

### Difference Array

For every update `[l, r]` with value `val`:

```python
diff[l] += val

if r + 1 < n:
    diff[r + 1] -= val
```

After processing all updates, compute the prefix sum to obtain the final array.

- Time Complexity: **O(Q + N)**

---

# Intuition

Think of it like this:

```
+val starts here
```

at index `l`.

Then,

```
-val starts here
```

at index `r + 1`.

When we compute the prefix sum, the value is added from `l` until `r` automatically.

---

# Example

### Initial Array

```
arr = [0, 0, 0, 0, 0]
```

### Updates

```
1. Add 10 to range [1,3]
2. Add 5 to range [2,4]
```

---

## Step 1: Create Difference Array

```
diff = [0, 0, 0, 0, 0]
```

---

## Update 1

```
[1,3] += 10
```

Perform:

```python
diff[1] += 10
diff[4] -= 10
```

Difference array becomes

```
[0, 10, 0, 0, -10]
```

---

## Update 2

```
[2,4] += 5
```

Perform:

```python
diff[2] += 5
```

Difference array becomes

```
[0, 10, 5, 0, -10]
```

---

## Step 2: Compute Prefix Sum

| Index | Diff | Prefix Sum |
|------:|-----:|-----------:|
| 0 | 0 | 0 |
| 1 | 10 | 10 |
| 2 | 5 | 15 |
| 3 | 0 | 15 |
| 4 | -10 | 5 |

Final Array

```
[0, 10, 15, 15, 5]
```

---

# Dry Run

```
Initial

diff = [0,0,0,0,0]

Update [1,3] += 10

diff = [0,10,0,0,-10]

Update [2,4] += 5

diff = [0,10,5,0,-10]

Prefix Sum

0
0+10 = 10
10+5 = 15
15+0 = 15
15-10 = 5

Answer

[0,10,15,15,5]
```

---



# Complexity Analysis

| Operation | Complexity |
|-----------|------------|
| Each Range Update | **O(1)** |
| Prefix Sum | **O(N)** |
| Total | **O(Q + N)** |

Where:

- `N` = Size of array
- `Q` = Number of range updates

---

# When to Use

Use the Difference Array Technique when:

- ✅ Multiple range increment/decrement operations
- ✅ Final array is required after all updates
- ✅ Large number of update queries

Avoid using it when:

- ❌ Values need to be queried immediately after every update
- ❌ Dynamic range queries are required (use Segment Tree or Fenwick Tree instead)

---

# Common Problems

- LeetCode 370 - Range Addition
- LeetCode 2381 - Shifting Letters II
- Corporate Flight Bookings
- Car Pooling
- Brightness of Lamps
- Range Increment Queries

---

# Key Takeaway

Instead of updating every element in a range:

```
O(length of range)
```

update only:

```python
diff[l] += val
diff[r + 1] -= val
```

and recover the final array using a **single prefix sum**, reducing the overall complexity from **O(Q × N)** to **O(Q + N)**.