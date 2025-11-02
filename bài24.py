# Tìm số lượng chữ số của một số nguyên n
n = int(input("Nhập số nguyên n bất kì: "))
dem = 0
if n == 0:
    dem = 1
else:
    while n > 0:
        n // 10
        dem += 1
print(f"số lượng chữ số của số nguyên dương {n} là: {dem}")
