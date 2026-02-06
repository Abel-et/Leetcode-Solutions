import collections
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        n = len(paths)

        collector = {}

        for i in paths:
            path = i.split()
            print(path)
            
            for files in path:
                if 'root' in files:
                    continue
                else:
                    content = files[files.index('(')+1 :files.index(')')]
                    text = files[:files.index('(')]
                    if content in collector:
                        collector[content].append(f'{path[0]}/{text}')
                    else:
                        collector[content] = []
                        collector[content].append(f'{path[0]}/{text}')
                 
       
        # od = collections.OrderedDict(sorted(collector.items()))

    
        return [value for key, value in od.items() if len(value)>1]
