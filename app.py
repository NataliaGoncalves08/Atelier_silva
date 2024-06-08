from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
  return render_template('inicio.html')

@app.route('/criar_pedido')
def criar_pedido():
  return render_template('criar_pedido.html')

@app.route('/finalizacao')
def finalizacao():
  return render_template('finalizar.html')
  
if __name__ == '__main__':
    app.run(debug=True)
