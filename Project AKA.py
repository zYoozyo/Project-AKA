# HitungIterasi: Penghitung Iterasi Algoritma
# Muhammad Ragiel Prastyo 2311102183
# Wildan Maulana Zidan 2311102162

import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Implementasi algoritma Linear Search
def linear_search(arr, x):
    iterations = 0
    for i in range(len(arr)):
        iterations += 1
        if arr[i] == x:
            return i, iterations
    return -1, iterations

# Implementasi algoritma Binary Search
def binary_search(arr, x):
    iterations = 0
    l = 0
    r = len(arr) - 1
    while l <= r:
        iterations += 1
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid, iterations
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1, iterations

# Implementasi algoritma Bubble Sort
def bubble_sort(arr):
    iterations = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, iterations

# Grafik untuk menyimpan data
sizes = []
linear_iters = []
binary_iters = []
bubble_iters = []
linear_times = []
binary_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_iters, 'ro-', label='Linear Search')
    plt.plot(sizes, binary_iters, 'bo-', label='Binary Search')
    plt.plot(sizes, bubble_iters, 'go-', label='Bubble Sort')
    plt.title('Performance Comparison: Linear Search vs Binary Search vs Bubble Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Iterations')
    plt.grid(True)
    plt.legend()
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "Recursive Time (s)", "Iterative Time (s)"]
    for i in range(len(sizes)):
        table.add_row([
            sizes[i],
            f"{linear_times[i]:.15e}",
            f"{binary_times[i]:.15e}"
        ])
    print(table)

# Program utama
while True:
    try:
        size = int(input('Masukkan ukuran array (atau ketik -1 untuk keluar): '))
        if size == -1:
            print('Program selesai. Terima kasih!')
            break
        if size <= 0:
            print('Ukuran array harus lebih besar dari 0.')
            continue

        arr = list(range(size))
        value = int(input('Masukkan nilai yang ingin dicari: '))

        sizes.append(size)

        start_time = time.perf_counter()
        _, linear_iter = linear_search(arr, value)
        end_time = time.perf_counter()
        linear_times.append(end_time - start_time)
        linear_iters.append(linear_iter)

        start_time = time.perf_counter()
        _, binary_iter = binary_search(arr, value)
        end_time = time.perf_counter()
        binary_times.append(end_time - start_time)
        binary_iters.append(binary_iter)

        _, bubble_iter = bubble_sort(arr[:])
        bubble_iters.append(bubble_iter)

        print_execution_table()
        update_graph()

    except ValueError:
        print('Masukkan nilai yang valid!')