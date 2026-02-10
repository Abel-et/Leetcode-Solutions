class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = []
        opened = False
        n  = len(source)
        temp = ''

        for line in source:
            i = 0 

            if not opened:
                temp = ""
            while i < len(line):
                if not opened and i+1 < len(line) and line[i:i+2] =="/*":
                    opened = True
                    i +=2
                elif opened and i+1 <len(line) and line[i:i+2] =="*/":
                    opened = False
                    i +=2
                elif not opened and i+1 < len(line) and line[i:i+2] =="//":
                    break
                elif not opened:
                    temp += line[i]
                    i+=1
                else:
                    i+=1
            if not opened and temp :
                code.append(temp)
        return code


