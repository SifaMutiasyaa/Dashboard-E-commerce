import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

df = pd.read_csv("dashboard/main_data.csv")

df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

df["year"] = df["order_purchase_timestamp"].dt.year
df["month"] = df["order_purchase_timestamp"].dt.to_period("M").astype(str)

st.title("E-Commerce Sales Dashboard")

year_filter = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(df["year"].unique())
)

df_filtered = df[df["year"] == year_filter]

total_revenue = df_filtered["payment_value"].sum()
total_orders = df_filtered["order_id"].nunique()
avg_order_value = total_revenue / total_orders

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")

st.subheader("Monthly Sales Trend")

monthly_sales = (
    df_filtered.groupby("month")["payment_value"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    monthly_sales,
    x="month",
    y="payment_value",
    markers=True,
    title="Revenue per Month"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Monthly Order Trend")

monthly_orders = (
    df_filtered.groupby("month")["order_id"]
    .nunique()
    .reset_index()
)

fig2 = px.bar(
    monthly_orders,
    x="month",
    y="order_id",
    title="Total Orders per Month"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Top Product Categories")

category_sales = (
    df_filtered.groupby("product_category_name")["payment_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    category_sales,
    x="payment_value",
    y="product_category_name",
    orientation="h",
    title="Top 10 Product Categories"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Customer RFM Summary")

snapshot_date = df["order_purchase_timestamp"].max() + pd.Timedelta(days=1)

rfm = df.groupby("customer_unique_id").agg({
    "order_purchase_timestamp": lambda x: (snapshot_date - x.max()).days,
    "order_id": "nunique",
    "payment_value": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

col1, col2, col3 = st.columns(3)

col1.metric("Avg Recency", f"{rfm['Recency'].mean():.0f} days")
col2.metric("Avg Frequency", f"{rfm['Frequency'].mean():.2f}")
col3.metric("Avg Monetary", f"${rfm['Monetary'].mean():.2f}")

fig4 = px.scatter(
    rfm,
    x="Recency",
    y="Monetary",
    size="Frequency",
    title="Customer RFM Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

st.markdown("""
### Insight

**Sales Trend**
Penjualan meningkat sepanjang tahun dengan pertumbuhan signifikan pada beberapa bulan tertentu yang menunjukkan adanya peningkatan aktivitas belanja pelanggan.

**Product Category**
Kategori seperti kebutuhan rumah tangga dan produk kesehatan menjadi penyumbang pendapatan terbesar.

**Customer Behavior**
Sebagian besar pelanggan memiliki frekuensi pembelian rendah namun terdapat kelompok kecil pelanggan dengan nilai transaksi tinggi yang berkontribusi besar terhadap total revenue.
""")
