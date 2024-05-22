##
# QValidator class cannot be used because "'QValidator' represents a C++ abstract class and cannot be instantiated"
# Use QIntValidator or QDoubleValidator class
##

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QLabel
from PySide6.QtGui import QIntValidator

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 App with QIntValidator")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.input_label = QLabel("Enter an integer:")
        self.input_line_edit = QLineEdit()
        self.input_line_edit.setPlaceholderText("Type an integer")
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_line_edit)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        button = QPushButton("Check")
        button.clicked.connect(self.check_input)
        layout.addWidget(button)

        # Creating a QIntValidator to allow only integers
        self.int_validator = QIntValidator()
        self.input_line_edit.setValidator(self.int_validator)

    def check_input(self):
        input_text = self.input_line_edit.text()
        if self.int_validator.validate(input_text, 0)[0] == QIntValidator.Acceptable:
            self.result_label.setText("Valid integer!")
        else:
            self.result_label.setText("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
