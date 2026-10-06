import os
import tkinter as tk
from tkinter import filedialog, messagebox
from markitdown import MarkItDown

def jalankan_konversi():
    # Inisialisasi engine MarkItDown
    md = MarkItDown()
    
    # Membuka jendela pemilihan file (bisa pilih lebih dari 1 file)
    file_paths = filedialog.askopenfilenames(
        title="Pilih File (PDF, Word, PPT, Excel, dll)",
        filetypes=[
            ("Semua File", "*.*"),
            ("PDF Documents", "*.pdf"),
            ("Word Documents", "*.docx"),
            ("PowerPoint", "*.pptx"),
            ("Excel", "*.xlsx")
        ]
    )
    
    if not file_paths:
        return # Batal jika tidak ada file yang dipilih
    
    sukses = 0
    gagal = 0
    
    # Proses konversi untuk setiap file yang dipilih
    for path in file_paths:
        try:
            # Melakukan konversi
            hasil = md.convert(path)
            
            # Membuat nama file baru dengan akhiran .md
            nama_tanpa_ekstensi = os.path.splitext(path)[0]
            file_output = f"{nama_tanpa_ekstensi}.md"
            
            # Menyimpan hasil konversi
            with open(file_output, "w", encoding="utf-8") as f:
                f.write(hasil.text_content)
                
            sukses += 1
        except Exception as e:
            print(f"Gagal memproses {path}: {e}")
            gagal += 1
            
    # Tampilkan pesan pop-up setelah selesai
    pesan = f"Konversi Selesai!\n\nBerhasil: {sukses} file\nGagal: {gagal} file"
    messagebox.showinfo("Laporan Konversi", pesan)

# --- Membuat Jendela Aplikasi Sederhana (GUI) ---
root = tk.Tk()
root.title("MarkItDown ke Claude")
root.geometry("350x150")
root.eval('tk::PlaceWindow . center') # Posisi di tengah layar

label = tk.Label(root, text="Ubah PDF, Word, PPT, Excel jadi Markdown\nuntuk di-upload ke Claude Web", pady=15)
label.pack()

btn = tk.Button(root, text="Pilih File & Convert", command=jalankan_konversi, padx=15, pady=5, bg="blue", fg="black")
btn.pack(pady=5)

root.mainloop()