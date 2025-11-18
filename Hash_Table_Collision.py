# Step 1: สร้าง list ว่าง
#my_list = [None] * 10

# Step 2: สร้าง hash function
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)  # Unicode ของตัวอักษร
    return sum_of_chars % 10       # คืนค่า 0-9

# ใช้ Chaining - แต่ละ bucket เป็น list
my_list = [[] for _ in range(10)]

def add(name):
    index = hash_function(name)
    my_list[index].append(name)

def contains(name):
    index = hash_function(name)
    return name in my_list[index]

# เพิ่มข้อมูล
add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Stuart')  # จะ collision กับ Lisa

print(my_list)