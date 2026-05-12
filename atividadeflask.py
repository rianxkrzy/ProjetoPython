from flask import Flask

app = Flask(__name__)


@app.route('/decorator')
def decorator_explicacao():
    return """<!DOCTYPE html>
<html lang=\"pt-BR\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Decorator em Python</title>
</head>
<body>
  <h1>Conceito de decorator em Python</h1>

  <h2>1) O que é um decorator em Python?</h2>
  <p>
    Um <strong>decorator</strong> (decorador) é uma forma de <strong>adicionar comportamento</strong>
    a uma função (ou método) sem precisar alterar diretamente o código original dela.
  </p>
  <p>
    Em geral, um decorator recebe uma função como entrada e retorna outra função
    (geralmente “envolvendo” a original), podendo executar ações antes e/ou depois.
  </p>

  <h2>2) Para que ele serve?</h2>
  <ul>
    <li><strong>Reaproveitar lógica</strong>: validações, logs e tratamento de exceções.</li>
    <li><strong>Manter o código organizado</strong>: separa preocupações (ex.: autenticação).</li>
    <li><strong>Evitar duplicação</strong>: reaplica o mesmo comportamento em várias funções.</li>
    <li><strong>Adicionar funcionalidades</strong> sem mudar a assinatura da função.</li>
  </ul>

  <h2>3) Como ele é utilizado no Flask (exemplo: @app.route)</h2>
  <p>
    No Flask, decorators são usados para <strong>registrar rotas</strong>. Quando você escreve
    <code>@app.route('/')</code>, você está usando um decorator para dizer ao Flask
    qual função deve ser chamada quando uma URL for acessada.
  </p>

  <h3>Exemplo (ideia do Flask)</h3>
  <pre>
@app.route('/')
def home():
    return 'Página inicial'
  </pre>

  <p>
    Portanto, o decorator <code>@app.route</code> conecta a URL com a função Python
    que vai gerar a resposta.
  </p>
</body>
</html>"""


if __name__ == '__main__':
    app.run(debug=True)

