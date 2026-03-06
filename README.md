# E-Commerce Data Analysis Dashboard ✨

Proyek ini merupakan analisis data **E-Commerce Public Dataset** yang bertujuan untuk memahami pola penjualan serta perilaku pelanggan menggunakan pendekatan analisis data dan visualisasi interaktif. Dashboard dibuat menggunakan **Streamlit** untuk menampilkan insight secara interaktif.

## Project Structure

```
submission
│
├── dashboard
│   ├── dashboard.py
│   └── main_data.csv
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Business Questions

1. Bagaimana pola penjualan e-commerce berdasarkan waktu (bulanan) dan kategori produk?
2. Bagaimana segmentasi pelanggan berdasarkan metode **RFM (Recency, Frequency, Monetary)**?

## Setup Environment

### Menggunakan Anaconda

```
conda create --name ecommerce-ds python=3.9
conda activate ecommerce-ds
pip install -r requirements.txt
```

### Menggunakan Terminal / Shell

```
mkdir ecommerce-data-analysis
cd ecommerce-data-analysis
pip install -r requirements.txt
```

## Run Streamlit Dashboard

Masuk ke folder dashboard kemudian jalankan aplikasi Streamlit.

```
cd dashboard
streamlit run dashboard.py
```

Setelah dijalankan, dashboard akan terbuka secara otomatis di browser pada alamat:

```
http://localhost:8501
```

## Dashboard Features

Dashboard ini menampilkan beberapa analisis utama:

* Monthly Sales Trend
* Top Product Categories by Revenue
* Customer RFM Analysis
* Customer Segmentation Visualization

## Dataset

Dataset yang digunakan berasal dari **E-Commerce Public Dataset** yang berisi informasi transaksi, pelanggan, produk, serta pembayaran.

## Author

**Nama:** Sifa Mutiasya Hendayana Puteri
**Email:** [sifamutiasya@gmail.com](mailto:sifamutiasya@gmail.com)
**ID Dicoding:** CDCC222D6X0835
