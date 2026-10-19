
import pandas as pd

df = pd.read_csv("data/StudentsPerformance.csv")

print("Ukuran dataset:", df.shape)

print("\nNama kolom:")
print(df.columns.tolist())

print("\nLima baris pertama:")
print(df.head())

print("\nInformasi tipe data:")
df.info()

print("\nJumlah data kosong:")
print(df.isnull().sum())
