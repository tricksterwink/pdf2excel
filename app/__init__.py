from flask import Flask, request, send_file, jsonify, render_template
import pandas as pd
import camelot
import tempfile
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdfs():
    if 'pdfFiles' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400
    files = request.files.getlist('pdfFiles')
    if not files or files[0].filename == '':
        return jsonify({'error': 'No selected files'}), 400

    temp_files = []

    try:
        for file in files:
            # Save PDF to a temporary file
            temp = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
            file.save(temp.name)
            temp_files.append((temp.name, file.filename))
            temp.close()

        # Create a temp Excel file and get its path
        temp_excel = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
        excel_path = temp_excel.name
        temp_excel.close()

        with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
            for pdf_path, orig_filename in temp_files:
                try:
                    tables = camelot.read_pdf(pdf_path, pages='all')
                    dfs = []
                    for table in tables:
                        df = table.df
                        df.columns = df.iloc[0]
                        df = df[1:]
                        dfs.append(df)
                    if dfs:
                        combined_df = pd.concat(dfs, ignore_index=True)
                        sheet_name = os.path.splitext(orig_filename)[0][:31]
                        sheet_name = ''.join(c if c.isalnum() or c in ' _-' else '_' for c in sheet_name)
                        combined_df.to_excel(writer, sheet_name=sheet_name, index=False)
                except Exception as e:
                    print(f"Error processing {pdf_path}: {e}")

        return send_file(excel_path, as_attachment=True, download_name='all_tables.xlsx')
    finally:
        # Clean up temp files
        for f, _ in temp_files:
            if os.path.exists(f):
                os.remove(f)
