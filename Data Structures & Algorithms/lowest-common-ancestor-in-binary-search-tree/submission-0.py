# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path, curr = [], []
        def dfs(node):
            if not node:
                return
            
            if node == p or node == q:
                curr.append(node)
                path.append(curr.copy())
            else:
                curr.append(node)

            dfs(node.left)
            dfs(node.right)

            curr.pop()
        
        dfs(root)

        print(path)
        p1, p2 = path[0], path[1]
        ptr = 0
        lca = None
        while ptr < len(p1) and ptr < len(p2):
            if p1[ptr] == p2[ptr]:
                lca = p1[ptr]
            ptr += 1
        
        return lca