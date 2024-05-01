from pages_functions.__init__ import *
from ui.Facebook.Follow_ui import Ui_Form

class Report(QWidget):
    def __init__(self ):
        super(Report, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    