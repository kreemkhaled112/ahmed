from pages_functions.__init__ import *

from ui.Public.Select_ui import Ui_Form
from pages_functions.Facebook.Manger_Face import Manager_Face

class Select(QDialog):
    def __init__(self, parent=None):
        super(Select, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.manage = Manager_Face()
        layout = QVBoxLayout(self.ui.widget); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.manage)
        self.manage.ui.widget_4.hide()
        self.manage.ui.widget_Info.hide()
        self.manage.ui.Save.setVisible(True)
        self.manage.ui.Save.clicked.connect(self.save)
        

        
    def save(self):
        data_to_save = []
        for row in range(self.manage.ui.table.rowCount()):
            checkbox_item = self.manage.ui.table.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                data = [self.manage.ui.table.item(row, col).text() for col in range(1, self.manage.ui.table.columnCount())]
                data_to_save.append(data)

        # Emit the signal to update info in the main thread
        self.parent().Update_info(data_to_save)
        self.accept()