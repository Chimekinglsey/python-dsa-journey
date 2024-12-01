from typing import List
from datetime import datetime
import random
def remove_element_v1(nums: List[int], val: int) -> int:
    """We will use list manipulation in a loop first. This method does the job in 0(n ^ 2)"""
    start = datetime.now()
    for _ in range(nums.count(val)):
        nums.remove(val)
    stop = f'{datetime.now() - start} seconds'
    result = len(nums)
    print(result, stop)
    return result

nums = random.choices(range(1, 5), k=50_000) # Performance of each solution in 50,000 elements list
val = 3
print(f'\n================List lenght = {len(nums)}================\n')

print('Array methods of count() and remove()')
remove_element_v1(nums, val)

def remove_elements_v2(nums: List[int], val: int) -> int:
    """This does the job in 0(n) using list comprehension"""
    start = datetime.now()
    nums[:] = [x for x in nums if x != val]
    stop = f'{datetime.now() - start} seconds'
    result = len(nums)
    print(result, stop)
    return result

print('\nList comprehension')
remove_elements_v2(nums, val)

def remove_elements_v3(nums: List[int], val: int) -> int:
    """Let's use two pointers in a loop to solve the problem. This has a complexity of 0(n)"""
    start = datetime.now()
    i = 0 
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    stop = f'{datetime.now() - start} seconds'
    print(i, stop)
    return i

print('\nTwo pointer loop')
remove_elements_v3(nums, val)