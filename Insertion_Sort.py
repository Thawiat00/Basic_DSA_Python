# สร้างไฟล์ insertion_sort.py

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
print("ก่อนเรียง:", mylist)

n = len(mylist)
for i in range(1, n):
    current_value = mylist[i]  # เก็บค่าที่จะแทรก
    insert_index = i
    
    # เลื่อนค่าที่มากกว่าไปทางขวา
    for j in range(i-1, -1, -1):
        if mylist[j] > current_value:
            mylist[j+1] = mylist[j]  # เลื่อนไปทางขวา
            insert_index = j
        else:
            break  # หยุดเมื่อเจอตำแหน่งที่ถูก
    
    mylist[insert_index] = current_value  # ใส่ค่าเข้าไป
    print(f"รอบที่ {i}: {mylist}")

print("\nหลังเรียง:", mylist)