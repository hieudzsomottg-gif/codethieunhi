# Tính số tháng gửi tiền tiết kiệm để được số tiền n
a = float(input("Nhập số tiền bạn đang có : "))
b = float(input("Nhập số tiền món đồ bạn cần mua: "))
t = 0
if a >= b:
    print("Số tiền bạn đã nhập đủ tiền mua món bạn cần")
else:
    while a < b:
        t += 1
        tong = a + (a * 0.02)
    print(f"Sau {t} tháng gửi số tiền của bạn là: {tong}")
