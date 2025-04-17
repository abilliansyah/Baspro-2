# 📌 Program Perkalian Matriks 5x5

ini adalah sebuah program yang menghitung hasil perkalian dua matriks berukuran 5x5

---

## 📌 Deskripsi

Program ini menghitung hasil perkalian matriks A dan B secara langsung (tanpa library tambahan), kemudian menyimpan hasilnya dalam matriks hasil dan menampilkannya ke layar.

---

## 📥 Input

Dua buah matriks 5x5:

- Matriks `A` berisi angka-angka yang telah ditentukan.
- Matriks `B` juga berisi angka-angka yang ditentukan.

Contoh:

```python
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

B = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
```

## 🔄 Proses Perkalian Matriks
Bagian ini adalah inti dari kode:

```python
for i in range(5):  # Loop untuk baris matriks A
    baris = []
    for j in range(5):  # Loop untuk kolom matriks B
        total = 0
        for k in range(5):  # Loop untuk elemen yang dikalikan dan dijumlahkan
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)
```
Penjelasan:
i: indeks baris pada matriks A
j: indeks kolom pada matriks B
k: indeks untuk elemen yang akan dikalikan (mengacu ke rumus perkalian matriks)

Setiap elemen di `hasil[i][j]` dihitung dengan rumus:

```python
hasil[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][4]*B[4][j]
```
## 🖨️ Menampilkan Hasil
Bagian ini mencetak setiap baris dari matriks hasil:
```python
for row in hasil:
    print(row)
```
## 🧮Output
Program akan menampilkan hasil perkalian matriks `A` dan `B`, dalam bentuk matriks 5x5.

output:

```python
[215, 230, 245, 260, 275]
[490, 530, 570, 610, 650]
[765, 830, 895, 960, 1025]
[1040, 1130, 1220, 1310, 1400]
[1315, 1430, 1545, 1660, 1775]
```


## 🧠 Singkatnya:
* Kode ini mengimplementasikan perkalian matriks 5x5 menggunakan nested loop.
* Prosesnya mengikuti aturan perkalian baris-kolom antara dua matriks.
* Hasil akhir adalah matriks baru berukuran 5x5 yang merupakan hasil perkalian A dan B.

