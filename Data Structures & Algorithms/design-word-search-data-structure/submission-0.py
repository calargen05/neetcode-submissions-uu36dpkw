class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] == None:
                new_node = TrieNode()
                node.children[index] = new_node
            node = node.children[index]
        node.isLast = True

    def search(self, word: str) -> bool:
        def dfs(word, node):
            if not word:
                return node.isLast
            
            if word[0] == '.':
                for n in node.children:
                    if n != None:
                        if dfs(word[1:], n):
                            return True
                return False
            else:
                index = ord(word[0]) - ord('a')
                if node.children[index] == None:
                    return False
                    
                return dfs(word[1:], node.children[index])

        
        return dfs(word, self.root)
    
