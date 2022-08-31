from flask import Flask, render_template
from flask import request, redirect
from calculadora import calculadora
import this

app = Flask(__name__)  # Referência ao objeto FLASK, criando uma variável APP que guarda os elementos do FLASK
calc = calculadora()
this.resultadoFinal= ""

@app.route("/")  # Página Index = Primeira Página de Qualquer Site
def homepage():
    return render_template("index.html")


@app.route("/soma", methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.somar(numero1,numero2)
    return render_template("soma.html", titulo="Soma", resultado=this.resultadoFinal)

@app.route("/subtracao", methods=['POST', 'GET'])
def subt():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.subtrair(numero1,numero2)
    return render_template("subtracao.html", titulo="Subtrair", resultado=this.resultadoFinal)

@app.route("/divisao", methods=['POST', 'GET'])
def div():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.dividir(numero1,numero2)
    return render_template("divisao.html", titulo="Dividir", resultado=this.resultadoFinal)

@app.route("/multiplicacao", methods=['POST', 'GET'])
def mult():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.multiplicar(numero1,numero2)
    return render_template("multiplicacao.html", titulo="Multiplicar", resultado=this.resultadoFinal)

@app.route("/potencia", methods=['POST', 'GET'])
def pot():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.potencia(numero1,numero2)
    return render_template("potencia.html", titulo="Potencia", resultado=this.resultadoFinal)

@app.route("/raiz", methods=['POST', 'GET'])
def rai():
    if request.method == 'POST':
        numero = request.form['num']
        
        this.resultadoFinal = calc.raiz(numero)
    return render_template("raiz.html", titulo="Raiz", resultado=this.resultadoFinal)

@app.route("/tabuada", methods=['POST', 'GET'])
def tabu():
    if request.method == 'POST':
        numero = request.form['num']
        
        this.resultadoFinal = calc.tabuada(numero)
    return render_template("tabuada.html", titulo="Tabuada", resultado=this.resultadoFinal)



if __name__ == '__main__':
    app.run(debug=True)