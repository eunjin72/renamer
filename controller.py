import sys
from PySide2.QtWidgets import *

from view import Widget
from model import RenameModel


class RenameController(Widget):
    def __init__(self):
        super().__init__()
        self.model = RenameModel()

        # button clicked event
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        # self.btn_rename.clicked.connect(self.btn_rename_clicked)

    def btn_browse_clicked(self):
        dialog = QFileDialog()
        dialog.setDirectory('/TD/show')
        dir_path = dialog.getExistingDirectory()
        self.line_path.setText(dir_path)

    # def btn_rename_clicked(self):
    #     self.model.change_name(path=None, old_name=None, new_name=None)


if __name__ == "__main__":
    app = QApplication()
    rc = RenameController()
    sys.exit(app.exec_())
