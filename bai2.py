# Tính tổng hàng đơn vị và hàng chục 
a = int(input("Nhập số a : "))
b = int(input("Nhập số b : "))
sum = (a % 10) + (b // 10 % 10)
print(f"Tổng hàng đơn vị của {a} và hàng chục của {b} là: {sum}")
