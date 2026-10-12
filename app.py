
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    name = request.form.get("name", "")
    age = request.form.get("age", "")
    gender = request.form.get("gender", "")
    symptoms = request.form.get("symptoms", "")
    duration = request.form.get("duration", "")
    severity = request.form.get("severity", "")
    allergies = request.form.get("allergies", "")
    medications = request.form.get("medications", "")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Symptom Report</title>
        <style>
            body {{ font-family: Arial; background: #f1f6f8;
                    padding: 30px; color: #263746; }}
            .card {{ max-width: 650px; margin: auto; background: white;
                     padding: 25px; border-radius: 12px; }}
            h1 {{ color: #087e8b; }}
            p {{ line-height: 1.6; overflow-wrap: anywhere; }}
            a {{ color: #087e8b; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Patient Information Received</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>Age:</b> {age}</p>
            <p><b>Gender:</b> {gender or "Not provided"}</p>
            <p><b>Symptoms:</b> {symptoms}</p>
            <p><b>Duration:</b> {duration or "Not provided"}</p>
            <p><b>Reported severity:</b> {severity or "Not provided"}</p>
            <p><b>Allergies:</b> {allergies or "Not provided"}</p>
            <p><b>Medications:</b> {medications or "Not provided"}</p>
            <hr>
            <p>This demo has received your information but has not
            performed a medical analysis. Please consult a qualified
            healthcare professional for medical advice.</p>
            <a href="/">Back to form</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
