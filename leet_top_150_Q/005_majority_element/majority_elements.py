from typing import List
from datetime import datetime
from random import choices
from collections import Counter

def performance_time(f):
    def calculator(*args, **kwargs):
        start_time = datetime.now()
        result = f(*args, **kwargs)
        stop_time = datetime.now() - start_time
        print(f"{f.__name__} ran for {stop_time} with result ==> {result or 'No return value'}")
    return calculator

class Solution:
    """Find the majority elements in an array"""
    @performance_time
    def majority_elements_v1(self, nums: List[int]) -> int:
        """
        First we will sort this list and since majority element appears at least n/2 times, 
        the mid item in the sorted list is the majority
        """
        mid_index = len(nums) // 2
        nums.sort()
        return nums[mid_index]
    
    @performance_time
    def majority_elements_v1_b(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


nums = choices(range(1, 5), weights=[1,1,3,2], k=50)
# solution = Solution()
# solution.majority_elements_v1(nums)
# solution.majority_elements_v1_b(nums)

def majorityElement(nums: List[int]) -> int:
    length = len(nums)
    if length < 1:
        return nums
    num_dict = dict()
    for n in nums:
        if n in num_dict:
            print(f"{num_dict=}")
            num_dict[n] = num_dict[n].append(n)
        else:
            num_dict[n] = list(n)
    print(f"{num_dict=} totalled")
    m_elem = 0
    for n in num_dict:
        if num_dict[n] and len(num_dict[n]) > m_elem:
            m_elem = n
    print(f"{m_elem=} is the majority element")
    return m_elem

majorityElement(nums)