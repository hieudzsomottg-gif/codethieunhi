# Nguyễn Xuân Hiếu
while True:
    try:
        n = int(input("Nhập vào một số n nguyên dương là: "))
        if n < 0 :
            print("Bạn cần nhập số nguyên dương!")
    except ValueError:
        print("Nhập số chứ ko nhập chữ")
        
    else:
        break    
tong = 0 
for i in range(1,n+1):
    tong += i
if tong % 2 == 0:
    print(f"Tổng bằng {tong} là số chẵn")
elif tong % 2 == 1:
    print(f"Tổng bằng {tong} là số lẽ")
