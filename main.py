from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.text_edit = QTextEdit()
        self.text_edit.setFontPointSize(14)

        #menu buttons
        open_action = QAction("open", self)
        save_action = QAction("save", self)
        quit_action = QAction("Quit", self)

        #connecting menu buttons
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        quit_action.triggered.connect(self.close)

        #menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        central_widget.setLayout(layout)

    def open_file(self):
        file_path, _= QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py);;Text Files (*.txt);;All Files(*)")

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text_edit.setPlainText(file.read())

    def save_file(self):
        file_path, _= QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py);;Text Files (*.txt);;All Files (*)")

        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())
            QMessageBox.information(self, "File Saved", f"File saved successfuly: {file_path}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()