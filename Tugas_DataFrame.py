import pandas as pd

# Nomor 1
df = pd.read_excel('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.xlsx', sheet_name='data')
df = df.fillna(0)
print("=== DataFrame Awal ===")
print(df)

# Nomor 2
hsl_thn_2015_2018 = {}
for i, row in df.iterrows():
    tahun = row['tahun']
    if 2015 <= tahun <= 2018:
        if tahun not in hsl_thn_2015_2018:
            hsl_thn_2015_2018[tahun] = 0
        hsl_thn_2015_2018[tahun] += row['jumlah_produksi_sampah']
jumlah_tahun_2015_2018 = pd.DataFrame(list(hsl_thn_2015_2018.items()), columns=['Tahun', 'Total'])
print("\n=== Jumlah Data Produksi Sampah Tahun 2015-2018 ===")
print(jumlah_tahun_2015_2018)

# Nomor 3
hsl_thn = {}
for i, row in df.iterrows():
    tahun = row['tahun']
    if tahun not in hsl_thn:
        hsl_thn[tahun] = 0
    hsl_thn[tahun] += row['jumlah_produksi_sampah']
jumlah_per_tahun = pd.DataFrame(list(hsl_thn.items()), columns=['Tahun', 'Total'])
print("\n=== Jumlah Data Produksi Sampah Per-Tahun ===")
print(jumlah_per_tahun)

# Nomor 4
hsl_kota = {}
for i, row in df.iterrows():
    kota = row['nama_kabupaten_kota']
    tahun = row['tahun']
    key = (kota,tahun)
    if key not in hsl_kota:
        hsl_kota[key] = 0 
    hsl_kota[key] += row['jumlah_produksi_sampah']
dt_list = [{'Kota': k[0], 'Tahun': k[1], 'Total': v} 
           for k, v in hsl_kota.items()]
jumlah_kota_per_tahun = pd.DataFrame(dt_list)
print("\n=== Jumlah Data Produksi Sampah Per-Kota/Kabupaten Per-Tahun ===")
print(jumlah_kota_per_tahun)

jumlah_tahun_2015_2018.to_csv('jumlah_tahun2015_2018.csv', index=False)
jumlah_tahun_2015_2018.to_excel('jumlah_tahun2015_2018.xlsx', index=False)

jumlah_per_tahun.to_csv('jumlah_pertahun.csv', index=False)
jumlah_per_tahun.to_excel('jumlah_pertahun.xlsx', index=False)

jumlah_kota_per_tahun.to_csv('jumlah_perkota_pertahun.csv', index=False)
jumlah_kota_per_tahun.to_excel('jumlah_perkota_pertahun.xlsx', index=False)