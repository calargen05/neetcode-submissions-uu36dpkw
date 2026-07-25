"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodes = deque()
        adjDict = {}

        # get the nodes in a queue
        nodes.append(node)
        adjDict[node] = Node(node.val)
        while nodes:
            n = nodes.popleft()
            for N in n.neighbors:
                if N not in adjDict:
                    nodes.append(N)
                    adjDict[N] = Node(N.val)
                adjDict[n].neighbors.append(adjDict[N])
        
        
        return adjDict[node]
        