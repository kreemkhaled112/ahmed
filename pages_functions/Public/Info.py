from pages_functions.__init__ import *
from ui.Public.Info_ui import Ui_Form

class Info(QDialog):
    def __init__(self ):
        super(Info, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.table.hide()
        self.ui.table.verticalHeader().hide()
        self.ui.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.ui.table.setColumnWidth(0, 18)
        self.ui.table.setColumnWidth(1, 120)
        self.ui.table.setColumnWidth(2, 120)
    def Add(self,type,id,name,action,message):
        if     type == 0 :  type = "❌"
        elif   type == 1 :  type = "✅"
        else : type = "⚠️"

        self.ui.table.insertRow(0)  
        self.ui.table.setItem(0, 0,  QTableWidgetItem(type))
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.table.setItem(0, 1 , QTableWidgetItem(id)) 
        self.ui.table.setItem(0, 2,  QTableWidgetItem(data))
        self.ui.table.setItem(0, 3 , QTableWidgetItem(name)) 
        self.ui.table.setItem(0, 4 , QTableWidgetItem(action)) 
        self.ui.table.setItem(0, 5 , QTableWidgetItem(message))
        try: cursor.execute('INSERT INTO Reports (Type, Id , Data , Name, Acction ,Message) VALUES ( ?, ?, ?, ?, ?, ?)', ( type , id , data, name, action, message)) ;conn.commit()
        except: pass
    def Update(self,s=None,f=None,o=None):
        self.ui.successful.setText(str(s))
        self.ui.faild.setText(str(f))
        self.ui.total.setText(str(s+f))
        self.ui.order.setText(str(o))
