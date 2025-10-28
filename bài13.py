# In ra các chữ số lẻ có trong 8 chữ số
while True:
    a = int(input("Nhập số a có 8 chữ số là: "))
    if len(str(a)) == 8:
        break
    else:
        print("Bạn cần nhập số có 8 chữ số")
for i in range(10**7,10**8):
    if a == i:
        b = str(a)
        for j in b:
            if int(j) % 2 != 0:
                print(f"{j}", end="")
        else:
            print("Số bạn nhập không có số lẻ nào")            
        break
