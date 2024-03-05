import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.dataframe_explorer import dataframe_explorer

# Fungsi untuk memuat data
df_hour=pd.read_csv("Bike-Sharing-dataset/hour.csv")
df_day=pd.read_csv("Bike-Sharing-dataset/day.csv")


def data_frame_hour(dataframe):
    
    st.markdown("## :green[Data Frame Hour ]")
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)
    
data_frame_hour(df_hour)

def data_frame_day(dataframe):
    
    st.markdown("## :blue[Data Frame Day ]")
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)
    
data_frame_day(df_day)


st.title("Analisis Dataset Bike Sharing")
# Muat dataset (Ganti dengan path file Anda) 
st.header("Visualisasi Distribusi Data per Jam")

# Atur gaya seaborn 
sns.set(style="whitegrid")

# Buat kolom untuk visualisasi - 2 baris x 2 kolom
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Visualisasi 1: Temperatur 
with col1:
    sns.boxplot(x=df_hour['temp'], color='skyblue')
    st.pyplot(plt)
    plt.clf()  # Bersihkan figure sebelumnya

# Visualisasi 2: Feels-Like Temp  
with col2:
    sns.boxplot(x=df_hour['atemp'], color='lightgreen')
    st.pyplot(plt)
    plt.clf()  

# Visualisasi 3: Kelembapan
with col3:
    sns.boxplot(x=df_hour['hum'], color='salmon')
    st.pyplot(plt)
    plt.clf()

# Visualisasi 4: Kecepatan Angin 
with col4:
    sns.boxplot(x=df_hour['windspeed'], color='gold')
    st.pyplot(plt)
    plt.clf()
    
    
st.title("Analisis Dataset Bike Sharing (Data Harian)")


st.header("Visualisasi Distribusi Data Harian")

# Atur gaya seaborn 
sns.set(style="whitegrid")

# Buat kolom untuk visualisasi - 2 baris x 2 kolom
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)

# Visualisasi 1: Temperatur 
with col5:
    sns.boxplot(x=df_day['temp'], color='skyblue')
    st.pyplot(plt)
    plt.clf()  

# Visualisasi 2: Feels-Like Temp  
with col6:
    sns.boxplot(x=df_day['atemp'], color='lightgreen')
    st.pyplot(plt)
    plt.clf() 

# Visualisasi 3: Kelembapan
with col7:
    sns.boxplot(x=df_day['hum'], color='salmon')
    st.pyplot(plt)
    plt.clf()

# Visualisasi 4: Kecepatan Angin 
with col8:
    sns.boxplot(x=df_day['windspeed'], color='gold')
    st.pyplot(plt)
    plt.clf()
    
    
    
st.write("## Suhu vs Jumlah Peminjaman Sepeda Harian")

# Visualisasi
plt.figure(figsize=(16, 12))
plt.subplot(2, 2, 1)
sns.scatterplot(x='temp', y='cnt', data=df_day, color='blue', alpha=0.6)

plt.title('Suhu vs Jumlah Peminjaman Sepeda Harian')
plt.xlabel('Suhu')
plt.ylabel('Total Peminjaman')
plt.tight_layout()
st.pyplot(plt)

# Menampilkan teks interpretasi
text = """
Terdapat korelasi positif antara suhu dan jumlah peminjaman sepeda.
Ini menunjukkan bahwa jumlah peminjaman cenderung meningkat pada hari yang lebih hangat. Scatter plot menunjukkan tren positif, di mana hari dengan suhu lebih tinggi memiliki jumlah peminjaman yang lebih besar.

"""
st.markdown(text)


st.write("## Kelembapan vs Jumlah Peminjaman Sepeda Harian")

# Visualisasi
plt.figure(figsize=(16, 12))
plt.subplot(2, 2, 2)
sns.scatterplot(x='hum', y='cnt', data=df_day, color='green', alpha=0.6)

