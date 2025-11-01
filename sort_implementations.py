
import random 
import time
import matplotlib.pyplot as plt


# Sorting Algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def measure_time(sort_func, arr):
    copied = arr.copy()
    start = time.time()
    sort_func(copied)
    end = time.time()
    return (end - start) # seconds

sizes = [50, 100, 200, 400, 500, 1000]

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

cases = {
    "Sorted Data": lambda n: list(range(n)),
    "Random Data": lambda n: random.sample(range(n*10), n),
    "Reverse Sorted Data": lambda n: list(range(n, 0, -1))
}


results = {case: {alg: [] for alg in algorithms} for case in cases}

# Run experiments
for size in sizes:
    for case_name, case_gen in cases.items():
        for alg_name, alg_func in algorithms.items():
            arr = case_gen(size) # generates array for each algorithm
            t = measure_time(alg_func, arr)
            results[case_name][alg_name].append(t)


# Plot Results + Save
for case_name in cases:
    plt.figure(figsize=(8,5))
    for alg_name in algorithms:
        plt.plot(sizes, results[case_name][alg_name], marker='o', label=alg_name)
    plt.title(f"Order of Growth - {case_name}")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time Taken (s)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{case_name.replace(' ', '_').lower()}.png") # save as PNG

plt.show()