import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QColumnView
from PySide6.QtCore import QAbstractItemModel, QModelIndex

class MyModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column)

    def parent(self, index):
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        return 5

    def columnCount(self, parent=QModelIndex()):
        return 3

    def data(self, index, role=0):
        if role == 0:
            return f"Item {index.row()},{index.column()}"
        return None

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 App with QColumnView")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QColumnView
        self.column_view = QColumnView()
        layout.addWidget(self.column_view)

        # Set the model for QColumnView
        model = MyModel()
        self.column_view.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
