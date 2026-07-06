class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        l,r = 0,k-1
        while r < len(nums):
            out.append(max(nums[l:r+1]))
            l+=1
            r+=1
        return out