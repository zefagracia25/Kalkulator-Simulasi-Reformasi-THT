import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Tabungan")

# Judul utama
st.title("Kalkulator Tabungan Simulasi")

# Pilihan mode utama
mode = st.selectbox(
    "Pilih jenis perhitungan:",
    ["Proyeksi Saldo Tabungan", "Tabungan Berencana", "Menabung Harian"]
)

# --- PROYEKSI SALDO TABUNGAN ---
if mode == "Proyeksi Saldo Tabungan":
    freq = st.selectbox(
        "Frekuensi menabung:",
        ["Bulanan", "Tahunan", "Semesteran", "Triwulanan"]
    )
    gaji = st.number_input("Gaji per bulan (Rp):", value=5000000, step=100000)
    iuran_pct = st.number_input("Persentase iuran (%):", value=10.0, step=0.1)
    bunga = st.number_input("Bunga/imbal hasil tahunan (%):", value=5.0, step=0.01)
    periode = st.number_input("Jangka waktu (tahun):", value=5, min_value=1)

    if st.button("Hitung"):
        x = gaji * iuran_pct / 100

        if freq == "Bulanan":
            i = bunga / 100 / 12
            n = 12 * periode
            period_label = "bulan"
        elif freq == "Tahunan":
            i = bunga / 100
            n = periode
            period_label = "tahun"
        elif freq == "Semesteran":
            i = bunga / 100 / 2
            n = 2 * periode
            period_label = "semester"
        else:  # Triwulanan
            i = bunga / 100 / 4
            n = 4 * periode
            period_label = "triwulan"

        if i == 0:
            FV = x * n
        else:
            FV = x * (((1 + i) ** n - 1) / i)

        st.success(f"Proyeksi saldo setelah {periode} tahun adalah Rp {FV:,.0f}")

        # Ringkasan saldo per tahun
        st.subheader("Ringkasan per tahun")
        rows = []
        for y in range(1, periode + 1):
            if period_label == "bulan":
                n_y = 12 * y
            elif period_label == "tahun":
                n_y = y
            elif period_label == "semester":
                n_y = 2 * y
            else:
                n_y = 4 * y

            if i == 0:
                fv_y = x * n_y
            else:
                fv_y = x * (((1 + i) ** n_y - 1) / i)

            rows.append({"Tahun": y, "Saldo (Rp)": f"{fv_y:,.0f}"})

        st.table(rows)

# --- TABUNGAN BERENCANA ---
elif mode == "Tabungan Berencana":
    target = st.number_input("Target tabungan (Rp):", value=100000000, step=100000)
    bunga = st.number_input("Bunga/imbal hasil tahunan (%):", value=5.0, step=0.01)
    periode = st.number_input("Jangka waktu (tahun):", value=5, min_value=1)

    if st.button("Hitung"):
        i = bunga / 100 / 12
        n = 12 * periode

        if i == 0:
            PMT = target / n
        else:
            PMT = target * i / ((1 + i) ** n - 1)

        st.success(
            f"Anda perlu menabung sebesar Rp {PMT:,.0f} per bulan selama {periode} tahun "
            f"untuk mencapai Rp {target:,.0f}"
        )

# --- MENABUNG HARIAN ---
else:
    nominal = st.number_input("Nominal tabungan harian (Rp):", value=20000, step=1000)
    bunga = st.number_input("Bunga/imbal hasil tahunan (%):", value=5.0, step=0.01)
    periode = st.number_input("Jangka waktu (tahun):", value=5, min_value=1)

    if st.button("Hitung"):
        i = bunga / 100 / 365
        n = periode * 365

        if i == 0:
            FV = nominal * n
        else:
            FV = nominal * (((1 + i) ** n - 1) / i)

        st.success(
            f"Jika Anda menabung Rp {nominal:,.0f} per hari selama {periode} tahun, "
            f"maka saldo akhir Anda adalah Rp {FV:,.0f}"
        )
