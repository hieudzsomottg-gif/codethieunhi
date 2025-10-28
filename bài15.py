# Tìm chữ số lớn nhất và chữ số nhỏ nhất của một số có 8 chữ số
while True:
    a = (input("Nhập số a có 8 chữ số là: "))
    if len(str(a)) == 8:
        break
    else:
        print("Bạn cần nhập số có 8 chữ số")
lon_nhat = max(int(i) for i in str(a))
nho_nhat = min(int(i) for i in str(a))
print(f"Chữ số lớn nhất trong 8 chữ số là: {lon_nhat}")
print(f"Chữ số nhỏ nhất trong 8 chữ số là: {nho_nhat}")
