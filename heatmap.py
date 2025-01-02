import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Tajuk aplikasi
st.title("Heatmap Generator")



# Input untuk tajuk
ylabel_title = st.text_input("Y-Axis Category (Index)", "Vehicle Type")
xlabel_title = st.text_input("X-axis Category (Columns)", "Features")

# Input untuk data
st.write("Put the label name and their values:")
index_data = st.text_area("Label for Index (ex: Type)", "Sedan\nSUV\nHatchback\nMPV\nSports Car\nTruck\nConvertible")
column_data = st.text_area("Label for Columns (ex: Features)", "Comfort\nSpeed\nFuel Efficiency\nCargo Space\nPrice\nSafety\nPerformance Consistency")
values_data = st.text_area("Values (ex: Scores)", 
                            "8, 7, 9, 6, 5, 9, 8\n"
                            "7, 8, 6, 8, 7, 8, 7\n"
                            "6, 7, 8, 5, 4, 7, 6\n"
                            "8, 6, 7, 9, 6, 8, 7\n"
                            "9, 9, 5, 4, 10, 9, 9\n"
                            "6, 5, 7, 10, 4, 6, 6\n"
                            "8, 8, 6, 4, 8, 8, 9")

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
