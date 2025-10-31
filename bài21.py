# Tìm ước chung lớn nhất của hai số nguyên a và b
import math
a = int(input("Nhập số nguyên a là: "))
b = int(input("Nhập số nguyên b là: "))
ucln = math.gcd(a,b)
# gcd: là hàm tích hợp sẵn,nhanh và chuẩn xác khi tìm ước chung
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
