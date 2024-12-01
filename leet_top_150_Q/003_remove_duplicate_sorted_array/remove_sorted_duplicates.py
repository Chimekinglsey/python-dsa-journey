from typing import List
from datetime import datetime
import random

class Solution:
    def removeDuplicates_v1(self, nums: List[int]) -> int:
        """
        Using the built-in set and sorted functions to remove duplicates and maintain the order.
        """
        print(f"\n{self.__class__.removeDuplicates_v1.__name__}")
        start = datetime.now()
        nums[:] = sorted(set(nums))
        stop = datetime.now() - start
        print(len(nums), stop, nums)
        return len(nums)
    
    def removeDuplicates_v2(self, nums: List[int]) -> int:
        """
        Let's use a less efficient two loops with additional space to store a duplicate for checks
        """
        print(f"\n{self.__class__.removeDuplicates_v2.__name__}")
        start = datetime.now()

        dups_nums = []
        for i in range(len(nums)):
            if nums[i] not in dups_nums:
                dups_nums.append(nums[i])
                
        for i in range(len(dups_nums)):
            nums[i] = dups_nums[i]
        

        stop = datetime.now() - start
        print(len(dups_nums), stop, dups_nums)
        return len(dups_nums)
    
    def removeDuplicates_v3(self, nums: List[int]) -> int:
        """
        Let's use a single loop woth extra space. Two pointers for read and write
        We will use one pointer to skip duplicates
        """
        print(f"\n{self.__class__.removeDuplicates_v3.__name__}")
        start = datetime.now()
        dup = nums
        i = 0
        for j in range(1, len(dup)):
            if nums[i] != dup[j]:
                nums[i + 1] = dup[j]
                i += 1
        stop = datetime.now() - start

        print(i + 1, stop, nums[:i+1])
        return i + 1 # we initialized i to 0 but it does not check nums[0] but nums[i + 1]
    
    def removeDuplicates_v4(self, nums: List[int]) -> int:
        """
        Let's use two pointers to read and write but without extra space
        """
        print(f"\n{self.__class__.removeDuplicates_v4.__name__}")
        start = datetime.now()

        if len(nums) < 2:
            return len(nums)
        i = 1
        for j in range(1, len(nums)):
            if nums[i - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        stop = datetime.now() - start
        print(i, stop, nums[:i])
        return i
    
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