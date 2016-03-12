from flask import Flask

# Criando instacia principal do Flask
app = Flask(__name__)

# Rota para pagina inicial (home)
@app.route('/')
def home():
    return 'hello world -- Academic forge'


if __name__ == '__main__':
    app.run(debug=True)