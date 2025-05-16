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
    
    Ensure your `requirements.txt` file includes:
    
    ```
    camelot-py[cv]
    pandas
    openpyxl
    ```
    
    You may also need to install Ghostscript separately if you encounter issues with `camelot`. Refer to the `camelot` documentation for details.