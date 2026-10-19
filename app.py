
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------
# 1. Konfigurasi halaman
# ---------------------------------
st.set_page_config(
    page_title="Dashboard Performa Siswa",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "StudentsPerformance.csv"

st.title("Dashboard Analisis Performa Siswa")
st.write(
    "Jelajahi data nilai ujian siswa menggunakan "
    "filter dan visualisasi interaktif."
)

# ---------------------------------
# 2. Membaca dataset
# ---------------------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)

    # Rapikan nama kolom untuk tampilan
    df = df.rename(columns={
        "gender": "Gender",
        "race/ethnicity": "Kelompok",
        "parental level of education": "Pendidikan Orang Tua",
        "lunch": "Kategori Makan Siang",
        "test preparation course": "Persiapan Ujian",
        "math score": "Matematika",
        "reading score": "Membaca",
        "writing score": "Menulis"
    })

    score_columns = [
        "Matematika", "Membaca", "Menulis"
    ]

    for col in score_columns:
        df[col] = pd.to_numeric(
            df[col], errors="coerce"
        )

    df = df.dropna(subset=score_columns)

    # Rata-rata tiga mata pelajaran
    df["Rata-rata"] = df[score_columns].mean(axis=1)

    return df


if not DATA_PATH.exists():
    st.error(
        "Dataset belum ditemukan. Jalankan "
        "download_dataset.py terlebih dahulu."
    )
    st.stop()

df = load_data(str(DATA_PATH))

# ---------------------------------
# 3. Filter interaktif
# ---------------------------------
st.sidebar.header("Filter Data")

def add_all_option(series):
    return ["Semua"] + sorted(
        series.dropna().astype(str).unique().tolist()
    )

gender = st.sidebar.selectbox(
    "Gender",
    add_all_option(df["Gender"])
)

education = st.sidebar.selectbox(
    "Pendidikan Orang Tua",
    add_all_option(df["Pendidikan Orang Tua"])
)

preparation = st.sidebar.selectbox(
    "Persiapan Ujian",
    add_all_option(df["Persiapan Ujian"])
)

filtered = df.copy()

if gender != "Semua":
    filtered = filtered[filtered["Gender"] == gender]

if education != "Semua":
    filtered = filtered[
        filtered["Pendidikan Orang Tua"] == education
    ]

if preparation != "Semua":
    filtered = filtered[
        filtered["Persiapan Ujian"] == preparation
    ]

st.caption(
    f"Menampilkan {len(filtered)} dari {len(df)} siswa."
)

if filtered.empty:
    st.warning(
        "Tidak ada data yang sesuai dengan filter. "
        "Silakan ubah pilihan filter."
    )
    st.stop()

# ---------------------------------
# 4. Ringkasan data
# ---------------------------------
st.subheader("Ringkasan Performa")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Jumlah Siswa", f"{len(filtered):,}")
col2.metric(
    "Rata-rata Matematika",
    f"{filtered['Matematika'].mean():.2f}"
)
col3.metric(
    "Rata-rata Membaca",
    f"{filtered['Membaca'].mean():.2f}"
)
col4.metric(
    "Rata-rata Menulis",
    f"{filtered['Menulis'].mean():.2f}"
)

# ---------------------------------
# 5. Grafik perbandingan nilai
# ---------------------------------
st.subheader("Perbandingan Nilai Berdasarkan Persiapan Ujian")

score_columns = [
    "Matematika", "Membaca", "Menulis"
]

chart_data = filtered.melt(
    id_vars=["Persiapan Ujian"],
    value_vars=score_columns,
    var_name="Mata Pelajaran",
    value_name="Nilai"
)

average_scores = (
    chart_data.groupby(
        ["Persiapan Ujian", "Mata Pelajaran"],
        as_index=False
    )["Nilai"].mean()
)

fig_bar = px.bar(
    average_scores,
    x="Persiapan Ujian",
    y="Nilai",
    color="Mata Pelajaran",
    barmode="group",
    title="Rata-rata Nilai Menurut Status Persiapan Ujian",
    labels={
        "Persiapan Ujian": "Status Persiapan",
        "Nilai": "Rata-rata Nilai"
    }
)

fig_bar.update_layout(
    yaxis_range=[0, 100],
    legend_title_text="Mata Pelajaran"
)

st.plotly_chart(fig_bar, width="stretch")

# ---------------------------------
# 6. Grafik hubungan nilai
# ---------------------------------
st.subheader("Hubungan Nilai Matematika dan Membaca")

fig_scatter = px.scatter(
    filtered,
    x="Matematika",
    y="Membaca",
    color="Persiapan Ujian",
    hover_data=["Gender", "Menulis"],
    title="Sebaran Nilai Matematika dan Membaca",
    labels={
        "Matematika": "Nilai Matematika",
        "Membaca": "Nilai Membaca"
    }
)

fig_scatter.update_layout(
    xaxis_range=[0, 100],
    yaxis_range=[0, 100]
)

st.plotly_chart(fig_scatter, width="stretch")

# ---------------------------------
# 7. Tabel data dan unduhan
# ---------------------------------
st.subheader("Data Siswa")

st.dataframe(
    filtered,
    width="stretch",
    hide_index=True
)

csv_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Unduh Data Hasil Filter (CSV)",
    data=csv_data,
    file_name="data_siswa_terfilter.csv",
    mime="text/csv"
)

st.caption(
    "Catatan: hasil merupakan analisis deskriptif "
    "dan tidak membuktikan hubungan sebab-akibat."
)
