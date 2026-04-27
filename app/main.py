from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recetas")
def recetas():
    return render_template("index.html")

@app.route("/dietas")
def dietas():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)