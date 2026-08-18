# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        serial = ''
        queue = deque()
        queue.append(root)
        substr = 'n' + str(root.val) + ';'
        serial += substr
        while queue:
            node = queue.popleft()
            if node.left:
                substr = 'n' + str(node.left.val) + ';'
                serial += substr
                queue.append(node.left)
            if not node.left:
                substr = 'n' + str(None) + ';'
                serial += substr
            if node.right:
                substr = 'n' + str(node.right.val) + ';'
                serial += substr
                queue.append(node.right)
            if not node.right:
                substr = 'n' + str(None) + ';'
                serial += substr       
        print(serial)
        return serial
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        data = data.split(';')
        queue = deque()
        i = 0
        root = TreeNode(val=int(data[i][1:]))
        i += 1
        queue.append(root)
        while queue and i < len(data):
            node = queue.popleft()
            if data[i][1:] != 'None':
                node_left = TreeNode(val=int(data[i][1:]))
                node.left = node_left
                queue.append(node_left)
            i += 1
            if i >= len(data):
                break
            if data[i][1:] != 'None':
                node_right = TreeNode(val=int(data[i][1:]))
                node.right = node_right
                queue.append(node_right)
            i += 1

        return root

