# Mảng con kì diệu
while True:
    a = int(input("Dòng thứ 1 chứa số nguyên n là: "))
    b = list(map(int,input("Mời bạn nhập 8 chữ số: ").split()))
    if len(b) != 8:
        print("Yêu cầu bạn nhập 8 chữ số!")
    else:
        if len(b) == len(set(b)):
            print("Không có số nào trùng nhau cả!")
        else:
            break
