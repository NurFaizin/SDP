<!---
Author: Klanjabrik (klanjabrik@sebangsa.com)
Created: June 2nd, 2015

Gunakan markdown viewer untuk membaca tugas ini
-->

# Tugas 1 (Individu)
Lobsters (https://lobste.rs/) adalah mesin agregasi tautan (link-aggregation) dengan fokus pada teknologi.

Pada tugas pertama ini, Anda tidak akan membuat program Lobsters melainkan Anda akan ditugaskan untuk mempelajari website Lobsters kemudian membuat daftar _endpoint_ yang dibutuhkan untuk membuat sistem Lobsters.

Masing-masing _endpoint_ memiliki dokumentasi yang lengkap dan ditulis menggunakan syntax markdown. Lihat contoh dokumentasi pada file doc_example.MD


# Tugas 2 (Tim)
Membuat aplikasi group chat dengan mengimplementasikan WebSocket.

## Definisi
Aplikasi memiliki 2 entitas, yaitu:
- Pengguna
- Grup

## Requirements
1. Pengguna bisa membuat grup yang disebut dengan pemilik grup (_group owner_).
2. Pengguna bisa bergabung pada grup apapun yang disebut dengan anggota grup.
3. Setiap anggota grup bisa mengirimkan pesan yang akan diterima oleh setiap anggotanya.
4. _Group owner_ bisa mengeluarkan anggota grup, sehingga anggota tersebut tidak akan mendapatkan pesan dari grup tersebut.
5. Anggota grup bisa meninggalkan grup yang dimaksud, sehingga tidak akan lagi mendapatkan pesan dari grup tersebut.
6. Ada 2 jenis grup, yaitu **Grup Umum** dan **Grup Tertutup**. Untuk bergabung dengan **Grup Umum** tidak perlu memasukkan kode rahasia, sedangkan untuk bergabung dengan **Grup Tertutup** harus memasukkan kode rahasia.
7. Kode Rahasia di-generate secara otomatis ketika grup baru dibuat.

Jika mengerjakan poin nomor 6 dan 7 akan menjadi nilai plus.

## Tools
Perangkat lunak pendukung bisa menggunakan apa saja asal tetap menggunakan Python sebagai Application.

Untuk memudahkan Anda bisa menggunakan perangkat lunak pendukung di bawah ini:
- WAMP Application router menggunakan Crossbar.io (http://crossbar.io/docs/Getting-started-with-Python/) 
- WAMP Client Library bisa menggunakan Autobahn|JS (http://autobahn.ws/js/) atau Autobahn|Python (http://autobahn.ws/python/)


