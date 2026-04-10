class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p=0

        while p < len(nums):
            if nums[p] == val:
                nums.remove(nums[p])
            else:
                p += 1
        
        return len(nums)