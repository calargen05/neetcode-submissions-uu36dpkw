class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if node.children[index] == None:
                new_node = TrieNode()
                node.children[index] = new_node
            node = node.children[index]
        node.isLast = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if node.children[index] == None:
                return False
            node = node.children[index]
        return node.isLast

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if node.children[index] == None:
                return False
            node = node.children[index]
        return True
        

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False