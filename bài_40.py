# Kiểm tra một số nguyên có là số tam giác
while True:
    so = input("Mời nhập số nguyên dương là: ")
    if so.isdigit():
        n = int(so)
        if n > 0:
            break
        else:
            print("Mởi nhập số nguyên dương là: ")
    else:
        print("Yêu cầu bạn nhập đúng số hợp lệ!")

tong = 0 
i = 1
while tong < n:
    tong += i
    i += 1

if tong == n:
    print(f"Số {n} là số tam giác")
else:
    print(f"Số {so} không phải là số tam giác")
