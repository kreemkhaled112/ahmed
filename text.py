import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

class MyTable(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.init_ui()

    def init_ui(self):
        self.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])
        self.setVerticalHeaderLabels(['Row {}'.format(i) for i in range(self.rowCount())])
        # Set the selection behavior to select whole rows
        self.setSelectionBehavior(QAbstractItemView.SelectItems)
        # Connect the cell clicked signal to the edit slot
        self.itemClicked.connect(self.edit_item)

    def edit_item(self, item):
        self.editItem(item)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editable Table Example")
        self.setGeometry(100, 100, 600, 400)

        self.table = MyTable(5, 3)  # 5 rows, 3 columns
        self.setCentralWidget(self.table)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
