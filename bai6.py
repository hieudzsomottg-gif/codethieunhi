#Tính  số bàn học sinh của 3 lớp biết rằng mỗi bàn ngồi ít nhất được 2 em học sinh và tính số bàn cần mua ít nhất
a = int(input("Số học sinh lớp 1 là: "))
b = int(input("Số học sinh lớp 2 là: "))
c = int(input("Số học sinh lớp 3 là: "))
d = (a + b + c) // 2 + 1
print(f"Số bàn học cần mua ít nhất là: {d} bàn")
