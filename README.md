# Marathi Sentiment Analysis 🇮🇳

## 📌 Problem Statement
This project performs emotion classification on Marathi text. The dataset contains English text and its Marathi translation, labeled with emotions such as joy, anger, sadness, fear, etc.

---

## ⚙️ Pipeline

English Text → Cleaning → Translation (Google Sheets) → Marathi Cleaning → Vectorization → Classification

---

## 🧠 Techniques Used

- Text Cleaning (neattext, regex)
- Marathi NLP preprocessing (mahaNLP)
- Feature Extraction:
  - CountVectorizer
  - TF-IDF (optional)
- Model:
  - Logistic Regression

---

## 📊 Evaluation

- Accuracy Score
- Classification Report (Precision, Recall, F1-score)

---

## ⚠️ Challenges Faced

- Handling noisy text (mentions, hashtags, emojis)
- Marathi text normalization
- Encoding issues (UTF-8 handling in CSV files)

---

## 🔥 Unique Aspects

- Regional language NLP (Marathi)
- Custom preprocessing pipeline
- End-to-end ML workflow from raw data to prediction

---

## 🚀 Future Improvements

- Use transformer-based models (IndicBERT, mBERT)
- Improve translation quality
- Deploy as REST API (FastAPI)
- Add real-time prediction UI

---
