import sys
from PySide2.QtWidgets import *


class RenameView(QWidget):
    def __init__(self):
        super().__init__()
        
        self.row_counter = 0
        self.dir_path = None
        self.old_list = []
        self.new_list = []
        self.create_groupbox()
        self.setupUI()

    def setupUI(self):
        layout_left_in = QHBoxLayout()
        layout_left = QVBoxLayout()
        layout_right_in = QHBoxLayout()
        layout_right = QVBoxLayout()
        layout_main = QHBoxLayout()

        self.line_path = QLineEdit("Path")
        self.text_name = QTextEdit("Current File Name")
        self.btn_browse = QPushButton("Browse")

        self.btn_add = QPushButton("+")
        self.btn_add.clicked.connect(self._insert_row_lineedit)
        self.btn_sub.clicked.connect(self.btn_sub_event)
        self.btn_rename = QPushButton("Rename")

        layout_left_in.addWidget(self.line_path)
        layout_left_in.addWidget(self.btn_browse)
        layout_left.addLayout(layout_left_in)
        layout_left.addWidget(self.text_name)

        layout_right.addWidget(self.form_group_box)
        layout_right_in.addWidget(self.btn_add)
        layout_right.addLayout(layout_right_in)
        layout_right.addWidget(self.btn_rename)

        layout_main.addLayout(layout_left)
        layout_main.addLayout(layout_right)

        self.setLayout(layout_main)
        self.setWindowTitle("Renamer")

        self.show()

    def _insert_row_lineedit(self):
        line_old = QLineEdit()
        line_old.setPlaceholderText("old name")
        label = QLabel(" -> ")
        line_new = QLineEdit()
        line_new.setPlaceholderText("new name")
        self.btn_sub = QPushButton("-")
        self.layout.addWidget(line_old, self.row_counter, 0)
        self.layout.addWidget(label, self.row_counter, 1)
        self.layout.addWidget(line_new, self.row_counter, 2)
        self.layout.addWidget(self.btn_sub, self.row_counter, 3)

        self.old_list.append(line_old)
        self.new_list.append(line_new)

        self.row_counter = self.row_counter + 1

    def create_groupbox(self):
        self.form_group_box = QGroupBox("Enter Name")
        self.layout = QGridLayout()
        self._insert_row_lineedit()
        self.form_group_box.setLayout(self.layout)

    def btn_sub_event(self):
        "remove QLineEdit"
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rv = RenameView()
    app.exec_()