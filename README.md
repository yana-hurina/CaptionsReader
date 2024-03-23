# CaptionsReader

CaptionsReader is a desktop application designed to read and extract text from images embedded in Word documents. 
Utilizing the power of EasyOCR, CaptionsReader provides an efficient solution for converting image-based captions 
into editable text. The application is built with PySide6, ensuring a smooth and user-friendly graphical interface.

## Features
- **Easy Navigation**: A straightforward UI to select and process Word documents.
- **OCR Processing**: Extracts text from images in Word documents using EasyOCR.
- **Threaded Processing**: Utilizes threading to keep the UI responsive during the extraction process.
- **Access Control**: Ensures that only authorized users can perform the text extraction process.

## Usage
* Start the application by running main.py.
* Click on the Word file input area to select a Word document for processing.
* Once a file is selected, the "Process" button will become active.
* Click "Process" to start extracting text from images within the document.
* After processing, the output will be saved in a text file with a similar name as the source document, 
appended with _output.
Note: You must be on the list of authorized users to process files.

## Installation
To use CaptionsReader, you will need to install the necessary Python packages. 
You can install all required packages using the following command:
```bash
pip install Pillow PySide6 python-docx easyocr numpy pyinstaller==5.13.2 python build.py
```

## Building the Application
To build CaptionsReader into a standalone executable, run the following command:
```bash
python build.py
```

This will generate a single executable file named CaptionsReader in the dist directory. 
The build process uses PyInstaller, configured to bundle the application along with all its dependencies 
into one file for easy distribution.

## Acknowledgments
EasyOCR for providing the OCR technology.
The PySide6 team for the GUI framework.
Python-docx for allowing manipulation of Word documents in Python.
