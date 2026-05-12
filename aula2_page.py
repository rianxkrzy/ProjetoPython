from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Rian Ribeiro</li>  
                <li><strong>Email:</strong> rianmirandaribeiroo@cotemig.com.br</li>
                <li><strong>Telefone:</strong> (31) 97174-6497</li>
            </ul>

            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Empresa:</strong> Loca Exata</li>
                <li><strong>Cargo:</strong> Estagiario T.i</li>
                <li><strong>Período:</strong> Dez 2025 - Presente</li>
            </ul>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
