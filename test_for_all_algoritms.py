import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def radix_sort(arr):
    if not arr:
        return
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

sizes = [100, 500, 1000, 5000]
results = {
    "Insertion Sort": [],
    "Bubble Sort": [],
    "Selection Sort": [],
    "Quick Sort": [],
    "Merge Sort": [],
    "Radix Sort": []
}

inplace_algos = ["Insertion Sort", "Bubble Sort", "Selection Sort", "Merge Sort", "Radix Sort"]

for size in sizes:
    base = [random.randint(1, 10000) for _ in range(size)]
    for name, func in [
        ("Insertion Sort", insertion_sort),
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
        ("Radix Sort", radix_sort),
    ]:
        arr = base.copy()
        start = time.time()
        if name in inplace_algos:
            func(arr)
        else:
            func(arr) 
        end = time.time()
        results[name].append(end - start)

for name, times in results.items():
    plt.plot(sizes, times, label=name)

plt.title("Порівняння часу виконання алгоритмів сортування")
plt.xlabel("Кількість елементів")
plt.ylabel("Час (секунди)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
