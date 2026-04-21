# checking on the current block the give char is working or not
        while i < len(s) and s[i] == char:
            count += 1
            i += 1
            
        if count % 2 == 1:
            
            working.add(char)
    
    print(''.join(sorted(list(working))))