mylist = [7, 3, 9, 12, 11]
print("ก่อนเรียง:", mylist)

n = len(mylist)
for i in range(n-1):
    swapped = False  # ตรวจว่ามีการสลับหรือไม่
    
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            swapped = True
    
    # ถ้าไม่มีการสลับเลย = เรียงเสร็จแล้ว
    if not swapped:
        print(f"หยุดที่รอบที่ {i+1} (เรียงเสร็จแล้ว)")
        break

print("หลังเรียง:", mylist)