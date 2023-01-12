 class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                cur[ch] = {}
                cur = cur[ch]
        cur['*'] = None

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                return False
        if '*' in cur:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch in cur:
                cur = cur[ch]
            else:
                return False
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)