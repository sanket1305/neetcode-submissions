class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.is_word = True
    
    def search(self, s, i, j):
        node = self.root

        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        
        return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie = Trie()

        for word in wordDict:
            trie.insert(word)
        
        dp = [False]*(n+1)
        dp[-1] = True

        t = 0
        for word in wordDict:
            t = max(t, len(word))
        
        for i in range(n-1, -1, -1):
            for j in range(i, min(n, i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break
        
        return dp[0]