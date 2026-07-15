"""
NAIVE SOLUTION: O(n) worst-case time complexity

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


"""


# BINARY SEARCH SOLUTION

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # finding the pivot to split the 2 lists
        l,r = 0, len(nums)-1
        pivot = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[pivot]:
                pivot = mid
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        l1,l2 = nums[:pivot], nums[pivot:]

        l,r = 0, pivot-1

        # first list binary search
        while l<=r:
            mid = (l+r) // 2
            if l1[mid] == target:
                return mid
            elif l1[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # second list binary search
        l,r = 0, len(l2)-1
        while l <= r:
            mid = (l+r) // 2
            if l2[mid] == target:
                return mid + pivot
            elif l2[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
