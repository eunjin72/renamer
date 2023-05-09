import sys

from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox
from PySide2 import QtWidgets, QtGui


class RenamerView(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Renamer")
        self.resize(600, 300)
        self.center()

        # create widgets
        vb = QVBoxLayout()

        hbtop = QHBoxLayout()
        vb.addLayout(hbtop)
        self.line_path = QtWidgets.QLineEdit()
        self.btn_browse = QtWidgets.QPushButton("Browse")
        hbtop.addWidget(self.line_path)
        hbtop.addWidget(self.btn_browse)

        hbmid = QHBoxLayout()
        vb.addLayout(hbmid)
        self.label_file = QtWidgets.QLabel("file lists")
        hbmid.addWidget(self.label_file)

        hbmid_2 = QHBoxLayout()
        vb.addLayout(hbmid_2)
        self.line_old_text = QtWidgets.QLineEdit()
        self.line_new_text = QtWidgets.QLineEdit()
        self.btn_add = QtWidgets.QPushButton("+")
        self.label = QtWidgets.QLabel("→")
        hbmid_2.addWidget(self.line_old_text)
        hbmid_2.addWidget(self.label)
        hbmid_2.addWidget(self.line_new_text)
        hbmid_2.addWidget(self.btn_add)

        hbbot = QHBoxLayout()
        vb.addLayout(hbbot)
        self.btn_rename = QtWidgets.QPushButton("Rename")
        hbbot.addWidget(self.btn_rename)

        self.setLayout(vb)

        # button clicked event example
        self.btn_browse.clicked.connect(self.browse_test)
        self.btn_add.clicked.connect(self.add_test)
        self.btn_rename.clicked.connect(self.rename_test)

        self.show()

    def center(self):
        fg = self.frameGeometry()
        dw = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        fg.moveCenter(dw)
        self.move(fg.topLeft())

    def message_box(self):
        msgbox = QMessageBox()
        msgbox.about(self, "Alert", "Complete")

    def browse_test(self):
        print("Select a directory")

    def add_test(self):
        print("add text")

    def rename_test(self):
        self.message_box()
        print("change name")


if __name__ == '__main__':    
    app = QApplication()
    rv = RenamerView()
    sys.exit(app.exec_())
