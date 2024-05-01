from PyQt5.QtWidgets import *
from ui.main_ui import Ui_MainWindow

from pages_functions.Facebook.Manger_Face import Manager_Face
from pages_functions.Facebook.Follow import Follow
from pages_functions.Facebook.Like import Like
from pages_functions.Facebook.Share import Share
from pages_functions.Facebook.Report import Report

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Account_Manger_face = self.ui.Account_Manger_face 
        self.Follow_face = self.ui.Follow_face
        self.Like_face = self.ui.Like_face
        self.Share_face = self.ui.Share_face

        self.menu_btns_list = {
            self.Account_Manger_face: Manager_Face(),
            self.Follow_face: Follow(),
            self.Like_face: Like(),
            self.Share_face: Share(),
        }

        self.show_home_window()
        self.ui.icon_only_widget.hide()
        
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.Account_Manger_face.clicked.connect(self.show_selected_window)
        self.Follow_face.clicked.connect(self.show_selected_window)
        self.Like_face.clicked.connect(self.show_selected_window)
        self.Share_face.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        result = self.open_tab_flag(self.Account_Manger_face.objectName())
        self.set_btn_checked(self.Account_Manger_face)

        if result[0]: self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.Account_Manger_face.text()
            curIndex = self.ui.tabWidget.addTab(Manager_Face(), title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def show_selected_window(self):
        button = self.sender()

        result = self.open_tab_flag(button.objectName())
        self.set_btn_checked(button)

        if result[0]: self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self, index):
        self.ui.tabWidget.removeTab(index)
        if self.ui.tabWidget.count() == 0:
            self.show_home_window()

    def open_tab_flag(self, tab):
        open_tab_count = self.ui.tabWidget.count()
        for i in range(open_tab_count):
            tab_name = self.ui.tabWidget.tabText(i)
            if tab_name == tab:
                return True, i
            else: continue
        return False,

    def set_btn_checked(self, btn):
        for button in self.menu_btns_list.keys():
            if button != btn: button.setChecked(False)
            else: button.setChecked(True)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec())
