MarkItDown Converter

Aplikasi sederhana ini berfungsi untuk mengonversi berbagai macam file berukuran besar menjadi teks murni berformat Markdown (.md).

Format .md ini sangat ringan, bersih, dan bebas dari kode atau format tersembunyi. Hal ini sangat menghemat penggunaan token dan membuat respons AI jauh lebih akurat saat file hasil konversinya diunggah ke Claude Web.

📂 Format File yang Didukung

Anda bisa mengonversi file dengan ekstensi berikut:

Dokumen & Bacaan: .pdf, .docx (Word), .html / .htm

Data & Tabel (Spreadsheet): .xlsx (Excel), .csv, .json

Presentasi: .pptx (PowerPoint)

Media (Gambar & Audio): .jpg, .jpeg, .png, .mp3, .wav

Arsip: .zip (Membaca dan mengekstrak teks dari file yang didukung di dalamnya)

💡 Tips: Saat jendela pencarian file terbuka, pilih opsi "Semua File (.)" atau "All Files" di pojok kanan bawah jika ekstensi file yang ingin Anda pilih (misalnya gambar atau audio) tidak muncul di daftar default.

🚀 Cara Penggunaan

Aplikasi ini memiliki dua mode yang bisa Anda pilih sesuai kebutuhan: Mode Desktop untuk penggunaan lokal di Mac/PC, dan Mode Web UI untuk diakses melalui server (seperti LXC Proxmox).

OPSI 1: Mode Desktop (Penggunaan Lokal di Mac)

Gunakan mode ini jika Anda ingin menjalankan aplikasi dengan tampilan pop-up sederhana di komputer Anda.

1. Buka Folder & Terminal
Pastikan Anda sudah membuka folder proyek converter_markitdown di aplikasi VS Code. Buka panel Terminal di bagian bawah layar (Anda bisa menggunakan shortcut keyboard Cmd + J).

2. Aktifkan Virtual Environment (Wajib!)
Agar sistem bisa memanggil library MarkItDown yang sudah diinstal sebelumnya, jalankan perintah ini di Terminal lalu tekan Enter:

source .venv/bin/activate


(Cek keberhasilannya: Akan muncul teks (.venv) di bagian paling depan baris terminal Anda).

3. Jalankan Aplikasi
Setelah virtual environment aktif, jalankan program desktop dengan mengetik perintah ini lalu tekan Enter:

python converter_markitdown.py


Sebuah jendela aplikasi kecil akan terbuka di tengah layar. Anda tinggal mengklik tombol "Pilih File & Convert", pilih file yang diinginkan, dan file .md akan otomatis terbuat di folder yang sama.

OPSI 2: Mode Web UI (Untuk Server / LXC)

Gunakan mode ini jika program berjalan di server, sehingga konversi bisa dilakukan dari perangkat mana saja (Mac, Windows, HP) hanya bermodalkan browser.

1. Masuk Folder & Aktifkan Virtual Environment
Buka terminal/console server Anda, masuk ke folder proyek, dan aktifkan environment:

cd converter_markitdown
source .venv/bin/activate


2. Jalankan Aplikasi Web
Jalankan file khusus versi web dengan mengetik perintah berikut:

streamlit run web_app.py


3. Akses via Browser
Buka browser di perangkat apa pun yang terhubung dalam satu jaringan, lalu ketik alamat IP server Anda diikuti port 8501. Contoh:
http://192.168.18.xxx:8501

(Catatan: Jika Anda sudah menyetel Systemd Service di server Linux, langkah di atas tidak perlu dilakukan lagi karena Web UI akan otomatis menyala di latar belakang 24 jam).