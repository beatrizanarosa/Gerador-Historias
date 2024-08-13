from flask import Flask, jsonify, request
from flask_cors import CORS 
import google.generativeai as gemini  

app = Flask(__name__)
CORS(app) 


gemini.configure(api_key="AIzaSyCo4yy6nQT_ceYE1H-BTBn0I7xbGH55c9I")
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
        A história deve ser apresentada no formato HTML com codificação UTF-8, sem o cabeçalho HTML.
        O título da história deve ser formatado com a tag <h1>.
        Os capítulos devem ser formatados com a tag <h2>.
        A narração deve ser apresentada em parágrafos, usando a tag <p>.
        Os diálogos devem ser apresentados entre aspas.
        No final da história, adicione uma moral em um parágrafo destacado com a tag <strong>.
        Assegure-se de que o texto esteja bem estruturado e coerente para rianças com os elementos fornecidos.
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
