# Tính n giai thừa (n!)
import math
while True:
    so = input("Mời bạn nhập số nguyên dương n là: ")
    if so.isdigit():
        n = int(so)
        if n > 0:
            break
        else:
            print("Yêu cầu bạn nhập số nguyên dương n lớn hơn 0 !")
    else:
        print("Yêu cầu bạn nhập đúng số hợp lệ!")

giai_thua = 1
for i in range(1,n+1):
    giai_thua *= i
print(f"{i}! = {giai_thua}")
