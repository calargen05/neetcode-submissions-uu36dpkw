class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        
        sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)

        result = [item[0] for item in sorted_d[:k]]
        
        return result
            
            