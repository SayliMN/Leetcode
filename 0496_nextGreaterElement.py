class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1) #O(n)
        for i, val in enumerate(nums1): # O(n)
            for j in range(nums2.index(val)+1, len(nums2)): #O(n)
                if nums2[j] > val:
                    result[i] = nums2[j]
                    break
        return result
    
    # O(n*2), O(n)
