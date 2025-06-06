from flask import Flask, request, jsonify

app = Flask(__name__)
articles = []

@app.route('/')
def home():
    return "Bienvenue dans mon application Flask ! 🚀"

@app.route('/articles', methods=['GET'])
def get_articles():
    return jsonify(articles)

@app.route('/articles', methods=['POST'])
def add_article():
    data = request.json
    articles.append(data['article'])
    return jsonify({'message': 'Article ajouté avec succès ! 🚀'}), 201

@app.route('/articles/<int:index>', methods=['PUT'])
def update_article(index):
    data = request.get_json()
    articles[index] = data['article']
    return jsonify({'message': 'Article mis à jour 🔄'})

@app.route('/articles/<int:index>', methods=['DELETE'])
def delete_article(index):
    articles.pop(index)
    return jsonify({'message': 'Article supprimé 🗑️'})

if __name__ == '__main__':
    app.run(debug=True, port=5005)
