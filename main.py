from flask import Flask
import random
import string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>' '<a href="/random_fact">¡Ver un dato aleatorio!</a>' '<a href="/password">Generador de contraseñas</a>'
        
@app.route("/random_fact")
def dato():
    return '<h2>¿Sabías que las tortugas marinas pueden vivir entre 50 y 100 años?</h2>'

@app.route("/password")
def generar_password():
    longitud = 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))

    return f"""
    <h2>Contraseña generada:</h2>
    <p>{password}</p>
    <a href="/password">Generar otra</a><br>
    <a href="/">Volver al inicio</a>
    """
app.run(debug=True)
