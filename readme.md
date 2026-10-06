MarkItDown Converter untuk Claude Web

Aplikasi sederhana ini berfungsi untuk mengonversi berbagai macam file berukuran besar menjadi teks murni berformat Markdown (.md).

Format .md ini sangat ringan, bersih, dan bebas dari kode atau format tersembunyi. Hal ini sangat menghemat penggunaan token dan membuat respons AI jauh lebih akurat saat file hasil konversinya diunggah ke Claude Web.

📂 Format File yang Didukung

Anda bisa mengonversi file dengan ekstensi berikut:

- Dokumen & Bacaan: .pdf, .docx (Word), .html / .htm

- Data & Tabel (Spreadsheet): .xlsx (Excel), .csv, .json

- Presentasi: .pptx (PowerPoint)

- Media (Gambar & Audio): .jpg, .jpeg, .png, .mp3, .wav

- Arsip: .zip (Membaca dan mengekstrak teks dari file yang didukung di dalamnya)

💡 Tips: Saat jendela pencarian file terbuka, pilih opsi "Semua File (.)" atau "All Files" di pojok kanan bawah jika ekstensi file yang ingin Anda pilih (misalnya gambar atau audio) tidak muncul di daftar default.

🚀 Cara Penggunaan Sehari-hari

Jika Anda baru saja menyalakan Mac atau membuka ulang aplikasi VS Code, ikuti 3 langkah mudah ini untuk menjalankan aplikasinya:

1. Buka Folder & Terminal

- Pastikan Anda sudah membuka folder proyek converter_markitdown di aplikasi VS Code.

Buka panel Terminal di bagian bawah layar (Anda bisa menggunakan shortcut keyboard Cmd + J).

2. Aktifkan Virtual Environment (Wajib!)

Agar sistem bisa memanggil library MarkItDown yang sudah diinstal sebelumnya, jalankan perintah ini di Terminal lalu tekan Enter:

- source .venv/bin/activate


(Cek keberhasilannya: Akan muncul teks (.venv) di bagian paling depan baris terminal Anda).

3. Jalankan Aplikasi

Setelah virtual environment aktif, jalankan program dengan mengetik perintah ini lalu tekan Enter:

- python converter_markitdown.py


Sebuah jendela aplikasi kecil akan terbuka di tengah layar. Anda tinggal mengklik tombol "Pilih File & Convert", pilih file yang diinginkan, dan file .md akan otomatis terbuat di folder yang sama, siap untuk diunggah ke chat Claude!