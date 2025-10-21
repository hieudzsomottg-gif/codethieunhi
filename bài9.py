#kiểm tra tam giác
a = float(input("Số đo cạnh a là: "))
b = float(input("Số đo cạnh b là: "))
c = float(input("Số đo cạnh c là: "))
while a + b > c and a + c > b and b + c > a:
    print("Đây là hình tam giác")
    if a == b == c:
        print("Đây là tam giác đều")
    elif a == b or a == c or b == c:
        print("Đây là tam giác cân")
    elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c ==a*a):
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác thường")
    break
else:
    print("Đây không phải là tam giác") 
