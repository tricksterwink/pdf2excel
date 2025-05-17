# pdf2excel

  

This is a Flask web app that extracts tables from PDF files and converts them into a single Excel workbook. It leverages the `camelot` library for reliable table detection and extraction, and uses `pandas` for efficient data processing and Excel output.

## Installation
1. Clone the repository:

```
git clone https://github.com/tricksterwink/pdf2excel.git
cd pdf2excel
```
2. Install the required Python libraries, including `camelot`:

```
pip install -r requirements.txt
```

You may also need to install Ghostscript separately if you encounter issues with `camelot`. Refer to the `camelot` documentation for details.

3. Run the flask app on localhost:
```
python3 run.py
```

## Project structure:

```
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── __pycache__/
|   |   |__ __init__.cpython-313.pyc
│   └── static/
│   |   └── style.css
|   |__ templates/
|   |   |__ index.html
├── run.py
├── wsgi.py
├── requirements.txt
└── readme.md
```