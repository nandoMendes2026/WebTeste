from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return render_template("inicio.html")

@app.route("/usuario/<nome_usuario>")
def getUsuer(nome_usuario):
    return "Olá "+ nome_usuario

if __name__=="__main__":
    app.run(debug=True)



