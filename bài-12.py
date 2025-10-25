# Kiểm tra ba số cón là 3 cạnh của 1 tam giác hay không và tính chu vui,diện tích tam giác đó
a = float(input("Số đo cạnh a là: "))
b = float(input("Số đo cạnh b là: "))
c = float(input("Số đo cạnh c là: "))
while a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác")
    chuvi = a + b + c
    print(f"Chu vi tam giác là: {chuvi} m")
    nuachuvi = chuvi / 2
    print(f"Nửa chu vi hình tam giác là: {nuachuvi} m")
    dientich = (nuachuvi * (nuachuvi - a) * (nuachuvi - b) * (nuachuvi - c)) ** 0.5
    print(f"Diện tích tam giác là: {dientich} m²")
    break
else: 
    print("Đây không phải là tam giác")
