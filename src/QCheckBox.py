import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCheckBox, QWidget, QLabel
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 App with QCheckBox")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QLabel to display checkbox state
        self.label = QLabel("Checkbox is unchecked")
        layout.addWidget(self.label)

        # Create QCheckBox
        self.checkbox = QCheckBox("Check me")
        self.state = self.checkbox.isChecked
        self.checkbox.stateChanged.connect(self.checkbox_state_changed) #stateChanged releases bool value
        layout.addWidget(self.checkbox)

    def checkbox_state_changed(self, state):
        if state:
            self.label.setText("Checkbox is checked")
        else:
            self.label.setText("Checkbox is unchecked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
