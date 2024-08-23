from flask import Flask, jsonify, request
from flask_cors import CORS 
import google.generativeai as gemini  

app = Flask(__name__)
CORS(app) 


gemini.configure(api_key="sua chave aqui")
model = gemini.GenerativeModel('gemini-1.5-flash')  # Inicializa o modelo generativo

@app.route('/historia', methods=['POST'])
def make_historia():
    try:
        # Extrai os dados do corpo da requisição
        dados = request.json
        elementos = dados.get('elementos')

        # Define o prompt para gerar a história
        prompt = f"""
        Crie um conto infantil utilizando os seguintes elementos: {elementos}.
        Siga esses critérios:
        - Assegure-se de que o texto esteja bem estruturado e coerente sem palavras ou conceitos inapropiados para crianças.
        - A ortografia deve ser correta
        - A história deve ser criativa e moralmente correta, se palavras ofensivas forem utilizadas apresente uma mensagem de erro em <h1>
        - O formato deve ser HTML com codificação UTF-8, sem o cabeçalho HTML.
        - O título da história deve ser formatado com a tag <h1> e deve estar acompanhado de um emoji de livro.
        - Os capítulos devem ser de tamanhos parecidos devem ser formatados com a tag <h2> contendo um título adequado e um emoji correspondente a um dos elementos fornecidos pelo usuário presentes na história.
        - A narração deve ser apresentada em parágrafos, usando a tag <p>.
        - Os diálogos devem ser apresentados entre aspas.
        - No final da história, em adicione uma moral em um parágrafo centralizado no meio com a tag <strong>.
        """

        # Gera o conteúdo da história usando o modelo
        resposta = model.generate_content(prompt)
        print(resposta)

        # Extrai a história do texto da resposta
        historia = resposta.text.strip().split('\n')
        return (historia), 200  # Retorna a história com o status 200 (OK)

    except Exception as e:
        # Retorna um erro no caso de exceção
        return jsonify({"Erro": str(e)}), 300
    
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo debug
