# สร้างไฟล์ compare_sorting.py
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        insert_index = i
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return arr

# ทดสอบ
test_data = [64, 34, 25, 12, 22, 11, 90, 5, 88, 45]

# Bubble Sort
arr1 = test_data.copy()
start = time.time()
bubble_sort(arr1)
print(f"Bubble Sort: {time.time() - start:.6f} วินาที")

# Selection Sort
arr2 = test_data.copy()
start = time.time()
selection_sort(arr2)
print(f"Selection Sort: {time.time() - start:.6f} วินาที")

# Insertion Sort
arr3 = test_data.copy()
start = time.time()
insertion_sort(arr3)
print(f"Insertion Sort: {time.time() - start:.6f} วินาที")