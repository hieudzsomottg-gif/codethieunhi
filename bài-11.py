# Tìm số lớn nhất trong 4 chữ số
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
d = float(input("Nhập số d: "))
if a > b > c > d:
    print(f"Số lớn nhất là: {a}")
elif b > a > c > d:
    print(f"Số lớn nhất là: {b}")
elif c > a > b > d:
    print(f"Số lớn nhất là: {c}")
else:
    print(f"Số lớn nhất là: {d}")
