import streamlit as st
from streamlit_extras.switch_page_button import switch_page
 
# Deskripsi Dataset
st.title("Bike Sharing Dataset")

st.subheader("Latar Belakang")
st.write("""
Sistem berbagi sepeda adalah cara baru penyewaan sepeda tradisional, dimana seluruh proses mulai dari pendaftaran keanggotaan, penyewaan, dan pengembalian dilakukan secara otomatis..... (isi sisanya dari penjelasan dataset)
""")

st.subheader("Dataset")
st.write("""
Dataset utama berisi catatan historis dua tahun (2011 dan 2012) dari sistem Capital Bikeshare di Washington D.C., Amerika Serikat.... (isi sisanya dari penjelasan dataset) 
""")

# Petunjuk penggunaan dataset secara umum (Anda bisa sesuaikan)
st.subheader("Penggunaan")
st.write("**Contoh Tugas yang Dapat Dilakukan:**")
st.write("* **Regresi**: Prediksi jumlah penyewaan berdasarkan kondisi lingkungan dan musim.")
st.write("* **Deteksi Peristiwa dan Anomali**")

# Tambahkan bagian lain seperti informasi file, karakteristik, lisensi, dan kontak
