# Đánh giá kết quả theo học tập theo tổng điểm
i = float(input("Nhập số điểm học tập của bạn : "))
if i >= 80:
    print("Loại B")
    if i >= 90:
        print("Xuất sắc")
    elif 80 <= i < 90:
        print("Giỏi")
elif 50 <= i < 80:
    print("Loại B")
    if i >= 65:
        print("Khá")
    elif 50 <= i < 65:
        print("Trung bình")
else:
    print("Loại C")
    if i >= 35:
        print("Yếu")
    else:
        print("Quá ngu!")
