from flask import Flask, request, jsonify
from keybert import KeyBERT

app = Flask(__name__)
kw_model = KeyBERT()

@app.route('/process', methods=['POST'])
def process_text():
    try:
        # Get the input parameter 'text' from the JSON request
        data = request.get_json()
        input_text = data.get('text', '')

        # Perform some processing on the input text (you can replace this with your actual processing logic)
        #processed_text = input_text.upper()
        keywords = kw_model.extract_keywords(input_text, keyphrase_ngram_range=(1, 2), stop_words="english")
        #keywords = [f"{kw[0]} ({kw[1]})" for  kw in keywords]

        # Create a response JSON
        response = {
            'input_text': input_text,
            'keywords': keywords
        }

        return jsonify(response), 200

    except Exception as e:
        print('error', str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
