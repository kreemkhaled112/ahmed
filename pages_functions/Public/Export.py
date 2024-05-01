from pages_functions.__init__ import *

from ui.Public.Export_ui import Ui_Form

class Export(QDialog):
    def __init__(self, parent=None, tableWidget=None):
        super(Export, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tableWidget = tableWidget
        self.ui.Export.clicked.connect(self.Export)
        self.ui.Cancel.clicked.connect(self.accept)
        self.ui.pushButton.clicked.connect(self.select_file)
        
    def Export(self):
        if self.ui.lineEdit.text()  == '' : QMessageBox.warning(self, 'No File Name', 'Please Select File.') ; return ""
        with open(self.ui.lineEdit.text(), "w",encoding="UTF-8") as file:
            for row in range(self.tableWidget.rowCount()):
                row_data = []
                checkbox_item = self.tableWidget.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    data = [self.tableWidget.item(row, col).text() for col in range(1, self.tableWidget.columnCount())]
                    if self.ui.Group.isChecked() : row_data.append(data[0])
                    if self.ui.Cookie.isChecked() : row_data.append(data[5])
                    file.write(':'.join(row_data) + '\n')
   
        self.accept()
    def select_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '')
        if fname[0]:
            self.ui.lineEdit.setText(fname[0])
        