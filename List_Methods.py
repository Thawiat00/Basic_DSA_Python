# ทดลอง append และ sort
x = [9, 12, 7, 4, 11]
print("List เดิม:", x)

# เพิ่มตัวเลข 8
x.append(8)
print("หลัง append(8):", x)

# เรียงลำดับจากน้อยไปมาก
x.sort()
print("หลัง sort():", x)

# เรียงจากมากไปน้อย
x.sort(reverse=True)
print("เรียงจากมากไปน้อย:", x)