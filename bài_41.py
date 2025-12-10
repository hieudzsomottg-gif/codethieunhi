# Ktra một số nguyên có là số đối xứng
n = int(input("Nhập vào một số nguyên dương: "))
    
if n <= 0 :
    print(f"Số {n} không có số đối xứng!")
else:
    reversed_n = n[::-1]   
if n == reversed_n:
    print(f"Số {n} là số đối xứng")
else:
    print(f"Số {n} không phải là số đối xứng!")
