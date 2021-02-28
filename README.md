# course-prerequisite-sorter

## Pengurutan Pengambilan Kuliah dengan Prerequisite Persemester dengan Memanfaatkan Pendekatan Topological Sort dengan Algoritma Decrease and Conquer

Anda bingung mau ngambil kuliah apa dulu karena kebanyakan prerequisite? Gampang! Dengan menggunakan program ini, Anda gaperlu repot-repot mengurutkan dengan manual.

## Author

- Rezda Abdullah F
- 13519194 | K4 STIMA IF2211

## Penjelasan Singkat Algoritma Decrease and Conquer yang Digunakan

Algoritma Decrease and Conquer yang digunakan memanfaatkan rekursi. Langkah umumnya adalab sbb.
1. Pertama-tama dipilih simpul pada graf yang tidak memiliki simpul yang masuk.
2. Simpul tersebut dikeluarkan dari graf dan dimasukkan ke graf kosong.
3. Graf kosong yang baru terisi tadi akan dikonkatenasi dengan graf baru lainnya yang merupakan hasil rekursi dari graf lama yang sudah dihapus simpulnya pada nomor satu.
4. Luaran merupakan graf yang sudah terurut berdasarkan Topological Sort.
5. Penghapusan simpul dari graf merupakan **decrease**, sedangkan konkatenasi simpul-simpul menjadi graf baru merupakan **conquer**.

# Program

### Contoh isi Fail

[nama kuliah][, prerequsite1] [, prerequsite2].

```
IF2121.
IF2124, IF2120, IF2110.
IF2110.
IF2220, IF2120, MA1101, MA1201.
IF2211.
IF3170, IF2121, IF2124, IF2220, IF2211.
MA1101.
MA1201.
IF2120.

```

### Cara menjalankan

1. Pastikan Python3 sudah terinstall
2. Unduh repositori ini
3. Buka terminal dan arahkan ke folder **src**. Lalu jalankan perintah berikut:

```
python3 "13519194-main.py"
```

4. Masukkan nama fail yang sudah dibuat dan foldernya jika ada
5. Selesai

Penting:

Fail **13519194-main.py**, **13519194-program.py**, **13519194-util.py** merupakan modifikasi kecil dari fail **original/main.py**, **original/program.py**, **original/util.py**.
Hal ini dilakukan karena teknis pengumpulan yang mengharuskan nama fail dimulai dari NIM, sedangkan Python tidak membolehkan import package dengan fail yang dimulai dari angka.
Sehingga, fail-fail yang dilampirkan pada laporan (**doc/13519194.pdf**) merupakan fail yang ada di folder **original**, sedangkan untuk testing dapat menjalankan fail yang diawali oleh NIM.
Tetapi, jika ingin menjalankan fail original, cukup jalankan dengan perintah **python3 main.py** saja.

### Contoh Luaran

![](https://image.prntscr.com/image/2Hsoi0FURc25DdoZmJD1Ig.png)
