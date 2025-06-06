from flask import Flask, render_template, request

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

@app.route('/page')
def page_html():
    try:
        return render_template('page.html' , num_pages=12)
    except Exception as e:
        return f"Erreur: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5005)
