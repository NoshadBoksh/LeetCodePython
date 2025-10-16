class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line = []
        length = 0  # total length of words (excluding spaces)

        for word in words:
            # Check if adding the next word exceeds the line width
            if length + len(word) + len(line) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - length):
                    # Distribute from left to right cyclically
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line = []
                length = 0

            line.append(word)
            length += len(word)

        # Handle the last line (left-justified)
        last_line = ' '.join(line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))

        return res
