from typing import List
def add_two_v1(nums: List[int], target: int) -> List[int]:
    """Using brute force to iterate in 0(n^2)"""
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
    return 'No match found'



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        if a + b = c, then c - a = b and c - b = a
        We will use this formula to map keys to remainder values of target
        """
        key_hash = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in key_hash:
                return [key_hash[remainder], i]
            key_hash[nums[i]] = i
        return [0, 0]
