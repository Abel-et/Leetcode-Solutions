a = input()
b = input()

c = ''
n = len(a)

for i in range(n):
    if a[i] != b[i]:
        c += '1'
    else:
        c += '0'
print(c)