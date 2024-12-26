#############################################
# Nama Kelompok: SIGOOT
# Kelas       : S1-IF-09-05
# Anggota Kelompok:
# 1. 21102277 - Wifqi Wifakul Azmi
#############################################

import random # Untuk menghasilkan data acak.
import string # Untuk memilih karakter acak.
import time #  Untuk mengukur waktu eksekusi algoritma.
import tkinter as tk # Untuk membangun GUI aplikasi.
from tkinter import ttk, messagebox
from time import perf_counter
import matplotlib.pyplot as plt  # Untuk menggambar grafik hasil perbandingan.

# Fungsi untuk menghasilkan data acak
# Data berupa string dengan format: satu huruf dan dua digit angka
def generate_random_data(size):
    return [f"{random.choice(string.ascii_letters)}{random.randint(0, 99)}" for _ in range(size)]

# Bubble Sort
# Algoritma sorting sederhana yang membandingkan pasangan elemen berurutan dan menukarnya jika salah urutan
# Kompleksitas waktu: O(n^2) dalam kasus terburuk
def bubble_sort(arr):
    data = arr.copy()  # Salin array asli untuk menjaga integritas data input
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Quick Sort
# Algoritma sorting berbasis divide-and-conquer
# Menggunakan pivot untuk membagi array menjadi bagian kiri (elemen lebih kecil) dan kanan (elemen lebih besar)
# Kompleksitas waktu: O(n log n) dalam kasus rata-rata
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort
# Algoritma sorting berbasis divide-and-conquer
# Membagi array menjadi bagian kecil, menyortirnya, lalu menggabungkan kembali secara berurutan
# Kompleksitas waktu: O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Fungsi untuk memulai pengurutan dan menampilkan hasilnya di GUI
problem_sizes = []
bubble_times, quick_times, merge_times = [], [], []

def start_sorting():
    try:
        # Membaca ukuran masalah dan jumlah iterasi dari input pengguna
        problem_size = int(problem_size_var.get())
        if problem_size < 10:
            raise ValueError("Problem size harus >= 10.")
        iterations = int(iterations_var.get())

        # Menghasilkan data acak
        original_data = generate_random_data(problem_size)

        # Mengukur waktu Bubble Sort
        start_time = perf_counter()
        for _ in range(iterations):
            bubble_sort(original_data)
        bubble_time = ((perf_counter() - start_time) / iterations) * 1000  # Waktu rata-rata dalam ms

        # Mengukur waktu Quick Sort
        start_time = perf_counter()
        for _ in range(iterations):
            quick_sort(original_data)
        quick_time = ((perf_counter() - start_time) / iterations) * 1000  # Waktu rata-rata dalam ms

        # Mengukur waktu Merge Sort
        start_time = perf_counter()
        for _ in range(iterations):
            merge_sort(original_data)
        merge_time = ((perf_counter() - start_time) / iterations) * 1000  # Waktu rata-rata dalam ms

        # Menampilkan data sebelum dan sesudah pengurutan di listbox GUI
        bubble_listbox.delete(0, tk.END)
        quick_listbox.delete(0, tk.END)
        merge_listbox.delete(0, tk.END)
        before_listbox.delete(0, tk.END)

        for item in original_data:
            before_listbox.insert(tk.END, item)
        for item in bubble_sort(original_data):
            bubble_listbox.insert(tk.END, item)
        for item in quick_sort(original_data):
            quick_listbox.insert(tk.END, item)
        for item in merge_sort(original_data):
            merge_listbox.insert(tk.END, item)

        # Memasukkan hasil waktu eksekusi ke tabel
        result_table.insert("", tk.END, values=(problem_size, f"{bubble_time:.3f}", f"{merge_time:.3f}", f"{quick_time:.3f}"))

        # Menyimpan hasil untuk grafik
        problem_sizes.append(problem_size)
        bubble_times.append(bubble_time)
        quick_times.append(quick_time)
        merge_times.append(merge_time)

        # Jika sudah 10 ukuran data, tampilkan grafik
        if len(problem_sizes) >= 10:
            plot_graph()

    except ValueError as e:
        # Menampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("Error", str(e))

# Fungsi untuk membuat grafik laju kenaikan waktu eksekusi
def plot_graph():
    plt.figure(figsize=(10, 6))
    plt.plot(problem_sizes, bubble_times, label="Bubble Sort", marker="o")
    plt.plot(problem_sizes, quick_times, label="Quick Sort", marker="s")
    plt.plot(problem_sizes, merge_times, label="Merge Sort", marker="^")
    plt.title("Laju Kenaikan Waktu Eksekusi Sorting Algorithms")
    plt.xlabel("Ukuran Input (n)")
    plt.ylabel("Waktu Eksekusi (ms)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Membuat GUI menggunakan tkinter
root = tk.Tk()
root.title("Sorting Algorithm Comparison")

# Variabel untuk input ukuran masalah dan iterasi
problem_size_var = tk.StringVar(value="10")
iterations_var = tk.StringVar(value="100")

# Frame untuk input parameter
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Problem size:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame_input, textvariable=problem_size_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Iteration:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame_input, textvariable=iterations_var).grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_input, text="Start", command=start_sorting).grid(row=2, column=0, columnspan=2, pady=10)

# Frame untuk menampilkan list hasil sorting
frame_lists = tk.Frame(root)
frame_lists.pack()

before_listbox = tk.Listbox(frame_lists, height=15, width=15)
bubble_listbox = tk.Listbox(frame_lists, height=15, width=15)
quick_listbox = tk.Listbox(frame_lists, height=15, width=15)
merge_listbox = tk.Listbox(frame_lists, height=15, width=15)

before_listbox.grid(row=0, column=0, padx=5)
bubble_listbox.grid(row=0, column=1, padx=5)
quick_listbox.grid(row=0, column=2, padx=5)
merge_listbox.grid(row=0, column=3, padx=5)

tk.Label(frame_lists, text="Before").grid(row=1, column=0)
tk.Label(frame_lists, text="Bubble").grid(row=1, column=1)
tk.Label(frame_lists, text="Quick").grid(row=1, column=2)
tk.Label(frame_lists, text="Merge").grid(row=1, column=3)

# Frame untuk tabel hasil waktu eksekusi
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

columns = ("n", "Bubble (ms)", "Merge (ms)", "Quick (ms)")
result_table = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)

for col in columns:
    result_table.heading(col, text=col)
    result_table.column(col, anchor="center")

result_table.pack()

# Menjalankan aplikasi GUI
root.mainloop()

