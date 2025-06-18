a=[1,2,3]
b=[4,5,6]
c=tuple(a[i//2] if i%2==0 else b[i//2] for i in range(6))
print(c)