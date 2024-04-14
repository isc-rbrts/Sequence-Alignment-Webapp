from flask import Flask, request, redirect, url_for, render_template
from algorithm import GlobalAlignment

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
       match_reward = float(request.form.get("match_reward"))
       mismatch_penalty = float(request.form.get("mismatch_penalty"))
       indel_penalty = float(request.form.get("indel_penalty"))

       score, v, w = GlobalAlignment(match_reward, mismatch_penalty, indel_penalty, seq1, seq2)

       return render_template("result.html", score=score, v=v, w=w, align_type=align_type, 
                              seq1=seq1, seq2=seq2, match_reward=match_reward, 
                              mismatch_penalty=mismatch_penalty, indel_penalty=indel_penalty)
    
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)