# Line Sweep Algorithm

The **Line Sweep Algorithm** (also called the **Sweep Line Technique**) is an optimization technique used to solve problems involving **intervals, events, overlapping ranges, and geometric computations** efficiently.

Instead of processing every point individually, we process only the **important events** (start and end points) in sorted order.

---
# Python Implementation (Maximum Overlapping Intervals)

```python
def maxOverlap(intervals):
    events = []

    for start, end in intervals:
        events.append((start, 1))
        events.append((end + 1, -1))

    events.sort()

    active = 0
    answer = 0

    for _, change in events:
        active += change
        answer = max(answer, active)

    return answer


intervals = [
    (1, 4),
    (2, 5),
    (7, 9)
]

print(maxOverlap(intervals))
```

### Output

```
2
```

---


# Why Use It?

Suppose there are multiple interval updates or interval-based events.

A brute-force solution checks every point or every interval against every other interval.

- **Brute Force:** `O(N²)` or worse.

The Line Sweep technique reduces this by processing only the event points.

- **Optimized:** Usually `O(N log N)` because of sorting.

---

# Intuition

Imagine a vertical line moving from **left to right** across the number line.

Whenever the line encounters:

- the **start** of an interval → something begins.
- the **end** of an interval → something ends.

We only update our state at these event points.

```
Intervals

[2--------6]
      [4--------8]
           [6------9]

Sweep Line →

0 1 2 3 4 5 6 7 8 9
    ↑   ↑   ↑
  Start Start End
```

---

# Example 1: Maximum Overlapping Intervals

Intervals

```
[1,4]
[2,5]
[7,9]
```

Create events:

| Position | Change |
|----------|--------|
| 1 | +1 |
| 2 | +1 |
| 5 | -1 |
| 6 | -1 |
| 7 | +1 |
| 10 | -1 |

Now process in sorted order.

| Position | Active Intervals |
|----------|------------------|
| 1 | 1 |
| 2 | 2 |
| 5 | 1 |
| 6 | 0 |
| 7 | 1 |
| 10 | 0 |

Maximum overlap = **2**

---

# Difference Array Connection

The Difference Array is actually a special case of the Line Sweep technique.

For an interval `[l, r]`:

```python
events[l] += val
events[r + 1] -= val
```

Then compute the prefix sum.

Notice that we only process the **start** and **end** events.

---

# Event Representation

Suppose we have

```
[3,7]
```

Create two events:

```
(3, +1)
(8, -1)
```

Meaning

- Add one active interval at `3`
- Remove one active interval after `7`

---

# Example

Intervals

```
[1,3]
[2,5]
[4,6]
```

Events

```
1 → +1
2 → +1
4 → -1
4 → +1
6 → -1
7 → -1
```

Sort events

```
1
2
4
4
6
7
```

Sweep

```
Position 1 → active = 1

Position 2 → active = 2

Position 4
    -1
    +1

active = 2

Position 6
    -1

active = 1

Position 7
    -1

active = 0
```

Maximum overlap = **2**

---

# Generic Algorithm

1. Convert every interval into events.
2. Store the events.
3. Sort all events.
4. Traverse from left to right.
5. Maintain the current active state.
6. Update the answer whenever needed.

---


# Line Sweep vs Difference Array

| Difference Array | Line Sweep |
|------------------|------------|
| Works on arrays | Works on events |
| Uses prefix sum | Uses sorted events |
| Coordinates are continuous (0...N-1) | Coordinates can be very large |
| O(N + Q) | O(N log N) |
| Best for range updates | Best for interval/event problems |

---

# Complexity

Suppose there are `N` intervals.

Creating events

```
O(N)
```

Sorting events

```
O(N log N)
```

Sweeping

```
O(N)
```

Overall

```
O(N log N)
```

---

# When to Use

Use Line Sweep when you encounter:

- ✅ Interval overlap problems
- ✅ Calendar scheduling
- ✅ Meeting room allocation
- ✅ Skyline problems
- ✅ Counting active intervals
- ✅ Geometry problems
- ✅ Event processing
- ✅ Large coordinate values
- ✅ Rectangle union/intersection

---

# Common Problems

- LeetCode 253 - Meeting Rooms II
- LeetCode 218 - The Skyline Problem
- LeetCode 732 - My Calendar III
- LeetCode 1094 - Car Pooling
- LeetCode 1943 - Describe the Painting
- LeetCode 391 - Perfect Rectangle

---

# Difference Array vs Line Sweep

Difference Array

```
Array
│
├── +val at l
├── -val at r+1
└── Prefix Sum
```

Line Sweep

```
Intervals
│
├── Convert to Events
├── Sort Events
├── Sweep Left → Right
└── Maintain Current State
```

---

# Key Takeaway

The Line Sweep Algorithm processes only the **important event points** instead of every position.

Instead of checking every interval against every other interval, we:

1. Convert intervals into events.
2. Sort the events.
3. Sweep from left to right while maintaining the current state.

This transforms many interval problems from **O(N²)** into **O(N log N)**.