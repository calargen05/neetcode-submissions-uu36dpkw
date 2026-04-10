class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list so it can be two pointer-ed properly
        nums.sort()
        res = []

        # loop to iterate through the nums
        for i in range(len(nums)-1):
            # skip duplicate i values
            if i > 0 and nums[i] == nums[i-1]: continue

            # reset the pointers after every loop to find a trio of nums
            l, r = i+1, len(nums)-1

            # nested while loop to find which pointer needs to move
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1

                # success case
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # nested loops to get rid of duplicates for the pointers
                    while l < r and nums[l] == nums[l-1]: l+=1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]: r-=1

        return res