from flask import Flask, request, render_template_string

app = Flask(__name__)

# Lista de usuários
usuarios = [
    {
        "usuario": "rian",
        "senha": "cotemig2026"
    },
    {
        "usuario": "dolga",
        "senha": "cotemig2026"
    },
    {
        "usuario": "janaina",
        "senha": "cotemig2026"
    },
    {
        "usuario": "antonio",
        "senha": "cotemig2026"
    }
]


# Tela de login
def mostrar_formulario():
    return render_template_string("""
        <h2>Login</h2>

        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>

            <input type="password" name="senha" placeholder="Senha"><br><br>

            <button type="submit">Entrar</button>
        </form>
    """)


# Função de login
def fazer_login():

    usuario_digitado = request.form.get("usuario")
    senha_digitada = request.form.get("senha")

    # Percorrendo a lista de dicionários
    for usuario in usuarios:

        if (
            usuario_digitado == usuario["usuario"]
            and senha_digitada == usuario["senha"]
        ):

            return f"<h1>Bem-vindo, {usuario_digitado}!</h1>"

    return "<h1>Login inválido!</h1>"


# Rota principal
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return fazer_login()

    return mostrar_formulario()


# Executar aplicação
if __name__ == "__main__":
    app.run(debug=True)