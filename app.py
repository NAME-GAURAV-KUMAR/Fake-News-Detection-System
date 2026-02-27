from flask import Flask, render_template, request
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__,template_folder='template',static_folder='template')

# Load model and vectorizer
model = pickle.load(open("Fake-news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

port_stem = PorterStemmer()
stop_words = set(stopwords.words('english'))

def stemming(content):
    content = re.sub('[^a-zA-Z]', ' ', content)
    content = content.lower()
    content = content.split()
    content = [port_stem.stem(word) for word in content if word not in stop_words]
    return ' '.join(content)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']
    processed = stemming(news)
    vectorized = vectorizer.transform([processed])
    prediction = model.predict(vectorized)

    if prediction[0] == 0:
        result = "Fake News ❌"
    else:
        result = "Real News ✅"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)