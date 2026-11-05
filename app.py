from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Passando dados do Python
    return render_template(
        "index.html",
        usuario="Maria"
    )

if __name__ == "__main__":
    app.run(debug=True,port=4000)