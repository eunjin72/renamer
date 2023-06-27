# import sys
#
# from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox
# from PySide2 import QtWidgets, QtGui
#
#
# class RenamerView(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.setWindowTitle("Renamer")
#         self.resize(600, 300)
#         self.center()
#
#         # create widgets
#         vb = QVBoxLayout()
#
#         hbtop = QHBoxLayout()
#         vb.addLayout(hbtop)
#         self.line_path = QtWidgets.QLineEdit()
#         self.btn_browse = QtWidgets.QPushButton("Browse")
#         hbtop.addWidget(self.line_path)
#         hbtop.addWidget(self.btn_browse)
#
#         hbmid = QHBoxLayout()
#         vb.addLayout(hbmid)
#         self.label_file = QtWidgets.QLabel("file lists")
#         hbmid.addWidget(self.label_file)
#
#         hbmid_2 = QHBoxLayout()
#         vb.addLayout(hbmid_2)
#         self.line_old_text = QtWidgets.QLineEdit()
#         self.line_new_text = QtWidgets.QLineEdit()
#         self.btn_add = QtWidgets.QPushButton("+")
#         self.label = QtWidgets.QLabel("→")
#         hbmid_2.addWidget(self.line_old_text)
#         hbmid_2.addWidget(self.label)
#         hbmid_2.addWidget(self.line_new_text)
#         hbmid_2.addWidget(self.btn_add)
#
#         hbbot = QHBoxLayout()
#         vb.addLayout(hbbot)
#         self.btn_rename = QtWidgets.QPushButton("Rename")
#         hbbot.addWidget(self.btn_rename)
#
#         self.setLayout(vb)
#
#         # button clicked event example
#         self.btn_browse.clicked.connect(self.browse_test)
#         self.btn_add.clicked.connect(self.add_test)
#         self.btn_rename.clicked.connect(self.rename_test)
#
#         self.show()
#
#     def center(self):
#         fg = self.frameGeometry()
#         dw = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
#         fg.moveCenter(dw)
#         self.move(fg.topLeft())
#
#     def message_box(self):
#         msgbox = QMessageBox()
#         msgbox.about(self, "Alert", "Complete")
#
#     def browse_test(self):
#         print("Select a directory")
#
#     def add_test(self):
#         print("add text")
#
#     def rename_test(self):
#         self.message_box()
#         print("change name")
#
#
# if __name__ == '__main__':
#     app = QApplication()
#     rv = RenamerView()
#     sys.exit(app.exec_())

import sys

from PySide2.QtWidgets import *
from model import RenameModel


class Widget(QWidget):
    form_group_box = None
    layout = None
    row_counter = None

    def __init__(self):
        super().__init__()
        self.model = RenameModel()
        self.row_counter = 0
        self.old_list = []
        self.new_list = []
        self.create_form_groupbox()

        a = QHBoxLayout()
        self.line_path = QLineEdit()
        self.btn_browse = QPushButton("Browse")
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        a.addWidget(self.line_path)
        a.addWidget(self.btn_browse)

        self.setLayout(a)

        self.btn_add = QPushButton("+")
        self.btn_add.clicked.connect(self._insert_row_component)

        self.btn_rename = QPushButton("Rename")
        self.btn_rename.clicked.connect(self.btn_rename_clicked)

        main_layout = QVBoxLayout()

        a.addLayout(main_layout)

        main_layout.addWidget(self.form_group_box)
        main_layout.addWidget(self.btn_add)
        main_layout.addWidget(self.btn_rename)
        self.setLayout(main_layout)

        self.setWindowTitle("Renamer")

    def btn_browse_clicked(self):
        dialog = QFileDialog()
        dialog.setDirectory('/TD/show/goguma/sequences/S010/S010_0010/cmp/dev/v001/nuke')
        self.dir_path = dialog.getExistingDirectory()
        self.line_path.setText(self.dir_path)

    def btn_rename_clicked(self):
        # self.old_list.append(self.qline_edit1)
        # self.new_list.append(self.qline_edit2)
        # self.qline_edit1.setObjectName('text' + str(self.row_counter))
        # self.qline_edit2.setObjectName('text' + str(self.row_counter))

        for i in range(self.row_counter):
            first = self.old_list[i].text()
            print(first)
        # old_name = self.qline_edit1.text()
        # new_name = self.qline_edit2.text()
        # # print(old_name)
        # # for o, n in old_name, new_name:
        # self.model.change_name(self.dir_path, old_name, new_name)

    def _insert_row_component(self):
        self.qline_edit1 = QLineEdit()
        self.qline_edit1.setPlaceholderText("1")
        self.qlabel = QLabel(" -> ")
        self.qline_edit2 = QLineEdit()
        self.qline_edit2.setPlaceholderText("2")
        self.layout.addWidget(self.qline_edit1, self.row_counter, 0)
        self.layout.addWidget(self.qline_edit2, self.row_counter, 2)
        self.layout.addWidget(self.qlabel, self.row_counter, 1)

        self.old_list.append(self.qline_edit1)
        self.new_list.append(self.qline_edit2)

        self.row_counter = self.row_counter + 1

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

