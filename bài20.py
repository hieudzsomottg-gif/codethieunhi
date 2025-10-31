# Đếm số nguyên chia hết cho 5 và in những sô nguyên chia hết cho 5 từ m đến n 
m = int(input("Nhập số nguyên m là: "))
n = int(input("Nhập số nguyên n là: "))
a = []
for i in range(m,n+1):
    if i % 5 == 0:
        a.append(i)
print(len(a),"-",*a)
