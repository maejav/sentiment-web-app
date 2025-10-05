from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from flask_cors import CORS

# To avoid CORS and file:// issues, let Flask serve your HTML and static files.
# using Flask to serve the HTML, and just testing locally
#Use CSS for static design and layout, and JavaScript for dynamic behavior.

app = Flask(__name__)
CORS(app)


# Load sentiment analysis pipeline from Hugging Face
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    result = sentiment_model(text)[0]
    return jsonify({
        "label": result["label"],
        "score": round(result["score"], 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
