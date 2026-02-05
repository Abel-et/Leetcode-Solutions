class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        length =0
        g = list(chars)
        for word in words:
            if len(word) > len(chars):
                continue
            for i in word:
                if i not in g :
                    break
                else:
                    g.remove(i)
            else:
                g = list(chars)
                length += len(word)
        return length