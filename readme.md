# pdf2excel

  

This project provides a Python script to extract tables from PDF files and convert them into a single Excel workbook.
It utilizes the `camelot` library for robust table detection and extraction from PDF documents, and `pandas` for efficient data handling and output to the Excel format.
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
python3 app.py
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