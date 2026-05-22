import streamlit as st

st.title("🎈 project ujicoba lpk")
import streamlit as st

st.title("🧪 Kalkulator Titrasi Asam Basa")

st.write("Gunakan rumus M1V1 = M2V2")

# Input data
st.subheader("Input Data")

M1 = st.number_input("Molaritas larutan diketahui (M1)", min_value=0.0, value=0.1)
V1 = st.number_input("Volume larutan diketahui (V1) mL", min_value=0.0, value=10.0)
V2 = st.number_input("Volume larutan tidak diketahui (V2) mL", min_value=0.0, value=20.0)

# Tombol hitung
if st.button("Hitung Konsentrasi"):

    if V2 != 0:
        M2 = (M1 * V1) / V2

        st.success(f"Konsentrasi larutan tidak diketahui (M2) = {M2:.4f} M")

    else:
        st.error("Volume V2 tidak boleh nol")
