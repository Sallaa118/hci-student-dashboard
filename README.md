
# HCI Student Performance Dashboard: Interactive Data Visualization

## 📌 Deskripsi Proyek

Proyek ini merupakan implementasi sederhana **Human-Computer Interaction (HCI)** dan **Data Visualization** menggunakan Python.

Dashboard dibuat untuk membantu pengguna memahami data performa akademik siswa melalui ringkasan nilai, grafik interaktif, filter data, dan tabel yang dapat diunduh.

Dataset yang digunakan adalah Students Performance in Exams dari Kaggle. Data mencakup karakteristik siswa serta nilai ujian matematika, membaca, dan menulis.

Dashboard dikembangkan menggunakan Streamlit, Pandas, dan Plotly. Prinsip HCI diterapkan melalui penyajian informasi secara terstruktur, penggunaan label yang jelas, pengurangan elemen yang tidak diperlukan, serta pemberian kontrol kepada pengguna melalui filter interaktif.

Proyek ini merupakan studi kasus pembelajaran dan portofolio, bukan sistem penilaian akademik resmi.

## 🎯 Tujuan

1. Memahami penerapan HCI dalam pengembangan dashboard.
2. Mengolah dataset menggunakan Pandas.
3. Membuat visualisasi data interaktif menggunakan Plotly.
4. Menampilkan ringkasan nilai siswa secara informatif.
5. Menerapkan filter agar pengguna dapat mengeksplorasi data.
6. Menerapkan prinsip usability dalam penyajian informasi.
7. Menyiapkan dasar evaluasi usability untuk pengembangan penelitian lebih lanjut.

## 📂 Struktur Proyek

```text
hci-student-dashboard/
├── data/
│   └── StudentsPerformance.csv
├── app.py
├── download_dataset.py
├── cek_dataset.py
├── requirements.txt
├── README.md
└── .gitignore
```

Keterangan:

- `data/StudentsPerformance.csv`: dataset siswa dalam format CSV.
- `app.py`: kode utama dashboard interaktif.
- `download_dataset.py`: kode untuk mengunduh dataset dari Kaggle.
- `cek_dataset.py`: kode untuk memeriksa struktur dan kualitas data.
- `requirements.txt`: daftar library Python yang diperlukan.
- `README.md`: dokumentasi proyek.
- `.gitignore`: daftar file dan folder yang tidak perlu diunggah ke GitHub.

Folder `data/` perlu tersedia sebelum dashboard dijalankan. File dataset dapat diunduh melalui skrip atau secara manual dari Kaggle.

## 📊 Dataset

Dataset yang digunakan adalah **Students Performance in Exams**, yang tersedia di Kaggle.

Sumber:
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

Dataset asli berisi 1.000 baris data dan 8 kolom, meliputi karakteristik siswa serta nilai ujian.

Kolom yang digunakan:

| Kolom | Keterangan |
|---|---|
| `gender` | Gender siswa |
| `race/ethnicity` | Kelompok siswa |
| `parental level of education` | Tingkat pendidikan orang tua |
| `lunch` | Kategori makan siang |
| `test preparation course` | Status persiapan ujian |
| `math score` | Nilai matematika |
| `reading score` | Nilai membaca |
| `writing score` | Nilai menulis |

Dataset digunakan untuk analisis deskriptif dan visualisasi. Analisis ini tidak secara langsung membuktikan hubungan sebab-akibat antara karakteristik siswa dan nilai ujian.

**Catatan:** Periksa ketentuan lisensi dataset sebelum mendistribusikan salinan datanya. Repository dapat menyimpan kode dan petunjuk pengunduhan tanpa menyertakan file CSV.

## 🛠️ Teknologi yang Digunakan

- **Python 3** — bahasa pemrograman.
- **Pandas** — membaca, membersihkan, dan mengolah data.
- **Streamlit** — membangun dashboard interaktif.
- **Plotly Express** — membuat grafik interaktif.
- **KaggleHub** — membantu mengunduh dataset dari Kaggle.
- **Pathlib** — mengelola lokasi file dan folder.

## ⚙️ Cara Menjalankan Proyek

### 1. Clone repository

```bash
git clone <URL_REPOSITORY>
cd hci-student-dashboard
```

Ganti `<URL_REPOSITORY>` dengan URL repository GitHub milikmu.

### 2. Buat virtual environment

```bash
python -m venv .venv
```

Aktifkan di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika menggunakan Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3. Instal library

```bash
python -m pip install -r requirements.txt
```

### 4. Siapkan dataset

Jalankan skrip pengunduhan:

```bash
python download_dataset.py
```

Jika pengunduhan membutuhkan autentikasi atau mengalami kendala, unduh dataset secara manual dari halaman Kaggle, lalu letakkan file CSV di folder `data/` dengan nama:

```text
StudentsPerformance.csv
```

### 5. Periksa dataset

```bash
python cek_dataset.py
```

Pastikan jumlah baris, nama kolom, tipe data, dan nilai kosong sudah diperiksa.

### 6. Jalankan dashboard

```bash
python -m streamlit run app.py
```

Dashboard biasanya dapat diakses melalui:

http://localhost:8501

## 🔬 Metodologi Implementasi

### 1. Persiapan data

Dataset dibaca menggunakan Pandas. Nama kolom disesuaikan agar lebih mudah dipahami, kolom nilai dikonversi menjadi numerik, dan baris dengan nilai ujian yang tidak tersedia dihapus.

### 2. Ringkasan performa

Dashboard menampilkan jumlah siswa serta rata-rata nilai matematika, membaca, dan menulis berdasarkan data yang sedang dipilih.

