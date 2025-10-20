i = int(input("Nhập số giây là: "))
h = i // 3600
p = (i - h * 3600) // 60
g = (i - h * 3600) - (p * 60)
print(f"{h}:{p}:{g}")
