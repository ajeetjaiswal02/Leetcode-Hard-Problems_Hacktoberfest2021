class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}

    def addNode(self, char, node):
        self.children[char] = node

class Trie:
    def __init__(self):
        self.root = TrieNode('0')

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                child = TrieNode(c)
                cur.addNode(c, child)
            cur = cur.children[c]

    def search_words(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        result = list(cur.children.keys())
        print(result)
        cur.children = {}
        return result
    
    def print_trie(self):
        q = [self.root]
        while len(q) > 0:
            for node in q:
                print(node.char)
                new_q = []
                new_q += list(node.children.values())
                q = new_q

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        trie_forest = []
        for i in range(n):
            new_trie = Trie()
            for word in wordList:
                word_list = list(word)
                if i != n - 1 and word_list[i] == word_list[n - 1]:
                    continue
                word_list[i], word_list[n - 1] = word_list[n - 1], word_list[i]
                new_trie.insert("".join(word_list))
            trie_forest.append(new_trie)
        
        existing_set = {beginWord}
        steps = 1
        current_level = {beginWord}
        next_level = set()
        while len(current_level) != 0:
            for word in current_level:
                for i in range(n):
                    word_list = list(word)
                    word_list[i] = word_list[n - 1]
                    new_char_list = trie_forest[i].search_words(word_list[:-1])
                    for ch in new_char_list:
                        word_list[i] = ch
                        new_word = "".join(word_list)
                        if new_word == endWord:
                            return steps
                        if new_word not in existing_set:
                            next_level.add(new_word)
            current_level = next_level
            steps += 1
            existing_set.update(current_level)

        return 0
