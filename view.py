import sys

from PySide2.QtWidgets import *


class RenameView(QWidget):
    form_group_box = None
    layout = None
    row_counter = None

    def __init__(self):
        super().__init__()
        # self.model = RenameModel()

        self.row_counter = 0
        self.dir_path = None
        self.old_list = []
        self.new_list = []
        self.create_groupbox()

        layout_side = QHBoxLayout()
        self.line_path = QLineEdit()
        self.btn_browse = QPushButton("Browse")
        self.btn_browse.clicked.connect(self.btn_browse_event)
        layout_side.addWidget(self.line_path)
        layout_side.addWidget(self.btn_browse)

        self.btn_add = QPushButton("+")
        self.btn_add.clicked.connect(self._insert_row_lineedit)

        self.btn_rename = QPushButton("Rename")
        self.btn_rename.clicked.connect(self.btn_rename_event)

        layout_main = QVBoxLayout()
        layout_side.addLayout(layout_main)

        layout_main.addWidget(self.form_group_box)
        layout_main.addWidget(self.btn_add)
        layout_main.addWidget(self.btn_rename)

        self.setLayout(layout_side)
        self.setLayout(layout_main)
        self.setWindowTitle("Renamer")

        self.show()

    def btn_browse_event(self):
        print("Select Directory")

    def btn_rename_event(self):
        print('Change name')

    def _insert_row_lineedit(self):
        line_old = QLineEdit()
        line_old.setPlaceholderText("old name")
        label = QLabel(" -> ")
        line_new = QLineEdit()
        line_new.setPlaceholderText("new name")
        self.layout.addWidget(line_old, self.row_counter, 0)
        self.layout.addWidget(label, self.row_counter, 1)
        self.layout.addWidget(line_new, self.row_counter, 2)

        self.old_list.append(line_old)
        self.new_list.append(line_new)

        self.row_counter = self.row_counter + 1

    def create_groupbox(self):
        self.form_group_box = QGroupBox("Enter Name")
        self.layout = QGridLayout()
        self._insert_row_lineedit()
        self.form_group_box.setLayout(self.layout)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     rv = RenameView()
#     sys.exit(app.exec_())

