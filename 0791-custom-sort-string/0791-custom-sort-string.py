from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        permuted = []
        remained = Counter(s)
        for i in order:
            if i in remained:
                permuted.append(i)
                remained[i] -=1
        print(permuted)
        for key,val in remained.items():
            if val > 0 and key in permuted:
                index = permuted.index(key)
                permuted.insert(index, key )
            elif val > 0 :
                permuted.append(key)
        return "".join(permuted)