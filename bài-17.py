# Tính trung bình cộng những số tự nhiên chẵn từ 1 đến n
a = 1
b = int(input("Nhập số tự nhiên n là: "))
sum = 0
dem = 0
for i in range(a,b+1):
    if i % 2 == 0:
        dem += 1
        sum += i
        tbc = sum / dem
print(f"Tổng trung bình cộng những số chẵn từ 1 đến n là: {tbc}")
