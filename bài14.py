#Tính tổng các số chẵn trong 8 chữ số
while True:
    i = int(input("Nhập số có 8 chữ số: "))
    if len(str(i)) == 8:
        break
    else:
        print("Bạn cần nhập số có 8 chữ số")
sum = 0
for j in str(i):
    if int(j) % 2 == 0:
        sum += int(j)
print(f"Tổng các số chẵn trong 8 chữ số là: {sum}")
if sum == 0:
    print("Số bạn nhập không có số chẵn nào")
