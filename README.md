# Text Processing Demonstrator

A simple text processing demonstrator that can process text either from a PDF or directly from a web page.

## App

- initial config

conda create -n demonstrator_application python=3.10

conda activate demonstrator_application

pip install Flask requests pdfplumber playwright

playwright install chromium

python app.py

## API

- initial config

conda create -n demonstrator_api python=3.10

conda activate demonstrator_api

pip install Flask

python api.py

- call it with JSON body containing the parameter "text"

http://127.0.0.1:5001/process

- now we'll adapt it to do something useful with the API

pip install keybert