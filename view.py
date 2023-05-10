# import sys

# from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox
# from PySide2 import QtWidgets, QtGui


# class RenamerView(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.setup_ui()

#     def setup_ui(self):
#         self.setWindowTitle("Renamer")
#         self.resize(600, 300)
#         self.center()

#         # create widgets
#         vb = QVBoxLayout()

#         hbtop = QHBoxLayout()
#         vb.addLayout(hbtop)
#         self.line_path = QtWidgets.QLineEdit()
#         self.btn_browse = QtWidgets.QPushButton("Browse")
#         hbtop.addWidget(self.line_path)
#         hbtop.addWidget(self.btn_browse)

#         hbmid = QHBoxLayout()
#         vb.addLayout(hbmid)
#         self.line_old_text = QtWidgets.QLineEdit()
#         self.line_new_text = QtWidgets.QLineEdit()
#         self.btn_add = QtWidgets.QPushButton("+")
#         self.btn_sub = QtWidgets.QPushButton("-")
#         self.label = QtWidgets.QLabel("→")
#         hbmid.addWidget(self.line_old_text)
#         hbmid.addWidget(self.label)
#         hbmid.addWidget(self.line_new_text)
#         hbmid.addWidget(self.btn_add)
#         hbmid.addWidget(self.btn_sub)

#         hbbot = QHBoxLayout()
#         vb.addLayout(hbbot)
#         self.btn_rename = QtWidgets.QPushButton("Rename")
#         hbbot.addWidget(self.btn_rename)

#         self.setLayout(vb)

#         # button clicked event example
#         self.btn_browse.clicked.connect(self.browse_test)
#         self.btn_add.clicked.connect(self.add_test)
#         self.btn_rename.clicked.connect(self.rename_test)

#         self.show()

#     def center(self):
#         fg = self.frameGeometry()
#         dw = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
#         fg.moveCenter(dw)
#         self.move(fg.topLeft())

#     def message_box(self):
#         msgbox = QMessageBox()
#         msgbox.about(self, "Alert", "Complete")

#     def browse_test(self):
#         print("Select a directory")

#     def add_test(self):
#         print("add text")

#     def rename_test(self):
#         self.message_box()
#         print("change name")


# if __name__ == '__main__':    
#     app = QApplication()
#     rv = RenamerView()
#     sys.exit(app.exec_())

from PySide2.QtWidgets import (QApplication, QPushButton, QWidget, QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
                                 QVBoxLayout, QGroupBox)

import sys


class Widget(QWidget):
    form_group_box = None
    layout = None
    row_counter = None

    def __init__(self):
        super().__init__()
        self.row_counter = 0
        self.create_form_groupbox()
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self._insert)
        button_box.rejected.connect(self._exit)
        button_box.button(QDialogButtonBox.Ok).setText("Insert")
        button_box.button(QDialogButtonBox.Cancel).setText("Cancel")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.form_group_box)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)
        self.setWindowTitle("form example")

    def _insert(self):
        self._insert_row_component()

    def _exit(self):
        pass

    def _insert_row_component(self):
        push_button = QPushButton("push button")
        push_button.clicked.connect(self._on_push_button_clicked)
        qline_edit1 = QLineEdit()
        qline_edit1.setPlaceholderText("enter text")
        qline_edit2 = QLineEdit()
        qline_edit2.setPlaceholderText("enter text")
        qlabel = QLabel("label")
        self.layout.addWidget(qline_edit1, self.row_counter, 0)
        self.layout.addWidget(qline_edit2, self.row_counter, 1)
        self.layout.addWidget(qlabel, self.row_counter, 2)
        self.layout.addWidget(push_button, self.row_counter, 3)
        self.row_counter = self.row_counter + 1

    def _on_push_button_clicked(self):
        # TODO implement
        print("button clicked")

    def create_form_groupbox(self):
        self.form_group_box = QGroupBox("Form layout")
        self.layout = QGridLayout()
        self._insert_row_component()
        self.form_group_box.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
