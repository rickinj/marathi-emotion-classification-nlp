# Marathi Emotion Classification 🇮🇳

## 📌 Problem Statement
This project performs emotion classification on Marathi text. The dataset contains English text and its Marathi translation, labeled with emotions such as joy, anger, sadness, fear, etc.

---

## ⚙️ Pipeline

English Text  
→ Cleaning  
→ Translation (Google Sheets)  
→ Marathi Cleaning  
→ Vectorization  
→ Classification  

---

## 📁 Project Structure

```

marathi-emotion-classification-nlp/
│
├── data/
│ ├── emotions_marathi_text.csv # Raw dataset
│ ├── processed_dataset.csv # Cleaned dataset
│
├── notebook/
│ ├── final_model.ipynb # Main training notebook
│
├── src/
│ ├── preprocessing.py # Text cleaning pipeline
│ ├── model.py # Model building & evaluation
│
├── requirements.txt
├── README.md

```


---

## 🧠 Techniques Used

### 🔹 Text Preprocessing
- neattext (noise removal)
- Regex (mentions, hashtags, URLs)
- mahaNLP (Marathi normalization & stopwords)

### 🔹 Feature Extraction
- CountVectorizer
- TF-IDF (optional)

### 🔹 Model
- Logistic Regression

---

## 📊 Evaluation

- Accuracy Score  
- Classification Report:
  - Precision
  - Recall
  - F1-score  

---

## ⚠️ Challenges Faced

- Handling noisy social media text (mentions, emojis, hashtags)
- Marathi text normalization and preprocessing
- Encoding issues (UTF-8 handling in CSV files)

---

## 🔥 Unique Aspects

- Regional language NLP (Marathi)
- Custom preprocessing pipeline
- Multilingual workflow (English → Marathi)
- End-to-end ML pipeline

---

## 🚀 Future Improvements

- Transformer-based models (IndicBERT, mBERT)
- Better translation pipeline
- FastAPI deployment
- Real-time prediction UI

---

## 🧪 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/marathi-emotion-classification-nlp.git
cd marathi-emotion-classification-nlp
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run notebook
```bash
cd notebook
jupyter notebook
```

---

📈 Results
Achieved reliable performance using classical ML models
Demonstrated effectiveness of preprocessing in improving model accuracy

---
