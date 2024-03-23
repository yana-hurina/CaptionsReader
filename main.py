from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from window import Ui_Dialog
from PySide6.QtCore import QThread
from PySide6.QtGui import QIcon
from screenshots_reader import Reader
import socket
import resources_rc


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.authorized_user_ids = ['syana', 'kyana', 'tyana', 'yana']
        self.isProcessing = False
        self.file_path = None
        self.thread = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initialize_ui_states()
        self.connect_signals()
        self.check_fields_filled()
        self.current_user_id = ''.join([c for c in socket.gethostname()[-4:] if c.isalpha()])

    def initialize_ui_states(self):
        self.ui.process.setEnabled(False)
        self.file_path = {'doc': None}

        word_widgets = [self.ui.word_file]

        for widget in word_widgets:
            widget.mousePressEvent = self.open_word_file_dialog
            widget.addItem("Click to select an Word file...")

    def connect_signals(self):
        self.ui.process.clicked.connect(self.process_file)

    def open_word_file_dialog(self, event):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Word File", "", "Word Files (*.doc *.docx)")
        if filePath:
            fileName = filePath.split("/")[-1]
            self.ui.word_file.clear()
            self.ui.word_file.addItem(fileName)
            self.file_path['doc'] = filePath
            self.check_fields_filled()

    def process_file(self):
        # Check if the current user is authorized
        user_authorized = self.current_user_id in self.authorized_user_ids

        if not user_authorized:
            QMessageBox.warning(self, "Access Denied", "You do not have access to perform this action.")
            return  # Exit the method to prevent further processing

        # Existing check for ongoing processing
        if self.isProcessing:
            QMessageBox.warning(self, "Processing", "Please wait for the current processing to complete.")
            return  # Prevent starting a new process if one is already active

        self.isProcessing = True  # Set the flag when starting a new process

        self.thread = QThread()  # Create a new thread
        self.worker = Reader(self.file_path['doc'])  # Create a new worker
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.process)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.on_processing_finished)
        # Update the flag when the process is finished
        self.worker.finished.connect(lambda: setattr(self, 'isProcessing', False))
        # Schedule the worker and thread for deletion without directly accessing them afterwards
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
        self.ui.process.setEnabled(False)
        self.setEnabled(False)

        self.progressDialog = QMessageBox(self)
        self.progressDialog.setWindowTitle("Processing")
        self.progressDialog.setText("Processing, please wait...")
        self.progressDialog.setStandardButtons(QMessageBox.NoButton)
        self.progressDialog.show()

    def on_processing_finished(self):
        self.progressDialog.accept()
        self.setEnabled(True)
        self.ui.process.setEnabled(True)
        QMessageBox.information(self, "Processing Complete", "The processing has been completed.")

    def check_fields_filled(self):
        excel_file_selected = self.file_path['doc'] is not None
        self.ui.process.setEnabled(excel_file_selected)

    def closeEvent(self, event):
        if self.isProcessing:  # Check if processing is ongoing
            reply = QMessageBox.question(self, 'Processing',
                                         "A process is still running. Are you sure you want to quit?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                if self.thread:  # Safely attempt to stop the thread if it exists
                    self.worker.stop()  # Ensure this method exists in your worker to stop processing
                    self.thread.quit()
                    self.thread.wait(2000)  # Wait for a maximum of 2000 milliseconds for the thread to finish
                event.accept()  # Accept the close event
            else:
                event.ignore()  # Ignore the close event, keeping the application open
        else:
            event.accept()  # No processing is active, safe to close


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/icon"))
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
