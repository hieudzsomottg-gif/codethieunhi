# Tính tổng những số tự nhiê chia hết cho 3 và 5 từ 1 đến n
a = int(input("Nhập số tự nhiên a là: "))
b = int(input("Nhập số tự nhiên b là: "))
sum  = 0
for i in range(a,b+1):
    if i % 3 == 0 and i % 5 == 0:
        sum += i
        print(f"Tổng các số tự nhiên chia hết cho 3 và 5 từ 1 đến n là: {sum}")
