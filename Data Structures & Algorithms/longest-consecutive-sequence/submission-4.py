class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            nums.sort()
            count = 1
            max_count = 1
            for i in range (0,len(nums)-1):
                if nums[i+1] == nums[i]+1:
                    count+=1
                    if count > max_count:
                        max_count = count
                elif nums[i+1] == nums[i]:
                    continue
                else:
                    count=1
            return max_count