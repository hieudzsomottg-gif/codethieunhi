# kiểm tra số kì ảo!!
while True:
    so = input("Mời bạn nhập số nguyên dương n là: ")
    if so.isdigit():
        n = int(so)
        if n > 0:
            break
        else:
            print("Yêu cầu bạn nhập số nguyên dương lớn hơn 0!")
    else:
        print("Yêu cầu bạn nhập đúng số hợp lệ!")

        
k = len(so)
so_ki_ao = True
for i in range(1,k+1):
    so_con = int(so[:i])
    if so_con % i != 0:
        so_ki_ao = False
        break
if so_ki_ao:
    print(f"Số {n} là số kì ảo")
else:
    print(f"Số {n} không phải là số kì ảo")
