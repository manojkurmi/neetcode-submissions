class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root:
                root[ch] = {}
            root = root[ch]
        root["end"] = True

        

    def search(self, word: str) -> bool:
        def dfs(root, idx):
            if not root:
                return False
            if idx >= len(word):
                return root.get("end") == True
            ch = word[idx]
            if ch != ".":
                return dfs(root.get(ch), idx+1)
            for key in root.keys():
                if key != "end" and dfs(root[key], idx+1):
                    return True
            return False

        return dfs(self.root, 0)
        
