# Demonstrator

## App
- initial config
conda create -n demonstrator_application python=3.10
conda activate demonstrator_application
pip install Flask requests pdfplumber playwright
playwright install chromium

// flask --app app run
python app.py

## API
- initial config
conda create -n demonstrator_api python=3.11
conda activate demonstrator_api
pip install Flask

// flask --app api run
python api.py

- call it with JSON body containing the parameter "text"
http://127.0.0.1:5001/process

- now we'll adapt it to do something useful with the API