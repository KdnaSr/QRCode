from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Lê o Excel e cria um dicionário com os dados
df = pd.read_excel("usuarios.xlsx")
usuarios = df.set_index("id").to_dict(orient="index")

@app.route("/")
def home():
    return "Use os QRCodes para acessar os dados dos usuários."

@app.route("/usuario/<int:user_id>")
def mostrar_usuario(user_id):
    usuario = usuarios.get(user_id)
    if usuario:
        return render_template("usuario.html", usuario=usuario)
    else:
        return "Usuário não encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)
