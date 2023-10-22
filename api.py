from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
MAX_LENGTH = 4000 # apparent maximum length of acceptable input

@app.route('/process', methods=['POST'])
def process_text():
    try:
        # Get the input parameter 'text' from the JSON request
        data = request.get_json()
        input_text = data.get('text', '')

        min_length_input = int(data.get('from_input', 100))
        print(f"{min_length_input=}")
        max_length_input = int(data.get('to_input', 300))
        print(f"{max_length_input=}")

        # Perform some processing on the input text (you can replace this with your actual processing logic)
        #processed_text = input_text.upper()
        response = summarizer_pipeline(input_text[:MAX_LENGTH], max_length=max_length_input, min_length=min_length_input, do_sample=False)
        response = response[0] # contains dict entry 'summary_text'

        # Add input to the response JSON
        response['input_text'] = input_text

        return jsonify(response), 200

    except Exception as e:
        print('error', str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
