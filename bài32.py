# So sánh năm sinh ai lớn hơn
while True:
    try:
        a = input("Nhập ngày (Theo định dạng dd/mm/yyyy): ")
        b = input("Nhập ngày (Theo định dạng dd/mm/yyyy): ")
    except ValueError:
        print("Nhập số chứ ko nhập chữ")
    else:
        break
if a > b :
    print("Tuổi An lớn hơn")
else:
    print("Tuổi An bé hơn")
