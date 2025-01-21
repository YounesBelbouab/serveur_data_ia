from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/api/V1/qui-suis-je", methods=["GET", "POST"])
def getName():
    return 'BELBOUAB Younes'

@app.route("/api/V1/<a>/<b>", methods=["GET", "POST"])
def addition(a, b):
    c = int(a) + int(b)
    return str(c)

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get('query')
    return f'recherche : {query}'

@app.route('/login', methods=["POST"])
def search_username():
    nom = request.form.get('username')
    mdp = request.form.get("mdp")
    return f'Nom : {nom} et mdp : {mdp}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)