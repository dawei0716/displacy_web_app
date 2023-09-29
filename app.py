# Import the necessary libraries
from flask import Flask, render_template, request, jsonify
import spacy
from spacy import displacy

# Load the English NLP model
nlp = spacy.load("en_core_web_md")

# Initialize the Flask application
app = Flask(__name__)

# Define the index route
@app.route('/', methods=['GET'])
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse():
    # Get the sentence from the form
    sentence = request.json['sentence']
    # Process the sentence with spaCy NLP model
    doc = nlp(sentence)
    # Render the dependency visualization as HTML
    html = displacy.render(doc, style='dep')
    # Extract dep, pos, and tag for each token
    token_data = [{'text': token.text, 'dep': token.dep_, 'pos': token.pos_, 'tag': token.tag_} for token in doc]
    # Return the rendered HTML and token data
    return jsonify({'html': html, 'token_data': token_data})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)