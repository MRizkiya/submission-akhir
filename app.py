import streamlit as st
import pandas as pd
import joblib

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Sistem Deteksi Dini Dropout Mahasiswa - Jaya Jaya Institut",
    page_icon="🎓",
    layout="wide"
)

# Header Aplikasi
st.title("🎓 Sistem Prediksi & Deteksi Dini Dropout Mahasiswa")
st.write("Aplikasi ini membantu **Jaya Jaya Institut** dalam memprediksi status kelulusan/potensi *dropout* mahasiswa berdasarkan data akademik dan sosial ekonomi.")

# Memuat Model Machine Learning
@st.cache_resource
def load_model():
    return joblib.load('model/model.joblib')

try:
    model = load_model()
    st.success("Model Machine Learning berhasil dimuat!")
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

# Sidebar: Input Form
st.sidebar.header("📋 Input Data Mahasiswa")

# Fitur Utama Penentu
tuition_fees = st.sidebar.selectbox("Status Pembayaran SPP", options=[1, 0], format_func=lambda x: "Lunas (1)" if x == 1 else "Menunggak (0)")
scholarship = st.sidebar.selectbox("Penerima Beasiswa", options=[1, 0], format_func=lambda x: "Ya (1)" if x == 0 else "Tidak (0)") # Sesuaikan 1/0
debtor = st.sidebar.selectbox("Status Memiliki Hutang", options=[1, 0], format_func=lambda x: "Ya (1)" if x == 1 else "Tidak (0)")
gender = st.sidebar.selectbox("Jenis Kelamin", options=[1, 0], format_func=lambda x: "Laki-laki (1)" if x == 1 else "Perempuan (0)")
age = st.sidebar.number_input("Usia Saat Mendaftar", min_value=15, max_value=70, value=20)

st.sidebar.subheader("Prestasi Akademik Semester 1 & 2")
sem1_approved = st.sidebar.number_input("MK Lulus Sem 1", min_value=0, max_value=20, value=5)
sem1_grade = st.sidebar.number_input("Rata-rata Nilai Sem 1", min_value=0.0, max_value=20.0, value=12.0)
sem2_approved = st.sidebar.number_input("MK Lulus Sem 2", min_value=0, max_value=20, value=5)
sem2_grade = st.sidebar.number_input("Rata-rata Nilai Sem 2", min_value=0.0, max_value=20.0, value=12.0)

# Menyiapkan Data Frame Input
input_data = pd.DataFrame([{
    'Marital_status': 1, 'Application_mode': 1, 'Application_order': 1, 'Course': 9254,
    'Daytime_evening_attendance': 1, 'Previous_qualification': 1, 'Previous_qualification_grade': 120.0,
    'Nacionality': 1, 'Mothers_qualification': 1, 'Fathers_qualification': 1,
    'Mothers_occupation': 1, 'Fathers_occupation': 1, 'Admission_grade': 120.0,
    'Displaced': 1, 'Educational_special_needs': 0, 'Debtor': debtor,
    'Tuition_fees_up_to_date': tuition_fees, 'Gender': gender, 'Scholarship_holder': scholarship,
    'Age_at_enrollment': age, 'International': 0,
    'Curricular_units_1st_sem_credited': 0, 'Curricular_units_1st_sem_enrolled': 5,
    'Curricular_units_1st_sem_evaluations': 5, 'Curricular_units_1st_sem_approved': sem1_approved,
    'Curricular_units_1st_sem_grade': sem1_grade, 'Curricular_units_1st_sem_without_evaluations': 0,
    'Curricular_units_2nd_sem_credited': 0, 'Curricular_units_2nd_sem_enrolled': 5,
    'Curricular_units_2nd_sem_evaluations': 5, 'Curricular_units_2nd_sem_approved': sem2_approved,
    'Curricular_units_2nd_sem_grade': sem2_grade, 'Curricular_units_2nd_sem_without_evaluations': 0,
    'Unemployment_rate': 10.8, 'Inflation_rate': 1.4, 'GDP': 1.74
}])

# Pemetaan Label (0 = Graduate, 1 = Dropout)
status_map = {0: 'Graduate', 1: 'Dropout'}

# Tombol Prediksi
if st.button("🔮 Prediksi Status Mahasiswa"):
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Hasil Prediksi:")
        # PERBAIKAN BUG: Mengecek angka 1 (Dropout) atau 0 (Graduate)
        if prediction == 1:
            st.error("⚠️ Risk Alert: **Dropout**")
            st.warning("Mahasiswa ini membutuhkan **bimbingan khusus** dan intervensi finansial/akademik!")
        else:
            st.success("🎉 Status: **Graduate** (Berpotensi Lulus Tepat Waktu)")

    with col2:
        st.subheader("Probabilitas:")
        # PERBAIKAN KRITERIA 3 REVIEWER: Mengubah label numerik (0/1) menjadi teks kategorikal
        labels = [status_map.get(c, str(c)) for c in model.classes_]
        
        prob_df = pd.DataFrame({
            'Status': labels,
            'Probabilitas (%)': [round(p * 100, 2) for p in probabilities]
        })
        st.dataframe(prob_df, hide_index=True)