n = int(input())
assert 1<=n<=9999999
a = [str(i) for i in range(1,n+1)]
b = ''.join(a)
print(len(b))

