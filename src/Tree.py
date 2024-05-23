import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 App with QTreeView")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QTreeView
        self.tree_view = QTreeView()
        layout.addWidget(self.tree_view)

        # Create a model
        self.model = QStandardItemModel()
        self.tree_view.setModel(self.model)

        # Populate the model
        root_item = self.model.invisibleRootItem()
        parent_item = QStandardItem("Parent Item")
        root_item.appendRow(parent_item)

        child1_item = QStandardItem("Child 1")
        child2_item = QStandardItem("Child 2")
        parent_item.appendRow(child1_item)
        parent_item.appendRow(child2_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
