class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        for hour in range(12):
            for minuite in range(60):
                if bin(hour).count('1') + bin(minuite).count('1') == turnedOn:
                    if minuite < 10 :
                        result.append(f'{hour}:0{minuite}')
                    else:
                        result.append(f'{hour}:{minuite}')
        return result