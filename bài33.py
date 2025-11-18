# Trò chơi đê nồ
day_so = list(map(int,input("Mời bạn nhập vào 5 chữ số: ").split()))
if len(day_so) != 5:
    print("Vui lòng nhập đúng 5 số!")
else:
    if len(day_so) == len(set(day_so)):
        print("Dãy số không có số nào trùng nhau")
    else:
        print("Dãy số có số trùng nhau")
