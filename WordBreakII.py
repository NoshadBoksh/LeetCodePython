class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)  # For O(1) lookups
        memo = {}  # Memoization dictionary

        def backtrack(start):
            # If we've already computed results for this start index, return them
            if start in memo:
                return memo[start]

            # Base case: reached the end of the string
            if start == len(s):
                return [""]

            sentences = []

            # Try all possible end positions
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    # Get all valid continuations from the remaining substring
                    for subsentence in backtrack(end):
                        # Add a space only if there is a next part
                        if subsentence:
                            sentences.append(word + " " + subsentence)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return backtrack(0)
