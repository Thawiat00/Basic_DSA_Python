# สร้างไฟล์ bubble_sort.py

mylist = [64, 34, 25, 12, 22, 11, 90, 5]
print("ก่อนเรียง:", mylist)

n = len(mylist)
for i in range(n-1):
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            # สลับค่า
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print("หลังเรียง:", mylist)