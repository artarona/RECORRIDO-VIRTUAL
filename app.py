# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Renderiza la plantilla con la imagen 360º
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)