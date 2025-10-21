# Tính bán kính hình tròn ngoại tiếp tam giác
a = float(input("Độ dài cạnh a là: "))
b = float(input("Độ dài cạnh b là: "))
c = float(input("Độ dài cạnh c là: "))
p = (a + b + c) / 2
print(f"Nửa chu vi tam giác là: {p}")
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"Diện tích tam giác là: {S}")
R = (a * b * c) / (4 * S)
print(f"Bán kính đường trong ngoại tiếp tam giác là: {R}")
