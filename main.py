from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       align_type = request.form.get("align_type")
       seq1 = request.form.get("seq1")
       seq2 = request.form.get("seq2")
       match_reward = request.form.get("match_reward")
       mismatch_penalty = request.form.get("mismatch_penalty")
       indel_penalty = request.form.get("indel_penalty")

       return "Aligning sequences: " + seq1 + " " + seq2 + " with alignment type: " + align_type + " " + str(match_reward) + str(mismatch_penalty) + str(indel_penalty)
    
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)