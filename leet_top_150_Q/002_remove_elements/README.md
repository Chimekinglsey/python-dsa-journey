```markdown
# Remove Element

**Difficulty:** Easy  
**Status:** Solved  

---

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

### Requirements:
- The number of elements in `nums` that are **not equal to `val`** will be denoted as `k`.
- Modify the array `nums` such that the first `k` elements contain the elements that are **not equal to `val`**.
- The remaining elements of `nums` are not important.
- Return `k`.

---

## Custom Judge

The judge will test your solution using the following steps:

```java
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
// It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length; // Check if k matches expected length
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, your solution is accepted.

---

## Examples

### Example 1:
**Input:**  
`nums = [3,2,2,3]`, `val = 3`  
**Output:**  
`k = 2`, `nums = [2,2,_,_]`  
**Explanation:**  
The first `k = 2` elements of `nums` are `[2, 2]`. The remaining elements can be ignored.

---

### Example 2:
**Input:**  
`nums = [0,1,2,2,3,0,4,2]`, `val = 2`  
**Output:**  
`k = 5`, `nums = [0,1,4,0,3,_,_,_]`  
**Explanation:**  
The first `k = 5` elements of `nums` are `[0, 1, 4, 0, 3]`. The order of these elements does not matter.

---

## Constraints:
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`
```