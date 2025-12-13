# kiểm tra một số nguyên có là số Pronic không
import math

while True:
    so = input("Mời bạn nhập số nguyên dương n là: ")
    if so.isdigit():
        n =int(so)
        if n > 0:
            break
        else:
            print("Yêu cầu bạn nhập số nguyên dương lớn hơn 0!")
    else:
        print("Yêu cầu bạn nhập đúng số hợp lệ!")
m = int(math.sqrt(n))
if m * (m + 1) == n:
    print(f"Số {n} là số Pronic")
else:
    print(f"Số {n} không phải là số Pronic!")
