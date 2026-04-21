# 🚀 Flask App — Viral Content Prediction

Aplikasi ini merupakan implementasi deployment Machine Learning menggunakan Flask untuk memprediksi apakah sebuah konten media sosial akan menjadi **viral atau tidak**.

---

## 📁 Struktur Folder

```
sosialmedia_flask/
│
├── app.py
├── model.joblib
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

---

## 🧠 Informasi Model

* Algoritma: Gradient Boosting Classifier
* Tipe: Classification
* Target:

  * 1 → Viral
  * 0 → Tidak Viral

---

## 📊 Fitur yang Digunakan

* platform
* content_type
* topic
* language
* region
* comments
* shares
* sentiment_score
* post_day
* post_month
* post_weekday
* hashtags_count

---

## ⚙️ Setup Awal

### 1. Buat Virtual Environment

```bash
python3 -m venv venv
```

### 2. Aktifkan Virtual Environment

```bash
# Mac / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Aplikasi

```bash
python app.py
```

Buka di browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Cara Menggunakan

1. Pilih kategori:

   * Platform
   * Content Type
   * Topic
   * Language
   * Region

2. Masukkan nilai:

   * Comments
   * Shares
   * Sentiment Score
   * Post Day
   * Post Month
   * Post Weekday
   * Jumlah Hashtag

3. Klik tombol **Prediksi**

---

## 📈 Output

* Hasil Prediksi (Viral / Tidak Viral)
* Confidence Score
* Akurasi Model

---

## ⚠️ Catatan

* Mapping kategori menggunakan Label Encoding
* Pastikan input sesuai dengan data training
* File model.joblib harus berada di folder yang sama dengan app.py

---

## 🔧 Troubleshooting

### Error: Module not found

```bash
pip install flask numpy joblib scikit-learn
```

### Error: Model tidak terbaca

* Pastikan file model.joblib tersedia
* Pastikan path sudah benar

---

## 💡 Pengembangan

* Tambahkan visualisasi data
* Tambahkan database
* Deploy ke internet

---

## 👨‍💻 Author

Project ini dibuat untuk pembelajaran deployment Machine Learning menggunakan Flask.
