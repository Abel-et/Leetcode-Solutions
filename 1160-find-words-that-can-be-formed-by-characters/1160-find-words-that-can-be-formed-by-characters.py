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
            print(word)
            if len(word) > len(chars):
                continue
            for i in word:
                if i not in g :
                    break
                else:
                    p = word.count(i)
                    k = g.count(i)
                    if p > k:
                        break
            else:
                length += len(word)
        return length