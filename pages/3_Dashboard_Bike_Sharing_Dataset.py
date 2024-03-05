import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk memuat data
@st.cache
def load_data():
    hour_data = pd.read_csv('path/to/hour.csv')
    day_data = pd.read_csv('path/to/day.csv')
    hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])
    day_data['dteday'] = pd.to_datetime(day_data['dteday'])
    return hour_data, day_data

def main():
    st.title("Dashboard Analisis Peminjaman Sepeda")

    hour_data, day_data = load_data()

    st.sidebar.header("Filter")
    option = st.sidebar.selectbox("Pilih Analisis:",
                                  ("Kondisi Cuaca", "Puncak Peminjaman", "Pola Peminjaman"))

    if option == "Kondisi Cuaca":
        st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda Harian")
        # Visualisasi data atau analisis lebih lanjut bisa ditambahkan di sini

    elif option == "Puncak Peminjaman":
        st.subheader("Kapan Puncak Peminjaman Sepeda Terjadi?")
        # Visualisasi data atau analisis lebih lanjut bisa ditambahkan di sini

    elif option == "Pola Peminjaman":
        st.subheader("Bagaimana Pola Peminjaman Sepeda Berubah Berdasarkan Jam, Hari, atau Bulan?")
        # Visualisasi data atau analisis lebih lanjut bisa ditambahkan di sini

    # Contoh menampilkan dataframe
    if st.checkbox('Tampilkan data sepeda harian'):
        st.write(day_data)

if __name__ == "__main__":
    main()