# this arr hold all left right and real values
  arr = []
  
  # receive the length of arr and coin 
  n,k = map(int , input().split())
  
  # n time append left right and real values
  for _ in range(n):
    arr.append(list(map(int, input().split())))
  
  arr.sort(key=lambda x: x[0])
  coin = k
  
  
  # checks if the coin is 
  if k < arr[0][0] :
    print(k)
  else:
    for i in range(len(arr)):
      left = arr[i][0]
      real = arr[i][2]
      right = arr[i][1]
      
      # if the coin is interval of left and right
      if  coin >= left and coin <= right :
        
        #  if curr coin value is less than real value update coin 
        if coin < real:
          coin = real
      elif coin < left:
        break
    print(coin)