### 3. Filter interaktif

Pengguna dapat menyaring data berdasarkan gender, pendidikan orang tua, dan status persiapan ujian.

### 4. Visualisasi data

Dua jenis grafik digunakan:

- **Bar chart:** membandingkan rata-rata nilai berdasarkan status persiapan ujian.
- **Scatter plot:** menunjukkan pola hubungan antara nilai matematika dan membaca.

### 5. Tabel dan ekspor data

Dashboard menampilkan tabel berdasarkan filter aktif dan menyediakan tombol untuk mengunduh hasil penyaringan dalam format CSV.

## 🧠 Penerapan Prinsip HCI

| Prinsip | Implementasi |
|---|---|
| User-centered design | Informasi disusun untuk mendukung kebutuhan eksplorasi data. |
| Recognition over recall | Label dan pilihan filter ditampilkan secara langsung. |
| Cognitive load | Informasi dibagi menjadi ringkasan, grafik, dan tabel. |
| Visibility of system status | Jumlah data yang ditampilkan mengikuti filter. |
| User control and freedom | Pengguna dapat mengganti filter atau memilih opsi Semua. |
| Aesthetic and minimalist design | Elemen dashboard difokuskan pada informasi yang relevan. |
| Overview first, details on demand | Ringkasan disajikan sebelum grafik dan tabel. |
| Data visualization | Grafik dipilih sesuai tujuan perbandingan dan eksplorasi hubungan. |

Penerapan tersebut merupakan rancangan awal. Kemudahan penggunaan yang sebenarnya perlu diperiksa melalui evaluasi dan pengujian dengan pengguna.

## 🧪 Pengujian Fungsional

Pengujian dilakukan untuk memastikan fitur utama dashboard berjalan sesuai harapan.

Skenario pengujian:

1. Dashboard dapat dibuka tanpa error.
2. Jumlah siswa sesuai dengan data yang terbaca.
3. Filter gender mengubah data yang ditampilkan.
4. Filter pendidikan orang tua berfungsi.
5. Filter persiapan ujian berfungsi.
6. Grafik mengikuti data hasil penyaringan.
7. Tabel menampilkan data yang sesuai.
8. Tombol unduh menghasilkan file CSV yang valid.
9. Pesan peringatan muncul ketika tidak ada data yang sesuai dengan filter.

Hasil pengujian perlu diisi berdasarkan eksekusi aplikasi yang sebenarnya.

Pengujian fungsional berbeda dengan pengujian usability. Untuk menilai pengalaman pengguna, penelitian lanjutan dapat menggunakan tugas terstruktur, pengukuran keberhasilan tugas, waktu penyelesaian, dan kuesioner System Usability Scale (SUS).

## 📈 Hasil dan Analisis

Dashboard dirancang untuk membantu pengguna mengeksplorasi data nilai siswa melalui ringkasan statistik, filter, dan grafik interaktif.

Hal yang dapat diamati setelah aplikasi dijalankan:

1. Perubahan filter memengaruhi jumlah data dan rata-rata nilai.
2. Bar chart membantu membandingkan rata-rata nilai antarkelompok.
3. Scatter plot membantu mengamati pola hubungan nilai matematika dan membaca.
4. Tabel menyediakan rincian data sesuai filter yang dipilih.

Hasil numerik dan kesimpulan akhir perlu diperoleh dari data serta pengujian yang benar-benar dilakukan. Visualisasi deskriptif tidak cukup untuk menyimpulkan hubungan sebab-akibat.

## 🧠 Kesimpulan

Proyek ini menerapkan konsep HCI dan Data Visualization melalui dashboard interaktif untuk analisis performa siswa.

Penggunaan Streamlit mempermudah pengembangan antarmuka, Pandas digunakan untuk pengolahan data, sedangkan Plotly menyediakan grafik interaktif.

Proyek ini menjadi dasar pembelajaran tentang penyajian informasi, interaksi pengguna, dan penerapan prinsip usability. Pengembangan berikutnya dapat difokuskan pada evaluasi pengalaman pengguna dan perbaikan antarmuka berdasarkan hasil pengujian.

## 🚀 Pengembangan Selanjutnya

- Menambahkan pilihan rentang nilai.
- Menambahkan grafik distribusi nilai.
- Memperbaiki tampilan untuk perangkat dengan layar kecil.
- Membuat wireframe dan persona pengguna.
- Melakukan evaluasi berdasarkan heuristik Nielsen.
- Menguji usability menggunakan SUS.
- Membandingkan desain awal dan desain hasil perbaikan.
- Menambahkan dokumentasi berupa tangkapan layar dashboard.

## ⚠️ Keterbatasan

1. Dataset digunakan untuk latihan analisis dan tidak mewakili seluruh populasi siswa.
2. Dashboard bersifat deskriptif, bukan model prediksi.
3. Visualisasi tidak membuktikan hubungan sebab-akibat.
4. Pengujian fungsional tidak otomatis menunjukkan bahwa antarmuka mudah digunakan.
5. Hasil evaluasi usability belum dapat disimpulkan sebelum pengujian dengan pengguna dilakukan.
6. Pengalaman penggunaan dapat berbeda berdasarkan perangkat dan ukuran layar.

---

**Kategori:** Human-Computer Interaction (HCI) dan Data Visualization  
**Bahasa:** Python  
**Dataset:** Students Performance in Exams — Kaggle  
**Framework:** Streamlit  
**Visualisasi:** Plotly  
**Status:** Proyek pembelajaran dan portofolio
