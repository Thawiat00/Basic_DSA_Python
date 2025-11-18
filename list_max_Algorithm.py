# ลองทำเอง: หาค่าสูงสุด
my_array = [7, 12, 9, 4, 11, 8]
maxVal = my_array[0]

for i in my_array:
    if i > maxVal:
        maxVal = i

print('ค่าสูงสุด:', maxVal)