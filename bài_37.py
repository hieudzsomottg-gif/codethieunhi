# Đếm ước số nguyên n
import math
def dem_uoc(n):
    if n <= 0:
        return 0
    dem = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            dem += 1
            if i  != n // i:
                dem += 1
    return dem
n = int(input("Mời bạn nhập số nguyên n : "))
print(f"Số ước của {n} là: {dem_uoc(n)}")            
