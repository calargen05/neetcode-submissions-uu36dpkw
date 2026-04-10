class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()

        for i in range(len(nums2)):
            nums.append(nums2[i])
        
        return nums