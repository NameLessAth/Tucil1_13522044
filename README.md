# Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force
Tugas Kecil 1 IF2211 Strategi Algoritma 
Semester II tahun 2023/2024

M Athaullah Daffa Kusuma M (13522044)

## Deskripsi Singkat
Program ini merupakan tugas kecil 1 dari mata kuliah IF2211 Strategi Algoritma. Program ini berfungsi untuk mencari rute terpendek yang memberikan reward maksimal sesuai dengan ukuran buffer,  matriks, dan daftar sequences yang diberikan. Program ini juga dapat men-generate sebuah matriks dan sequences nya sesuai dengan beberapa aturan yang diinput oleh user.  

## Informasi Tambahan
Program dibuat dengan : Python 3.13.0a1<br />
IDE yang digunakan : Visual Studio Code dengan banyak extension lainnya<br />
Laporan dibuat dengan : Google Docs <br />
OS dari device yang digunakan : Windows

## Petunjuk Cara Menjalankan Program dan lainnya

### Cara Menjalankan Program
cukup menjalankan program main.py di dalam folder src
### Input melalu CLI
Cukup memasukkan input ke CLI sesuai format
### Input berupa File
Masukkan file txt yang hendak diuji ke dalam folder test yang telah disediakan, lalu input sesuai dengan instruksi lebih lanjut yang ada di dalam program.
### Output berupa File
Ketika program selesai dijalankan dan mendapat hasil, nantinya user akan ditanya apakah hendak menulis hasil di file txt. Jika iya, silahkan masukkan nama file txt. Jika file tersebut sudah ada di folder test/, maka file tersebut akan diwrite setelah isi dari file tersebut. Jika file tersebut tidak ada di folder test/, maka program akan membuat file baru dengan nama tersebut dan menulis hasil dari kalkulasi ke dalam file tersebut.  

## Input Format

### Input untuk program solver via file txt
buffer_size<br />
matrix_width matrix_height<br />
matrix<br />
number_of_sequences<br />
sequences_1<br />
sequences_1_reward<br />
sequences_2<br />
sequences_2_reward<br />
…<br />
sequences_n<br />
sequences_n_reward
### Input untuk program generator via CLI
number_of_unique_tokens<br />
list_of_token<br />
buffer_size<br />
matrix_width matrix_height<br />
number_of_sequences<br />
maximum_length_of_sequence

 
## Commit Messages

Untuk type mengikuti semantic berikut.

- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)
