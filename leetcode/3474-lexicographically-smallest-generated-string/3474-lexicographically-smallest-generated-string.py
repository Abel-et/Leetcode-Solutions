class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        
        def lexicographicallySmallest(str1, str2):
            n, m = len(str1), len(str2)
            L = n + m - 1
            res = [None] * L
            fixed = [False] * L
            
            # Step 1: Fill all 'T' constraints
            for i in range(n):
                if str1[i] == 'T':
                    for j in range(m):
                        if res[i + j] is not None and res[i + j] != str2[j]:
                            return ""
                        res[i + j] = str2[j]
                        fixed[i + j] = True
            
            # Step 2: Fill remaining with 'a' to get a baseline smallest string
            for i in range(L):
                if res[i] is None:
                    res[i] = 'a'
            
            # Step 3: Satisfy 'F' constraints
            # Iterate through the string. If an 'F' constraint is violated,
            # try to change the rightmost non-fixed character in that window
            # to the smallest possible character that fixes it.
            # Since we want lexicographically smallest, we should ideally check 
            # from left to right, but once we change a character, it might affect 
            # subsequent 'F's. 
            
            def check_f():
                for i in range(n):
                    if str1[i] == 'F':
                        is_match = True
                        for j in range(m):
                            if res[i+j] != str2[j]:
                                is_match = False
                                break
                        if is_match:
                            return i
                return -1

            while True:
                idx_f = check_f()
                if idx_f == -1: break
                
                # Found a violation at idx_f. We must change one character in res[idx_f : idx_f + m]
                # to be different from str2[0:m]. To keep it lexicographically smallest, 
                # we should change the rightmost possible character.
                found = False
                for j in range(m - 1, -1, -1):
                    pos = idx_f + j
                    if not fixed[pos]:
                        # Try next character
                        original = res[pos]
                        # Try smallest char > original
                        for c_code in range(ord(original) + 1, ord('z') + 1):
                            res[pos] = chr(c_code)
                            # After changing, we might need to re-verify everything.
                            # However, we only move 'up' in lexicographical order.
                            found = True
                            break
                        if found: break
                
                if not found: return "" # Cannot satisfy 'F'
                
            return "".join(res)
        return lexicographicallySmallest(str1, str2)