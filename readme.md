# PDF to Excel Converter

A Flask web app that extracts tables from PDF files and converts them into a single Excel workbook. It uses `camelot` for table extraction and `pandas` for data manipulation. It is Containerized using Docker. 

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python run.py
   ```
   Visit `http://localhost:5000`

### With Docker
```bash
docker build -t pdf2excel .
docker run -p 5000:8080 pdf2excel
```

## Project Structure

```
pdf2excel/
├── app/                  # Application code
│   ├── __init__.py       # Main Flask app
│   ├── static/           # CSS/JS assets
│   └── templates/        # HTML templates
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
└── run.py                # Entry point
```