# Xuất ra các số nguyên tố từ 1 đến N
a = int(input("Nhập số nguyên a là: "))
for i in range(2,a+1):
    snt = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            snt = False
            break
    if snt:
        print(i,end=" ")
