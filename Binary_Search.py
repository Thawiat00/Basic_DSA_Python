# =====================================================
# แบบฝึกหัดที่ 3: Binary Search
# =====================================================
print("\n\n📝 แบบฝึกหัดที่ 3: Binary Search - ค้นหาเลขหน้าหนังสือ")
print("-" * 70)
print("""
โจทย์: หนังสือมีเลขหน้า (sorted):
pages = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

ให้:
1. ใช้ Binary Search หาว่าหน้า 25 อยู่ที่ index ไหน
2. หาว่าหน้า 33 มีในหนังสือหรือไม่
3. หาหน้าแรกที่มากกว่าหรือเท่ากับ 32
""")

print("\n💡 เฉลย:")

pages = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

def binary_search_simple(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def find_first_greater_or_equal(arr, target):
    """หาตัวแรกที่ >= target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] >= target:
            result = mid
            right = mid - 1  # ลองหาทางซ้ายต่อ
        else:
            left = mid + 1
    
    return result

# 1. หาหน้า 25
result1 = binary_search_simple(pages, 25)
print(f"1. หน้า 25 อยู่ที่ index: {result1}")

# 2. หาหน้า 33
result2 = binary_search_simple(pages, 33)
print(f"2. หน้า 33 {'มี' if result2 != -1 else 'ไม่มี'}ในหนังสือ")

# 3. หาหน้าแรกที่ >= 32
result3 = find_first_greater_or_equal(pages, 32)
if result3 != -1:
    print(f"3. หน้าแรกที่ >= 32 คือหน้า {pages[result3]} (index {result3})")
