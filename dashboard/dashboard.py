import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("dashboard/all_data.csv")

st.header('Olist E-Commerce Dashboard :sparkles:')

st.subheader('10 Kota dengan jumlah pelanggan tertinggi')
city_counts = all_df['customer_city'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=city_counts.index[:10], y=city_counts.values[:10], palette='coolwarm')
plt.title('10 Kota dengan Jumlah Pelanggan Terbanyak')
plt.xlabel('Kota')
plt.ylabel('Jumlah Pelanggan')
plt.xticks(rotation=45)
st.pyplot(plt)

st.subheader('Distribusi penjual bedasarkan negara bagian')
state_counts = all_df['seller_state'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=state_counts.index, y=state_counts.values, palette='plasma')
plt.title('Distribusi Jumlah Penjual berdasarkan Negara Bagian')
plt.xlabel('Negara Bagian')
plt.ylabel('Jumlah Penjual')
plt.xticks(rotation=45)
st.pyplot(plt)

st.subheader('10 Kategori produk paling laris')
category_counts = all_df['product_category_name'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=category_counts.values[:10], y=category_counts.index[:10], palette='pastel')
plt.title('10 Kategori Produk Terlaris')
plt.xlabel('Jumlah Produk')
plt.ylabel('Kategori Produk')
st.pyplot(plt)

st.subheader('Distribusi jumlah pesanan bedasarkan status')
status_distribution = all_df['order_status'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=status_distribution.index, y=status_distribution.values, palette='coolwarm')
plt.title('Distribusi Status Pesanan')
plt.xlabel('Status Pesanan')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=45)
st.pyplot(plt)

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")