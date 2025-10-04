class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])              # Length of each word
        num_words = len(words)                # Total number of words
        total_len = word_len * num_words      # Total length of concatenated substring
        word_count = {}                       # Frequency of words in 'words'
        
        # Build the word frequency map
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        res = []
        
        # We only need to start checking from indices < word_len
        for i in range(word_len):
            left = i
            curr_count = {}
            count = 0  # number of words matched
            
            # Move right pointer in chunks of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                w = s[right:right + word_len]
                
                if w in word_count:
                    curr_count[w] = curr_count.get(w, 0) + 1
                    count += 1
                    
                    # If word appears too many times, shrink the window
                    while curr_count[w] > word_count[w]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # If all words matched, record the start index
                    if count == num_words:
                        res.append(left)
                else:
                    # Reset window if invalid word found
                    curr_count.clear()
                    count = 0
                    left = right + word_len
        
        return res
