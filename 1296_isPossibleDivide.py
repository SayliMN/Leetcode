class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    
        # mapping = {}
        # for i in range(len(nums)):
        #     if nums[i] not in mapping:
        #         mapping[nums[i]] = 1
        #     else:
        #         mapping[nums[i]] += 1
                    
    # O(nlogn)
        
        mapping = Counter(nums)
        for n in sorted(mapping):
            if mapping[n] > 0:
                need = mapping[n]
                for i in range(n,n+k):
                    if mapping[i] < need:
                        return False
                    mapping[i] -= need
        return True
