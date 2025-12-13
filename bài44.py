# Kiểm tra một số nguyên có phải là số phong phú không!
import math
while True:
    so = input("Mời bạn nhập vào số nguyên dương n là: ")
    if so.isdigit():
        n = int(so)
        if n > 0:
            break
        else: 
            print("Yêu cầu bạn nhập số nguyên dương lớn hơn 0!")
    else:
        print("Yêu cầu bạn nhập đúng số hợp lệ!")
tong = 0
u = []
uoc = math.gcd(n)
for i in range(1,n):
    if n % i == 0:
        u.append(i)
        tong += i
if tong > n:
    print(f"Số {n} là số phong phú")
else:
    print(f"Số {n} không phải là số phong phú!")
