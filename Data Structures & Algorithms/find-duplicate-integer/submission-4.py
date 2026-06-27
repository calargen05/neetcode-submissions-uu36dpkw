class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]

        fast,slow = 0,0

        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        # reset fast to 0 to verify duplicate number
        fast = 0

        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast