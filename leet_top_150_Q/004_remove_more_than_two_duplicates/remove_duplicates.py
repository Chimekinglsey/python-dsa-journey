from typing import List
from datetime import datetime
import random

class Solution:
    def removeDuplicates_v1(self, nums: List[int]) -> int:
        next_index = 2
        n_len = len(nums)
        if n_len < 3:
            return n_len
        for i in range(2, n_len):
            if nums[next_index - 1] == nums[next_index - 2] and nums[i] == nums[next_index - 1]:
                continue
            else:
                nums[next_index] = nums[i]
                next_index += 1
        return next_index
    
nums = sorted(random.choices(range(10), k=500000))
nums2, nums3, nums4 = nums[:], nums[:], nums[:]
solution = Solution()
solution.removeDuplicates_v1(nums)
solution.removeDuplicates_v2(nums2)
solution.removeDuplicates_v3(nums3)
solution.removeDuplicates_v4(nums4)

"""
From runtime analysis - removeDuplicates_v1 is most performant followed by v3, v4 and then v2 (the least)
"""