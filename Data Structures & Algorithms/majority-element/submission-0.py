class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 0
        
        m = nums[0]
        for key in d.keys():
            if d[key] > d[m]:
                m = key
        
        return m