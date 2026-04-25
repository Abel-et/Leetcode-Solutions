# elephants move forward
position = 5

moves = 0

if  x <= 5:
    print(moves+1)
else:
    while position > 0:
        moves += x//position
        # after moving moves position x will remain
        x = x%position
        
        # this will chose best position for the remaining x location
        position = x%position
        
    print(moves)