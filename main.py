import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QLineEdit, QVBoxLayout, QWidget, QFileSystemModel


class FileTreeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Tree")
        self.setGeometry(100, 100, 800, 600)

        self.model = QFileSystemModel()
        self.model.setRootPath(os.path.expanduser("~"))
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(os.path.expanduser("~")))

        self.filter_edit = QLineEdit()
        self.filter_edit.textChanged.connect(self.filter_tree)

        layout = QVBoxLayout()
        layout.addWidget(self.filter_edit)
        layout.addWidget(self.tree_view)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def filter_tree(self, text):
        root_index = self.tree_view.rootIndex()
        for row in range(self.model.rowCount(root_index)):
            index = self.model.index(row, 0, root_index)
            file_name = self.model.fileName(index)
            if text.lower() in file_name.lower():
                self.tree_view.setRowHidden(row, root_index, False)
            else:
                self.tree_view.setRowHidden(row, root_index, True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_tree_app = FileTreeApp()
    file_tree_app.show()
    sys.exit(app.exec_())