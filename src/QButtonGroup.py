import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QRadioButton, QPushButton, QWidget, QButtonGroup

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 App with QButtonGroup")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.radio_button_group = QButtonGroup()

        radio_button1 = QRadioButton("Option 1")
        radio_button2 = QRadioButton("Option 2")
        radio_button3 = QRadioButton("Option 3")

        layout.addWidget(radio_button1)
        layout.addWidget(radio_button2)
        layout.addWidget(radio_button3)

        self.radio_button_group.addButton(radio_button1)
        self.radio_button_group.addButton(radio_button2)
        self.radio_button_group.addButton(radio_button3)

        button = QPushButton("Print Selected")
        button.clicked.connect(self.print_selected)
        layout.addWidget(button)

    def print_selected(self):
        checked_button = self.radio_button_group.checkedButton()
        if checked_button:
            print("Selected Option:", checked_button.text())
        else:
            print("No option selected.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
