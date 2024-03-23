from docx import Document
from PIL import Image
import io
from PySide6.QtCore import QObject, Signal
import easyocr
import numpy as np


class Reader(QObject):
    finished = Signal()
    progress = Signal(int)

    def __init__(self, docx_path):
        super().__init__()
        self.docx_path = docx_path
        self._running = True  # Add a running flag
        self.reader = easyocr.Reader(['en'])  # Initialize the EasyOCR reader for English language

    def stop(self):  # Method to stop the processing
        self._running = False

    def process(self):
        images = self.extract_images()
        texts = self.extract_text_from_images(images)
        output_file_path = self.docx_path.rsplit('.', 1)[0] + '_output.txt'
        self.save_text_to_file(texts, output_file_path)
        self.finished.emit()

    def extract_images(self):
        """Extract images from a .docx file, attempting to preserve their order."""
        doc = Document(self.docx_path)
        images = []
        for rel in doc.part.rels.values():
            if "image" in rel.target_ref:
                img_blob = rel.target_part.blob
                image = Image.open(io.BytesIO(img_blob))
                images.append((rel.target_ref, image))

        # Sort images by their relationship ID
        images.sort(key=lambda x: x[0])
        return [image for _, image in images]

    def extract_text_from_images(self, images):
        """Use OCR to extract text from a list of PIL Image objects using EasyOCR,
        attempting to preserve some of the original formatting."""
        texts = []
        for img in images:
            img = img.convert('RGB')
            results = self.reader.readtext(np.array(img), paragraph=False)  # Get individual text blocks

            # Sort results by their vertical (top) position
            sorted_results = sorted(results, key=lambda x: x[0][0][1])

            last_bottom = 0
            text = ""
            for result in sorted_results:
                top_left, top_right, bottom_right, bottom_left = result[0]
                top, right, bottom, left = top_left[1], top_right[0], bottom_right[1], bottom_left[0]

                # If there's a significant vertical gap from the last text block, add a newline
                if top - last_bottom > 10:  # Threshold for vertical gap, adjust as needed
                    text += "\n"
                text += result[1] + " "
                last_bottom = bottom

            texts.append(text.strip())
        return texts

    def save_text_to_file(self, texts, file_path):
        """Save extracted text to a text file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for text in texts:
                    file.write(text + "\n\n")
            return True
        except Exception as e:
            return f"An error occurred while saving the file: {str(e)}"
