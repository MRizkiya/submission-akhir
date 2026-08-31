# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan perguruan tinggi yang berdiri sejak tahun 2000 dan telah mencetak banyak alumni berkualitas. Meskipun demikian, institusi ini menghadapi tantangan serius terkait tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya (*dropout*). Fenomena ini berdampak langsung pada keberlanjutan finansial operasional perguruan tinggi serta reputasi akademik institusi.

### Permasalahan Bisnis
* Berapa rasio *dropout* mahasiswa di Jaya Jaya Institut secara keseluruhan?
* Faktor sosial ekonomi dan akademik apa saja yang paling signifikan memicu terjadinya *dropout* mahasiswa?
* Bagaimana cara memprediksi dan mendeteksi secara dini mahasiswa yang berisiko *dropout* agar pihak manajemen institusi dapat memberikan penanganan yang tepat waktu?

### Cakupan Proyek
* **Exploratory Data Analysis (EDA):** Menganalisis pola performa akademik dan demografi mahasiswa dari dataset `data.csv`.
* **Business Dashboard:** Membangun *dashboard* interaktif menggunakan Looker Studio untuk memantau indikator kinerja utama (KPI) dan faktor risiko *dropout*.
* **Machine Learning Modeling:** Mengembangkan model klasifikasi (*Random Forest Classifier*) untuk memprediksi potensi *dropout* mahasiswa.
* **Model Deployment:** Mengintegrasikan model ke dalam aplikasi web interaktif berbasis Streamlit dan mendeply ke Streamlit Community Cloud.

### Persiapan

Sumber data: Dataset `students' performance` (`data.csv`) 
link dataset: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

1. Membuat dan Mengaktifkan Virtual Environment
Untuk memastikan seluruh *dependency* terisolasi dengan stabil dan proyek dapat dijalankan ulang oleh siapapun, ikuti langkah berikut:

- Membuat virtual environment
python -m venv env

- Mengaktifkan virtual environment (Windows)
env\Scripts\activate

- Mengaktifkan virtual environment (macOS/Linux)
source env/bin/activate

2. Menginstal Dependensi
pip install -r requirements.txt

3. Menjalankan Aplikasi Streamlit
streamlit run app.py

## Business Dashboard
Business Dashboard dikembangkan menggunakan Looker Studio untuk menyajikan visualisasi data secara interaktif dan mempermudah pemantauan rasio dropout secara real-time.

Link Access Dashboard: https://datastudio.google.com/reporting/837ff541-baf5-4581-9900-91aec4f23c70

Fitur Dashboard: 
- Scorecard KPI: Total Mahasiswa, Jumlah Dropout, dan Dropout Rate (%).
- Visualisasi Komparatif: Proporsi Status Mahasiswa, Rasio Dropout berdasarkan Status SPP (Tuition_fees_up_to_date), dan Rasio Dropout berdasarkan Penerima Beasiswa (Scholarship_holder).
- Breakdown Akademik: Distribusi Dropout per Program Studi (Course).
- Filter Kontrol Interaktif: Dropdown per Program Studi dan Status Beasiswa.

## Menjalankan Sistem Machine Learning
Aplikasi web prototype dibuat menggunakan Streamlit untuk memprediksi status mahasiswa secara individual berdasarkan data input akademik dan status finansial.
- Link Prototype Machine Learning: https://submission-akhir-dvk8snqgkabhtgxmdb5frz.streamlit.app/
- Cara Menjalankan Secara Lokal: streamlit run app.py


## Conclusion
Berdasarkan analisis data pada notebook dan visualisasi pada dashboard, didapatkan kesimpulan sebagai berikut:
1. **Rasio Dropout:** Dari total 4.424 mahasiswa pada dataset awal, terdapat 1.421 mahasiswa yang mengalami *dropout* (Dropout Rate sebesar 32,12%). Untuk keperluan pemodelan Machine Learning, 794 data berstatus *Enrolled* dipisahkan dari dataset *training* untuk mencegah ambiguitas target.
2. **Pengaruh Finansial (SPP):** Penunggakan SPP merupakan faktor penentu paling dominan. Sebesar 86,55% mahasiswa yang menunggak SPP berujung *dropout*, sementara mahasiswa dengan SPP lancar memiliki tingkat kelulusan mencapai 55,95%.
3. **Pengaruh Beasiswa:** Mahasiswa non-beasiswa memiliki tingkat *dropout* sebesar 38,71% (3x lipat lebih tinggi) dibandingkan penerima beasiswa yang angka *dropout*-nya hanya 12,19% (dengan tingkat kelulusan 75,98%).
4. **Performa Model Machine Learning:** Model dikembangkan menggunakan *Random Forest Classifier* dengan target klasifikasi biner murni (**1 = Dropout** dan **0 = Graduate**). Data *Enrolled* dikeluarkan penuh dari proses *training* untuk mengeliminasi *data leakage*. Model terbaru telah diekspor dan disimpan pada `model/model.joblib`.
5. **Evaluasi Matriks Pemodelan:** Berdasarkan pengujian pada 726 data uji (*test set*), model biner ini menghasilkan performa yang sangat presisi:
   - **Akurasi:** 92,15%
   - **Precision:** 92% (0,92)
   - **Recall:** 91% (0,91)
   - **F1-Score:** 92% (0,92)
6. *(Khusus deteksi kelas **Dropout**, model berhasil mencapai Precision 92%, Recall 88%, dan F1-Score 90%).*

### Rekomendasi Action Items
- **Sistem Intervensi Finansial Dini:** Mewajibkan tim keuangan untuk memberikan opsi cicilan atau dana bantuan darurat bagi mahasiswa yang mengalami kendala pembayaran SPP sebelum memasuki periode ujian.
- **Optimalisasi & Perluasan Beasiswa:** Memprioritaskan alokasi beasiswa berbasis kebutuhan ekonomi (*need-based scholarship*) untuk mahasiswa kelompok ekonomi rentan guna menahan angka *dropout*.
- **Bimbingan Akademik Khusus Semester Awal:** Menyelenggarakan program pendampingan (*tutoring*) intensif bagi mahasiswa yang gagal meluluskan mayoritas mata kuliah pada Semester 1 dan 2.
