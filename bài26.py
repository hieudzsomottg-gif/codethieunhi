# Tính tổng các chữ số nguyên của một số nguyên n
a = int(input("Mời bạn nhập số nguyên n: "))
tong = 0 
a = abs(a)
while a > 0:
        chu_so = a % 10
        tong += chu_so
        a //= 10
print(tong)
