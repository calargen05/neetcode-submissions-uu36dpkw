class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def move_left(res, left, right, bottom):
            while right >= left:
                res.append(matrix[bottom][right])
                right -= 1
        
        def move_right(res, left, right, top):
            while left <= right:
                res.append(matrix[top][left])
                left += 1
        
        def move_up(res, top, bottom, left):
            while bottom >= top:
                res.append(matrix[bottom][left])
                bottom -= 1

        def move_down(res, top, bottom, right):
            while top <= bottom:
                res.append(matrix[top][right])
                top += 1
        
        out = []
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        size = (right + 1) * (bottom + 1)

        while len(out) < size:
            # cycle
            move_right(out, left, right, top)
            top += 1
            move_down(out, top, bottom, right)
            right -= 1
        
            if top <= bottom:
                move_left(out, left, right, bottom)
                bottom -= 1
            if left <= right:
                move_up(out, top, bottom, left)
                left += 1
        
        return out

