import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Tajuk aplikasi
st.title("Heatmap Generator")

# Input untuk tajuk
ylabel_title = st.text_input("Masukkan tajuk untuk Y-axis", "Tonggak")
xlabel_title = st.text_input("Masukkan tajuk untuk X-axis", "Elemen")

# Input untuk data
st.write("Masukkan data anda di bawah:")
index_data = st.text_area("Masukkan nama untuk Index (contoh: Tonggak)", "Identiti\nPeranti\nRangkaian")
column_data = st.text_area("Masukkan nama untuk Columns (contoh: Elemen)", "Kawalan Akses\nPengurusan Identiti")
values_data = st.text_area("Masukkan nilai (contoh: Skor Tahap Kerumitan)", "4.6, 3.4\n4.4, 3.2")

# Pemprosesan data
if index_data and column_data and values_data:
    try:
        # Parsing input
        index_list = index_data.split("\n")
        column_list = column_data.split("\n")
        values_list = [list(map(float, row.split(","))) for row in values_data.split("\n")]

        # Membina DataFrame
        df = pd.DataFrame(values_list, index=index_list, columns=column_list)

        # Plot heatmap
        st.write("Heatmap:")
        plt.figure(figsize=(16, 10))
        sns.heatmap(df, annot=True, cmap="YlGnBu", linewidths=0.1, linecolor="gray")

        # Menambah tajuk dan label
        plt.title("")
        plt.ylabel(ylabel_title)
        plt.xlabel(xlabel_title)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        # Paparkan graf
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Ralat semasa memproses data: {e}")
else:
    st.info("Masukkan semua data untuk menjana heatmap.")
