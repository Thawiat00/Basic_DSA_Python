# Algorithm หาค่าต่ำสุดเอง
my_array = [7, 12, 9, 4, 11, 8]

minVal = my_array[0]  # ตั้งค่าเริ่มต้นเป็นตัวแรก

for i in my_array:
    if i < minVal:
        minVal = i

print('ค่าต่ำสุด:', minVal)