plt.title('Kelembapan vs Jumlah Peminjaman Sepeda Harian')
plt.xlabel('Kelembapan')
plt.ylabel('Total Peminjaman')
plt.tight_layout()
st.pyplot(plt)

# Menampilkan teks interpretasi
text = """
Scatter plot antara kelembapan dan jumlah peminjaman tidak menunjukkan hubungan yang jelas.
Namun, ada kecenderungan jumlah peminjaman yang lebih rendah pada kelembapan yang sangat tinggi.
Hal ini mungkin mengindikasikan pengurangan aktivitas peminjaman sepeda pada kondisi yang sangat lembap.

"""
st.markdown(text)


st.write("## Kecepatan Angin vs Jumlah Peminjaman Sepeda Harian")

# Kecepatan Angin (windspeed) vs Jumlah Peminjaman
plt.figure(figsize=(16, 12))
plt.subplot(2, 2, 3)
sns.scatterplot(x='windspeed', y='cnt', data=df_day, color='orange', alpha=0.6)
plt.title('Kecepatan Angin vs Jumlah Peminjaman Sepeda Harian')
plt.xlabel('Kecepatan Angin')
plt.ylabel('Total Peminjaman')
plt.tight_layout()
st.pyplot(plt)

# Menampilkan teks interpretasi
text = """
Tidak ada hubungan yang jelas dari scatter plot antara kecepatan angin dan jumlah peminjaman, tapi terlihat bahwa pada kecepatan angin yang lebih tinggi, jumlah peminjaman cenderung lebih bervariasi namun umumnya lebih rendah.

"""
st.markdown(text)

st.write("## Situasi Cuaca vs Jumlah Peminjaman Sepeda Harian")

# Situasi Cuaca (weathersit) vs Jumlah Peminjaman
plt.figure(figsize=(16, 12))
plt.subplot(2, 2, 4)
sns.boxplot(x='weathersit', y='cnt', data=df_day)
plt.title('Situasi Cuaca vs Jumlah Peminjaman Sepeda Harian')
plt.xlabel('Situasi Cuaca')
plt.ylabel('Total Peminjaman')
plt.tight_layout()
st.pyplot(plt)

# Menampilkan teks interpretasi
text = """
Boxplot menunjukkan bahwa kondisi cuaca yang lebih baik (nilai weathersit lebih rendah) berkorelasi dengan jumlah peminjaman sepeda yang lebih tinggi. Ini menunjukkan bahwa cuaca yang lebih cerah atau lebih baik cenderung mendorong lebih banyak peminjaman sepeda.

"""
st.markdown(text)


st.write("## Pola Peminjaman Berdasarkan Jam (Hourly Patterns)")

# Mempersiapkan data agregat
hourly_avg = df_hour.groupby('hr')['cnt'].mean()
daily_avg = df_hour.groupby('weekday')['cnt'].mean()
monthly_avg = df_hour.groupby('mnth')['cnt'].mean()

# Pola Peminjaman Berdasarkan Jam
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
hourly_avg.plot(kind='bar', color='skyblue')
plt.title('Rata-Rata Jumlah Peminjaman per Jam')
plt.xlabel('Jam')
plt.ylabel('Rata-Rata Jumlah Peminjaman')
plt.xticks(rotation=0)
plt.tight_layout()
st.pyplot(plt)

# Menampilkan teks interpretasi
text = """
- Puncak Peminjaman: Puncak peminjaman terjadi pada jam-jam sibuk: pagi sekitar jam 8 dan sore sekitar jam 17-18. Ini kemungkinan besar mencerminkan pola komuter, di mana orang menggunakan sepeda untuk pergi ke dan pulang dari tempat kerja atau sekolah. Konsistensi puncak ini menunjukkan bahwa layanan berbagi sepeda sangat dipengaruhi oleh rutinitas harian pengguna. Penyedia layanan dapat meningkatkan ketersediaan sepeda dan stasiun docking di jam-jam sibuk untuk memenuhi permintaan.
"""
st.markdown(text)


