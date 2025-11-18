# ========================================
# Part 19: MERGE SORT (แบ่งแล้วรวม)
# ========================================

def mergeSort(arr, depth=0):
    """
    Merge Sort (แบบ Recursion):
    1. แบ่งครึ่งจนเหลือ 1 ตัว
    2. รวมกลับโดยเรียงเล็ก → ใหญ่
    """
    indent = "  " * depth
    
    # Base case: array มีตัวเดียว
    if len(arr) <= 1:
        print(f"{indent}↩️  Return: {arr}")
        return arr
    
    # แบ่งครึ่ง
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    
    print(f"{indent}📂 Split: {arr}")
    print(f"{indent}   ├─ Left:  {leftHalf}")
    print(f"{indent}   └─ Right: {rightHalf}")
    
    # Recursion
    sortedLeft = mergeSort(leftHalf, depth + 1)
    sortedRight = mergeSort(rightHalf, depth + 1)
    
    # Merge
    result = merge(sortedLeft, sortedRight)
    print(f"{indent}🔀 Merge: {sortedLeft} + {sortedRight} = {result}")
    
    return result


def merge(left, right):
    """
    รวม 2 arrays ที่เรียงแล้ว
    """
    result = []
    i = j = 0
    
    # เปรียบเทียบทีละตัว
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # เพิ่มที่เหลือ
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# ========================================
# ทดสอบโค้ด
# ========================================

# ตัวอย่างที่ 1: พื้นฐาน
print("=" * 70)
print("ตัวอย่างที่ 1: Merge Sort พื้นฐาน")
print("=" * 70)
mylist1 = [12, 8, 9, 3, 11, 5, 4]
print(f"Original: {mylist1}\n")
result1 = mergeSort(mylist1)
print(f"\n✅ Final Result: {result1}")

# ตัวอย่างที่ 2: มีเลขลบและทศนิยม
print("\n\n" + "=" * 70)
print("ตัวอย่างที่ 2: มีเลขลบและทศนิยม")
print("=" * 70)
mylist2 = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(f"Original: {mylist2}\n")
result2 = mergeSort(mylist2)
print(f"\n✅ Final Result: {result2}")

# ตัวอย่างที่ 3: เรียงอยู่แล้ว
print("\n\n" + "=" * 70)
print("ตัวอย่างที่ 3: Array ที่เรียงอยู่แล้ว")
print("=" * 70)
mylist3 = [1, 2, 3, 4, 5]
print(f"Original: {mylist3}\n")
result3 = mergeSort(mylist3)
print(f"\n✅ Final Result: {result3}")

print("\n" + "=" * 70)
print("📚 สรุป Merge Sort:")
print("=" * 70)
print("✅ ใช้ได้กับ: ตัวเลขทุกประเภท (int, float, ลบ)")
print("🎯 วิธีการ: แบ่งครึ่ง → เรียง → รวม")
print("⚡ Stable Sort: รักษาลำดับค่าเดียวกัน")
print("📊 Time Complexity: O(n log n) - สม่ำเสมอทุกกรณี")
print("💾 Space Complexity: O(n) - ต้องการพื้นที่เพิ่ม")