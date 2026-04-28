class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for elem in nums:
            hashmap[elem] += 1
        
        sorted_hashmap = dict(sorted(hashmap.items(), key = lambda x: x[1], reverse = True))
        list_of_keys = list(sorted_hashmap.keys())
        return list_of_keys[:k]
        
        return list(hashmap.items())