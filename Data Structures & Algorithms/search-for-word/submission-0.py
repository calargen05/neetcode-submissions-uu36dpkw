class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, k):
            # base case 1 - word is found
            if k == len(word):
                return True
            
            # base case 2 - letter doesn't match or out of bounds
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[k]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r-1, c, k+1) or
                    dfs(r+1, c, k+1) or
                    dfs(r, c-1, k+1) or
                    dfs(r, c+1, k+1)
            )

            board[r][c] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False



'''

def exist:
    curr = []

    dfs function(i, j):
        if string-version of curr == word:
            return True
        
        if i < 0 or i > length of board rows:
            return
        if j < 0 or j > length of board columns:
            return
        
        append board[i][j] to curr

        # left
        dfs(i, j-1)
        pop from back of curr
        # right
        dfs(i, j+1)
        pop from back of curr
        # up
        dfs(i-1, j)
        pop from back of curr
        # down
        dfs(i+1, j)
        pop from back of curr
    
    for i in len(board):
        for j in len(board[0]):
            if board[i][j] == word[0]:
                dfs[i][j]
    
    return False

'''