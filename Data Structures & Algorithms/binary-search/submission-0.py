class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # variable definitions
        i = len(nums)//2
        node = nums[i]

        if not target in nums:
            return -1
        
        while node != target:
            if target < node:
                i-=1
                node = nums[i]
            else:
                i+=1
                node = nums[i]
        return i