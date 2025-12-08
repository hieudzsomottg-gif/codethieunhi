# Kiểm tra số nguyên tố <333
import math

while True:
    so_str = input("Mời bạn nhập một số nguyên dương: ")
    if so_str.isdigit():
        so = int(so_str)
        if so > 0 :
            break
        else:
            print("Vui lòng nhập số nguyên dương lớn hơn 0!")
    else:
        print("Vui lòng nhập một số hợp lệ!")

so_nguyen_to = True
if so <= 1:
    so_nguyen_to = False
else:
    for i in range(2,so):
        if so % i == 0:
            so_nguyen_to = False
            break

if so_nguyen_to:
    print(f"Số {so} là số nguyên tố")
else:
    print(f"Số {so} không phải là số nguyên tố")  
