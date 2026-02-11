test = int(input())

for i in range(test):
  length = int(input())
  char = input().strip()
  
  # checking if the permutation of a, b, c in the given char
  if 'aa' in char:
    print(2)
  elif 'aba' in char or 'aca' in char:
    print(3)
  elif 'acba' in char or 'abca' in char:
    print(4)
  elif 'abbacca' in char or 'accabba' in char:
    print(7)
  else:
    print(-1)
    
