import streamlit as st
# Deskripsi Dataset
st.title("Bike Sharing Dataset")

st.subheader("Latar Belakang")
st.write("""
Dataset Bike Sharing dibuat untuk memahami dan menganalisis sistem berbagi sepeda di Washington D.C., Amerika Serikat. Data ini dikumpulkan selama dua tahun (2011-2012) dan mencakup informasi tentang:
""")

st.subheader("Dataset")
st.write(""" 
- **instant**: indeks baris
- **dteday**: tanggal
- **season**: musim (1: semi, 2: panas, 3: gugur, 4: dingin)
- **yr**: tahun (0: 2011, 1:2012)
- **mnth**: bulan (1 sampai 12)
- **hr**: jam (0 sampai 23)
- **holiday**: apakah hari itu libur atau tidak
- **weekday**: hari
- **workingday**: 1 jika bukan akhir pekan atau hari libur, 0 jika sebaliknya
- **weathersit**: kondisi cuaca
- **temp**: temperatur ternormalisasi (Celcius)
- **atemp**: suhu yang dirasakan, ternormalisasi (Celcius)
- **hum**: kelembapan ternormalisasi
- **windspeed**: kecepatan angin ternormalisasi
- **casual**: jumlah pengguna tidak terdaftar
- **registered**: jumlah pengguna terdaftar
- **cnt**: jumlah total sepeda yang disewa (termasuk terdaftar dan tidak) """)
