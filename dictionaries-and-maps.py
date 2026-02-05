import sys
n = int(input())
book = dict()
for i in range(n):
    name , phone = map(str, input().split())
    book[name] = phone


for query in sys.stdin:
    name = query.strip()
    
    if not name :
        continue
    if name in book:
        print(f'{name}={book[name]}')
    else:
        print("Not found")
