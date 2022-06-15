class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mapping count of number as a key to a list of numbers
        if len(nums) <= 1:
            return nums
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            freq[c].append(n)
            
        result = []
        for i in range(len(freq)-1, -1,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
                
        # O(n),O(n)
            
        
        
