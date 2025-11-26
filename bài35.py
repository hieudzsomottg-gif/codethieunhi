m,n,k = list(map(int,input("Nhập ba số nguyên m,n,k là: ").split()))
c = []
for i in range(m,n+1,k):
    if i < n:
        c.append(i)
print(c,end=" ")
