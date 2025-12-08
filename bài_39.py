# Kiểm tra một số nguyên có là số hoàn hảo
import math

while True:
    so_str =input("Mời bạn nhập một số nguyên dương là: ")
    if so_str.isdigit():
        so = int(so_str)
        if so > 0:
            break
        else:
            print("Mời bạn nhập một số nguyên dương: ")
    else:
        print("Vui lòng nhập một số hợp lệ!")

tong = 0
for i in range(1,so):
    if so % i == 0:
        tong += i

if tong == so:
    print(f"Số {so} là số hoàn hảo!")
else:
    print(f"Số {so} là số không hoàn hảo!")
