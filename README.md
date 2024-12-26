<h1 align="center"> TUGAS BESAR STRATEGI ALGORITMA </h1>

<p align="center">
  <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png">
</p>

<p align="center">
  <a href="https://travis-ci.org/python/cpython">
    <img src="https://travis-ci.org/python/cpython.svg" alt="Build Status">
  


## **Program Perbandingan Algoritma Sorting**

### **Deskripsi**
Program ini dirancang untuk membandingkan performa tiga algoritma sorting yang berbeda: **Bubble Sort**, **Quick Sort**, dan **Merge Sort**. Program mengukur waktu eksekusi (running time) masing-masing algoritma dengan berbagai ukuran data input dan menampilkan hasilnya dalam bentuk tabel dan grafik.

---

### **Fitur Utama**
1. **Pengujian Algoritma**:
   - Mengukur waktu eksekusi **Bubble Sort**, **Quick Sort**, dan **Merge Sort**.
   - Membandingkan hasil untuk berbagai ukuran input (n).
   
2. **Antarmuka GUI (Graphical User Interface)**:
   - Input ukuran data (problem size) dan jumlah iterasi.
   - Menampilkan data sebelum dan sesudah sorting.
   - Tabel perbandingan waktu eksekusi.

3. **Visualisasi Grafik**:
   - Membuat grafik perbandingan waktu eksekusi untuk ketiga algoritma berdasarkan ukuran input.

---

### **Cara Kerja Program**
1. **Input Data**:
   - Pengguna memasukkan ukuran masalah (problem size) dan jumlah iterasi melalui GUI.
   - Program menghasilkan data acak berbentuk string dengan format: satu huruf dan dua digit angka (contoh: A23, B45).

2. **Sorting**:
   - Data yang sama diuji menggunakan tiga algoritma sorting.
   - Setiap algoritma menghitung waktu eksekusi rata-rata berdasarkan jumlah iterasi yang diberikan.

3. **Output**:
   - Menampilkan data awal (sebelum sorting) dan hasil sorting.
   - Menampilkan tabel hasil perbandingan waktu eksekusi.
   - Menampilkan grafik performa algoritma berdasarkan ukuran input.

---

### **Pengujian**
- **Data Uji**:
  - Data berupa array string acak.
  - Data yang sama digunakan untuk semua algoritma dalam setiap pengujian.
  
- **Metodologi**:
  - Program diuji pada berbagai ukuran input data (n).
  - Jumlah iterasi ditingkatkan seiring dengan bertambahnya ukuran input untuk mendapatkan hasil yang akurat.

- **Hasil**:
  - Waktu eksekusi dicatat dalam tabel untuk setiap algoritma dan ukuran input.

---

### **Hasil Pengujian dan Analisis**
#### **Tabel Perbandingan Waktu Eksekusi**:
| No  | Problem Size (n) | Iteration | Bubble Sort (ms) | Quick Sort (ms) | Merge Sort (ms) |
|-----|------------------|-----------|------------------|-----------------|-----------------|
| 1   | 10               | 100       | 0.013            | 0.014           | 0.018           |
| 2   | 20               | 200       | 0.031            | 0.011           | 0.015           |
| 3   | 30               | 300       | 0.040            | 0.017           | 0.019           |
| 4   | 40               | 400       | 0.050            | 0.026           | 0.025           |
| 5   | 50               | 500       | 0.075            | 0.035           | 0.038           |
| 6   | 60               | 600       | 0.107            | 0.043           | 0.044           |
| 7   | 70               | 700       | 0.141            | 0.052           | 0.051           |
| 8   | 80               | 800       | 0.181            | 0.062           | 0.066           |
| 9   | 90               | 900       | 0.225            | 0.071           | 0.073           |
| 10  | 100              | 1000      | 0.264            | 0.078           | 0.080           |

#### **Kesimpulan**:
- **Quick Sort** dan **Merge Sort** jauh lebih cepat dibandingkan dengan **Bubble Sort**, terutama pada ukuran data yang lebih besar.
- **Quick Sort** sedikit lebih cepat dibandingkan **Merge Sort**, meskipun perbedaannya tidak signifikan.
- **Bubble Sort** tidak efisien untuk dataset besar karena kompleksitasnya yang **O(n²)**.
- **Quick Sort** adalah algoritma terbaik di antara ketiganya untuk pengujian ini, karena memiliki waktu eksekusi lebih cepat dan kompleksitas **O(n log n)**.

---

### **Cara Menjalankan Program**
1. Pastikan Python telah diinstal pada komputer Anda.
2. Instal pustaka tambahan yang diperlukan:
   ```bash
   pip install matplotlib
   ```
3. Jalankan program dengan perintah:
   ```bash
   python nama_file_program.py
   ```
4. Masukkan ukuran data dan iterasi pada GUI untuk memulai pengujian.

---



