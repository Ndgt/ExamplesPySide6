import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 App with QMenu")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        button = QPushButton("Show Menu")
        button.clicked.connect(self.show_menu)
        layout.addWidget(button)

        # Create a menu
        self.menu = self.menuBar().addMenu("Options")

        # Add actions to the menu
        action1 = QAction("Action 1", self)
        action1.triggered.connect(lambda: self.action_triggered("Action 1"))

        action2 = QAction("Action 2", self)
        action2.triggered.connect(lambda: self.action_triggered("Action 2"))

        self.menu.addAction(action1)
        self.menu.addAction(action2)

    def show_menu(self):
        # Show the menu at the current cursor position
        self.menu.popup(self.cursor().pos())

    def action_triggered(self, action_name):
        print(f"{action_name} triggered.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
