#Nhập vào một số tiền a đồng. Tính số tờ 5000 đồng nhiều nhất khi đổi số tiền a và số tiền còn lại sau khi đổi nằm trên một dòng cách nhau một dấu cách
a = int(input("Nhập số tiền a : "))
b = a // 5000
c = a % 5000
print(f"Số tờ 5000 đồng nhiều nhất là: {b} tờ và tiền thừa còn lại là: {c} đồng")
