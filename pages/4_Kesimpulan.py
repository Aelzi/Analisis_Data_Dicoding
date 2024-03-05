import streamlit as st

st.title("Kesimpulan")

# Poin-poin penting
st.markdown("""

### Pengaruh Kondisi Cuaca

Analisis visualisasi menunjukkan bahwa kondisi cuaca memiliki pengaruh yang signifikan terhadap jumlah peminjaman sepeda harian. Berikut adalah beberapa temuan utama:

**Suhu:**

* Terdapat tren positif yang kuat antara suhu dan jumlah peminjaman.
* Hari yang lebih hangat cenderung memiliki jumlah peminjaman yang lebih tinggi.
* Suhu yang terlalu tinggi mungkin membatasi peningkatan ini.

**Kelembapan:**

* Tidak ada pola yang sangat jelas antara kelembapan dan jumlah peminjaman.
* Kelembapan yang sangat tinggi bisa menurunkan jumlah peminjaman.

**Kecepatan Angin:**

* Hubungan antara kecepatan angin dan jumlah peminjaman tidak terlalu jelas.
* Angin yang lebih kencang cenderung menurunkan jumlah peminjaman.

**Situasi Cuaca:**

* Cuaca yang lebih cerah atau lebih baik berkorelasi dengan jumlah peminjaman yang lebih tinggi.
* Cuaca yang lebih buruk, seperti hujan ringan atau badai, berkorelasi dengan penurunan jumlah peminjaman.

**Kesimpulan:**

Kondisi cuaca yang baik secara intuitif lebih mendukung kegiatan bersepeda. Hujan, salju, atau cuaca buruk lainnya tidak hanya membuat bersepeda menjadi tidak nyaman tetapi juga bisa meningkatkan risiko kecelakaan.

**Puncak Peminjaman Sepeda:**

Analisis data dan visualisasi menunjukkan bahwa peminjaman sepeda mencapai puncaknya dua kali dalam sehari: sekitar jam 8 pagi dan antara jam 5 sore hingga 6 sore. Pola ini konsisten dengan rutinitas harian banyak orang, di mana sepeda digunakan untuk perjalanan ke tempat kerja atau pendidikan di pagi hari dan kembali ke rumah di sore hari.

**Pola Peminjaman Sepeda:**

Berdasarkan analisis data, pola peminjaman sepeda menunjukkan pengaruh yang signifikan dari waktu dalam sehari, hari dalam seminggu, dan bulan dalam setahun.

**Jam:**

* Puncak peminjaman terjadi pada jam 8 pagi dan 5-6 sore, konsisten dengan jam komuter.

**Hari:**

* Aktivitas peminjaman lebih tinggi pada hari kerja dibandingkan akhir pekan.

**Bulan:**

* Peningkatan peminjaman dari musim semi hingga musim panas dan penurunan pada musim gugur dan musim dingin, terkait dengan kondisi cuaca.

**Kesimpulan:**

Informasi ini dapat digunakan oleh penyedia layanan berbagi sepeda untuk mengantisipasi fluktuasi permintaan dan menyesuaikan ketersediaan sepeda, meningkatkan kepuasan pengguna dan efisiensi operasional.

""")
