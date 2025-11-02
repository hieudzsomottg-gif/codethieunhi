#Bài toán rút gọn phân số
import math
while True:
    a = int(input("Nhập tử số là: "))
    b = int(input("Nhập mẫu số là: "))
    if b == 0:
        print("Lỗi cú pháp!")
    else:
        break
c = math.gcd(a,b)
tu_so = a / c 
mau_so = b / c
print(f"{int(tu_so)}/{int(mau_so)}")
