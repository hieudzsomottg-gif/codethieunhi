#Bài toán tính tiền taxi
a = float(input("Số km bạn đi được là: "))
if a <= 1:
    b = a * 12000
    print(f"Số tiền bạn phải trả là: {int(b)} đồng")
elif 2 <= a <= 30:
    c = a * 10000
    print(f"Số tiền bạn phải trả là: {int(c)} đồng")
elif a > 30:
    d = a * 8000
    print(f"Số tiền bạn phải trả là: {int(d)} đồng")
