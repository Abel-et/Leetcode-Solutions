from collections import Counter


for _ in range(int(input())):
    a = input()
    b = input()
    s = Counter(a)
    t = Counter(b)
   
    
    # check s is sub sequence of t
    
    check = not (s - t) 
    
    if check :
        ans = []
        
        # put all the key element of second string into array
        # then lexicographically sorted 
        keys =sorted([key for key in t.keys()])
        
        # using pointer in separate arrays approach 
        first, second = 0 , 0
        while first < len(a) and second <len(keys):
            if keys[second] < a[first]:
                element = keys[second]
                if element in s:
                    if t[element] - s[element] > 0:
                        dif = t[element] - s[element]
                        for i in range(dif):
                            ans.append(element )
                else:
                    for i in range(t[element]):
                        ans.append(element )
                second += 1
            else:
                ans.append(a[first])
                first += 1
                
        # if there is remaining element in the keys or in t 
        while second < len(keys):
            if keys[second] in s:
                if t[keys[second]] - s[keys[second]]>0:
                    dif = t[keys[second]] - s[keys[second]]
                    for i in range(dif):
                        ans.append(keys[second])
            else: 
                for i in range(t[keys[second]]):
                    ans.append(keys[second])
            second += 1
        print(''.join(ans))
        
    #  if the s  is not sub sequence of t
    else:
        print("Impossible")