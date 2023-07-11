import sys
import os
from PySide2.QtWidgets import *

from view import RenameView
from model import RenameModel


class RenameController(RenameView):
    def __init__(self):
        super().__init__()
        self.model = RenameModel()

        # button clicked event
        self.btn_browse.clicked.connect(self.btn_browse_clicked)
        self.btn_rename.clicked.connect(self.btn_rename_clicked)

    def btn_browse_clicked(self):
        dialog = QFileDialog()
        dialog.setDirectory('<path>')
        self.dir_path = dialog.getExistingDirectory()
        self.line_path.setText(self.dir_path)
        self.show_file_name()
        
    def show_file_name(self):
        files = os.listdir(self.dir_path)
        self.text_name.clear()
        for file in files:
            self.text_name.append(file)

    def btn_rename_clicked(self):
        for i in range(self.row_counter):
            old_name = self.old_list[i].text()
            new_name = self.new_list[i].text()
            self.model.change_name(path=self.dir_path, old_name=old_name, new_name=new_name)
        self.show_file_name()


if __name__ == "__main__":
    app = QApplication()
    rc = RenameController()
    sys.exit(app.exec_())
