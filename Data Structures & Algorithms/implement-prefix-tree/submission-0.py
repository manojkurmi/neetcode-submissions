class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if not ch in root:
                root[ch] = {}
            root = root[ch]
        root["end"] = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch in root:
                root = root[ch]
            else:
                return False
        return root.get("end") == True
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch in root:
                root = root[ch]
            else:
                return False
        return True
        

"""
prefix tree or trie
all lower case letters

store char map and word marker
marker tell whether a complete ward is there

"""