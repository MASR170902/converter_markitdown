import streamlit as st
from markitdown import MarkItDown
import os

# Judul Halaman Web
st.title("📄 MarkItDown Converter")
st.write("Ubah file PDF, Word, Excel, PPT menjadi Markdown murni.")

# Widget Upload File
uploaded_file = st.file_uploader("Pilih atau drag & drop file ke sini...", 
                                 type=["pdf", "docx", "xlsx", "pptx", "html", "csv", "json"])

if uploaded_file is not None:
    # Simpan file yang diupload ke penyimpanan sementara
    temp_filename = f"temp_{uploaded_file.name}"
    with open(temp_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.info("Sedang memproses konversi, mohon tunggu...")
    
    try:
        # Jalankan konversi MarkItDown
        md = MarkItDown()
        result = md.convert(temp_filename)
        
        st.success("Konversi berhasil!")
        
        # Tampilkan preview hasil konversi
        with st.expander("Lihat Preview Teks Markdown"):
            st.text_area("Hasil:", result.text_content, height=250)
        
        # Tombol Download hasil .md
        st.download_button(
            label="⬇️ Download File Markdown (.md)",
            data=result.text_content,
            file_name=f"{uploaded_file.name}.md",
            mime="text/markdown"
        )
        
    except Exception as e:
        st.error(f"Terjadi kesalahan saat konversi: {e}")
        
    finally:
        # Hapus file sementara agar server tidak penuh
        if os.path.exists(temp_filename):
            os.remove(temp_filename)