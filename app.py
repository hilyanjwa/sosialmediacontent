from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# 🔥 Load model (bukan dict, langsung model)
model = joblib.load("model.joblib")
ACCURACY = None  # karena model kamu tidak simpan accuracy

# 🔥 Mapping kategori (HARUS sesuai training kamu)
platform_map = {
    "Instagram": 0,
    "TikTok": 1,
    "X": 2,
    "YouTube Shorts": 3
}

content_type_map = {
    "carousel": 0,
    "image": 1,
    "text": 2,
    "video": 3
}

topic_map = {
    "Education": 0,
    "Entertainment": 1,
    "Lifestyle": 2,
    "Politics": 3,
    "Sports": 4,
    "Technology": 5
}

language_map = {
    "en": 0,
    "es": 1,
    "fr": 2,
    "hi": 3,
    "ur": 4
}

region_map = {
    "Brazil": 0,
    "India": 1,
    "Pakistan": 2,
    "UK": 3,
    "US": 4
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    error = None

    if request.method == "POST":
        try:
            # Ambil input
            platform = platform_map[request.form["platform"]]
            content_type = content_type_map[request.form["content_type"]]
            topic = topic_map[request.form["topic"]]
            language = language_map[request.form["language"]]
            region = region_map[request.form["region"]]

            comments = float(request.form["comments"])
            shares = float(request.form["shares"])
            sentiment_score = float(request.form["sentiment_score"])

            post_day = int(request.form["post_day"])
            post_month = int(request.form["post_month"])
            post_weekday = int(request.form["post_weekday"])

            hashtags_count = int(request.form["hashtags_count"])

            # Susun fitur
            features = np.array([[
                platform,
                content_type,
                topic,
                language,
                region,
                comments,
                shares,
                sentiment_score,
                post_day,
                post_month,
                post_weekday,
                hashtags_count
            ]])

            # Prediksi
            hasil = model.predict(features)[0]
            proba = model.predict_proba(features)[0]
            confidence = round(max(proba) * 100, 1)

            prediction = "Viral" if hasil == 1 else "Tidak Viral"

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        error=error,
        accuracy=(round(ACCURACY * 100, 1) if ACCURACY else None)
    )

if __name__ == "__main__":
    app.run(debug=True)