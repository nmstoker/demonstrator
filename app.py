from flask import Flask, render_template, request, jsonify
from playwright.sync_api import sync_playwright
import pdfplumber
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'url' in request.form and len(request.form['url'].strip()) > 0:
            url = request.form['url']
            extracted_data = scrape_url(url)
            source_type = "Web page"
        elif 'file' in request.files:
            file = request.files['file']
            extracted_data = extract_text_from_pdf(file)
            source_type = "PDF file"
        else:
            return "Invalid input", 400
        
        extracted_text = extracted_data[0]
        title = extracted_data[1]
        # Call the external API
        result = call_external_api(extracted_text)
        
        return render_template('result.html', result=result, source_type=source_type, title=title)
    return render_template('index.html')

def scrape_url(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text("body")
        title = page.title()
        browser.close()
    return content, title

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = '\n'.join(page.extract_text() for page in pdf.pages)
        title = file.filename
    return text, title

def call_external_api(text):
    # Placeholder for calling the external API.
    hdr = {"Content-Type": "application/json"}
    response = requests.post('http://127.0.0.1:5001/process', json={"text": text}, headers=hdr)

    return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
