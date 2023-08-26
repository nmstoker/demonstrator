from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_text():
    print("process_text started")
    try:
        # Get the input parameter 'text' from the JSON request
        data = request.get_json()
        print("here...")
        input_text = data.get('text', '')
        print("now here...")

        # Perform some processing on the input text (you can replace this with your actual processing logic)
        processed_text = input_text.upper()
        print(f"{processed_text=}")

        # Create a response JSON
        response = {
            'input_text': input_text,
            'processed_text': processed_text
        }

        return jsonify(response), 200

    except Exception as e:
        print('error', str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
