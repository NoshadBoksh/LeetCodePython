from collections import deque, defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Convert wordList to a set for O(1) lookup
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Preprocess: create a dictionary of all generic forms
        # Example: "hot" -> "*ot", "h*t", "ho*"
        adj = defaultdict(list)
        L = len(beginWord)
        for word in wordSet:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        # BFS queue: (current_word, steps)
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            # Try all one-letter transformations
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in adj[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))
                # Optional: clear pattern to reduce redundant loops
                adj[pattern] = []

        return 0
