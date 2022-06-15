class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i need to create a hashmap where mapping of counts of each word to list of anagrams
        
        result = defaultdict(list)
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()
    
    # O(26*n*len(s)), O(n)
