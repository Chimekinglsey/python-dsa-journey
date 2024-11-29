from typing  import List

def merge_v1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
        Since len(nums1) = m + n where m and n are numbers of array elements in both arrays,
        I will first use list manupulations with in-place sort()
        
        First, we will ensure that if any array is empty, the other is returned as nums1
        If both arrays are contain items, then the items in nums1 occupying 
        index of nums1[-n:] will be overwritten with nums2
    """
    if not nums2:
        pass
    elif not nums1:
        nums1[:] = nums2
    else:
        nums1[:] = nums1[:-n] + nums2
        nums1.sort()

nums1 = [2, 5, 7,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# merge_v1(nums1=nums1, m=m, nums2=nums2, n=n)
# print(nums1) #[1, 2, 2, 3, 5, 6]

def merge_v2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """ 
    Simpler string manipulation:
    since nums1[m:] holds all the valid values for nums1, we can simply merge and return the sort
    
    """
    nums1[m:] = nums2[:n] # or simply nums2
    nums1.sort()

# merge_v2(nums1=nums1, m=m, nums2=nums2, n=n)
# print(nums1) #[1, 2, 2, 3, 5, 6]


def merge_v3(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    We will use a loop and maintain a positional placement of items from nums2 into nums1
    checks:
        If the last element in nums1 is greater than that of num2, it goes to the extreme right
        this is because both lists are sorted.
        Until nums2 (which contains the elements that should all be merged) is exhausted we will keep iterating
    """
    
    m_index = m - 1
    n_index = n - 1
    last_index = m + n - 1
    
    while n_index >= 0:
        if m_index >= 0 and nums1[m_index] > nums2[n_index]:
            nums1[last_index] = nums1[m_index]
            m_index -= 1
        else:
            nums1[last_index] = nums2[n_index]
            n_index -= 1
            
        last_index -= 1

merge_v3(nums1=nums1, m=m, nums2=nums2, n=n)
print(nums1)