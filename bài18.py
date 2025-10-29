# Tính tổng trung bình cộng những số tự nhiên chia hết cho 3 và 5 từ 1 đến n
a = 1
b = int(input("Nhập số tự nhiên v là: "))
sum = 0
dem = 0
for i in range(a,b+1):
    if i % 3 == 0 and i % 5 == 0:
        dem += 1
        sum += i
        tbc = sum / dem
        print(f"Tổng trung bình cộng các số tự nhiên chia hết cho 3 và 5 là: {tbc}")
