from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/inicio', methods=['POST'])
def homepage():
    texto = request.form['usuario']
    return render_template('homepage.html', resposta=texto)

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')


if __name__ == '__main__':
 app.run(debug=True)
