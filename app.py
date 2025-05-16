from flask import Flask, request, send_file, jsonify
import pandas as pd
import camelot
import tempfile
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_pdfs():
    if 'pdfFiles' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400
    files = request.files.getlist('pdfFiles')
    if not files or files[0].filename == '':
        return jsonify({'error': 'No selected files'}), 400

    main_tables = pd.DataFrame()
    temp_files = []

    try:
        for file in files:
            # Save PDF to a temporary file
            temp = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
            file.save(temp.name)
            temp_files.append(temp.name)
            temp.close()

        for pdf_path in temp_files:
            try:
                tables = camelot.read_pdf(pdf_path, pages='all')
                for table in tables:
                    main_tables = pd.concat([main_tables, table.df], ignore_index=True)
            except Exception as e:
                print(f"Error processing {pdf_path}: {e}")

        # Export to Excel
        output = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
        main_tables.to_excel(output.name, index=False)
        output.close()

        return send_file(output.name, as_attachment=True, download_name='all_tables.xlsx')
    finally:
        # Clean up temp files
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)

if __name__ == '__main__':
    app.run(debug=True, port=8080) 