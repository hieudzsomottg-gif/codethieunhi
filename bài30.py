# in hình chữ nhật bằng dấu *
a = int(input("Nhập chiều dài hình chữ nhật là: "))
b = int(input("Nhập chiều rộng hình chữ nhật là: "))
for i in range(b):
    print("*" * a)
for i in range(b):
    if i == 0 or i == b - 1:
        print("*" * a)
    else:
        print("*" + " " * (a -2) + "*")
