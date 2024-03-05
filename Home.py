import streamlit as st

# Menambahkan judul
st.title("Proyek Analisi Data Dicoding")

# Menampilkan informasi pribadi
st.markdown("""
**Nama:** Alfarelzi\n
**Email:** alfarezi31as@gmail.com\n
**Username:** Farelzii
""")

# Menambahkan judul dataset
st.header("Dataset: Analisis Bike Sharing Dataset")

# Menambahkan teks deskriptif tentang dataset
st.markdown("""
Dataset ini berisi data tentang penggunaan sepeda bersama di berbagai kota di seluruh dunia. 
Data ini dapat digunakan untuk menganalisis berbagai aspek penggunaan sepeda bersama, 
seperti pola penggunaan, pengaruh cuaca, dan faktor-faktor lain yang memengaruhi permintaan.

**Beberapa contoh analisis yang akan dilakukan dengan dataset ini:**

* Bagaimana kondisi cuaca mempengaruhi jumlah peminjaman sepeda harian?
* Kapan puncak peminjaman sepeda terjadi?
* Bagaimana pola peminjaman sepeda berubah berdasarkan jam, hari, atau bulan?




""")
