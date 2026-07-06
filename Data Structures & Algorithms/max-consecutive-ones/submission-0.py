class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        p,streak,max_streak=0,0,0
        while p < len(nums):
            if nums[p] == 1:
                streak+=1
            else:
                max_streak = max(streak,max_streak)
                streak = 0
            p += 1
        
        return max(max_streak,streak)