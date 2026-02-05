class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        length =0
        # i changed the string into a list 
        g = list(chars)

        # Traverse over all words in the the word list
        for word in words:
            
            #  if length of single word is greater that the former word return false
            if len(word) > len(chars):
                continue

                # travers in each word letters and check if they are found into the former list
            for i in word:
                if i not in g :
                    break
                else:
                    # on the question it say each character could only be used onces for each word
                    p = word.count(i)
                    k = g.count(i)
                    # checking if the a letter is appeared morethan number of former list 
                    if p > k:
                        break
            else:

                #add the vaild word length
                length += len(word)
        return length