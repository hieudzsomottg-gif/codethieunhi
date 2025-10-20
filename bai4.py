# Nhập số tiền a đồng.Tính xem có bao nhiêu tờ 5000 đồng,2000 đồng, 1000 đồng khi đổi
a = int(input("Nhập số tiền a là: "))
b = a // 5000
c = a % 5000
d = c // 2000
e = c % 2000
f = e // 1000
g = e % 1000
print(f"{b} {d} {f}")
