import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PySide6.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 App with QPixmap")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Load an image using QPixmap
        pixmap = QPixmap(r"C:\Users\owner\Pictures\shelfTest.png") # do not use backslash only

        # Create a QLabel and set the pixmap as its content
        label = QLabel()
        label.setPixmap(pixmap)

        layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
