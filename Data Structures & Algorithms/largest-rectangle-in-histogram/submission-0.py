'''
    UPI Method:

        Understand: The problem is asking me to find the largest rectangle area that can be formed
        from the bars (numbers) in the histogram.

        Plan: I think that I append the values that are larger than the current top of the stack
        until I find a smaller value, then I calculate the current area and check if adding the
        smaller value would increase the area or decrease the area. If it decreases, I would keep
        the value of the area stored and then clear the stack. However, if it increases the area,
        then I would push it to the top of the stack and keep iterating
        Implement: See below VVV
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rec = 0

        # ADD CODE HERE
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                rec = max(rec, height*(i-index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            rec = max(rec, h*(len(heights) - i))
        return rec