# 📰 Fake News Detection System

## 📌 Overview
The Fake News Detection System is a Machine Learning-based web application that classifies news articles as **Fake** or **Real** using Natural Language Processing (NLP) techniques and Logistic Regression.

The project consists of:
- Model training notebook (`fake_News.ipynb`)
- Saved trained model (`fake_news_model.pkl`)
- Saved TF-IDF vectorizer (`vectorizer.pkl`)
- Flask web application for real-time prediction

---

## 🚀 Features

- Text preprocessing (Regex cleaning, lowercasing)
- Stopword removal using NLTK
- Porter Stemming
- TF-IDF Vectorization
- Logistic Regression classifier
- Confusion Matrix & performance evaluation
- 95.94% model accuracy
- Flask-based web interface

---

## 🧠 Machine Learning Workflow

1. Data Cleaning using Regular Expressions  
2. Convert text to lowercase  
3. Remove English stopwords (NLTK)  
4. Apply Porter Stemming  
5. Convert text into TF-IDF numerical features  
6. Train Logistic Regression model  
7. Evaluate using Confusion Matrix & metrics  
8. Save trained model and vectorizer using Pickle  

---

## 📊 Model Performance

### Confusion Matrix

|                | Predicted Fake | Predicted Real |
|---------------|---------------|---------------|
| Actual Fake   | 6650          | 356           |
| Actual Real   | 229           | 7192          |

### Performance Metrics

- Accuracy: **95.94%**
- Precision: **95.28%**
- Recall: **96.91%**
- F1-Score: **96.09%**

---

## 🌐 Web Application

The Flask web application allows users to:

- Enter news content
- Click Predict
- Receive output: Fake News ❌ or Real News ✅

Run locally at:

http://127.0.0.1:5000

## 📁 Project Structure

```
Fake-News-Detection/
│
├── fake_News.ipynb
├── app.py
├── fake_news_model.pkl
├── vectorizer.pkl
│
├── template/
│   ├── index.html
│   └── style.css
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

git clone <your-repository-link>  
cd Fake-News-Detection  

### 2️⃣ Install Dependencies

pip install -r requirements.txt  

Or manually:

pip install flask nltk scikit-learn numpy pandas matplotlib seaborn  

### 3️⃣ Download NLTK Stopwords (Run Once)

```python
import nltk
nltk.download('stopwords')

4️⃣ Train Model (Optional)

Open fake_News.ipynb and run all cells to retrain the model.

5️⃣ Run Web Application

python app.py

Then open:

http://127.0.0.1:5000

🛠 Technologies Used

Python

Scikit-learn

NLTK

Flask

HTML

CSS

Pandas

NumPy

Matplotlib

Seaborn

🔮 Future Improvements

Add Deep Learning model (LSTM / BERT)

Add prediction confidence score

Deploy on cloud platform (Render / Railway)

Add REST API support

Add multi-class fake news detection

Improve UI using Bootstrap

👨‍💻 Author

Gaurav Kumar
B.Tech Computer Science Engineering
Machine Learning & AI Enthusiast

GitHub: https://github.com/NAME-GAURAV-KUMAR

LinkedIn: https://www.linkedin.com/in/gaurav-kumar-96655b28a/
