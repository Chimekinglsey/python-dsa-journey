Here’s a well-structured `README.md` for your repository with the first problem documented:

```markdown
# LeetCode Challenge: Solving 150 Top Technical Questions

This repository documents my journey in solving 150 top technical questions on LeetCode. Each question includes the problem statement, my solution, and any insights or approaches I found useful while solving it.

---

## Problem 1: Merge Sorted Array

### Problem Statement

**Difficulty**: Easy  
**Topics**: Arrays, Two Pointers, Sorting  

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order. The result should be stored inside `nums1`. 

To accommodate this:
- `nums1` has a length of `m + n`, where the first `m` elements are the elements to be merged, and the last `n` elements are initialized to `0` and should be ignored.
- `nums2` has a length of `n`.

#### Example 1
```plaintext
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3  
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

#### Example 2
```plaintext
Input: nums1 = [1], m = 1, nums2 = [], n = 0  
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

#### Example 3
```plaintext
Input: nums1 = [0], m = 0, nums2 = [1], n = 1  
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
```

#### Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

#### Follow-Up
Can you come up with an algorithm that runs in **O(m + n)** time?

---

```