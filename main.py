from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       seq1 = request.form.get("seq1")
       seq2 = request.form.get("seq2") 

       return "Aligning sequences: " + seq1 + " " + seq2
    
    return render_template("home.html")

#if __name__ == "__main__":
#    app.run(host="127.0.0.1", port=8080, debug=True)