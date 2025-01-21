from typing import List
from datetime import datetime
import random
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)



def performance_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        stop = datetime.now() - start
        print(f'{func.__name__} Executed in {stop} \t {result=}')
    return wrapper
    

class Solution:
    @performance_time
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
    
    @performance_time
    def removeDuplicates_v2(self, nums: List[int]) -> int:
        next_index = 2
        n_len = len(nums)
        if n_len < 3:
            return n_len
        for i in range(2, n_len):
            if nums[i] != nums[next_index - 2]:
                nums[next_index] = nums[i]
                next_index += 1
        return next_index
    
nums = sorted(random.choices(range(10), k=5000000))
nums2, nums3, nums4 = nums[:], nums[:], nums[:]
solution = Solution()
solution.removeDuplicates_v1(nums)
solution.removeDuplicates_v2(nums2)
# solution.removeDuplicates_v3(nums3)
# solution.removeDuplicates_v4(nums4)

"""
From runtime analysis - removeDuplicates_v2 is most performant
"""