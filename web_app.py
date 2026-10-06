import streamlit as st
from markitdown import MarkItDown
import os

# Judul Halaman Web
st.title("📄 MarkItDown Converter")
st.write("Ubah file PDF, Word, Excel, PPT menjadi Markdown murni. Bisa multi-file sekaligus!")

# Widget Upload File dengan dukungan multi-file
uploaded_files = st.file_uploader(
    "Pilih atau drag & drop beberapa file ke sini...", 
    type=["pdf", "docx", "xlsx", "pptx", "html", "csv", "json"],
    accept_multiple_files=True
)

if uploaded_files:
    st.info(f"Total {len(uploaded_files)} file dipilih. Memproses konversi...")
    
    # Inisialisasi MarkItDown
    md = MarkItDown()
    
    for uploaded_file in uploaded_files:
        st.write("---")
        st.subheader(f"📁 File: {uploaded_file.name}")
        
        temp_filename = f"temp_{uploaded_file.name}"
        with open(temp_filename, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            # Jalankan konversi
            result = md.convert(temp_filename)
            
            st.success(f"Berhasil mengkonversi {uploaded_file.name}!")
            
            # Tampilkan preview teks markdown
            with st.expander(f"Lihat Preview Markdown ({uploaded_file.name})"):
                st.text_area("Hasil:", result.text_content, height=200, key=uploaded_file.name)
            
            # Tombol Download per file
            st.download_button(
                label=f"⬇️ Download {uploaded_file.name}.md",
                data=result.text_content,
                file_name=f"{uploaded_file.name}.md",
                mime="text/markdown",
                key=f"dl_{uploaded_file.name}"
            )
            
        except Exception as e:
            st.error(f"Gagal memproses {uploaded_file.name}: {e}")
            
        finally:
            # Hapus file sementara
            if os.path.exists(temp_filename):
                os.remove(temp_filename)