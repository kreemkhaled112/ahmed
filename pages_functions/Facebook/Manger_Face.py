from pages_functions.__init__ import *

from ui.Facebook.Manger_face_ui import Ui_Form

from pages_functions.Public.Info import Info
from pages_functions.Public.Export import Export
from pages_functions.Facebook.Data.Chrome import *

class Manager_Face(QWidget):
    def __init__(self):
        super(Manager_Face, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.succes = 0
        self.failed = 0
        self.order = 0
        self.checkpoint = 0 
        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.ui.Save.hide()
        self.Info.ui.order.hide()
        self.Info.ui.label_34.hide()
        
        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.lineEdit.textChanged.connect(self.filter_table)
        self.ui.Select.clicked.connect(self.select_all_rows)
        self.ui.AddMultiAccount.clicked.connect(self.Add_Multi_Account)
        self.ui.Export.clicked.connect(self.Export)
        self.ui.Update_all.clicked.connect(lambda : Thread(target=self.Update).start())
        self.ui.Refresh.clicked.connect(self.Refresh)
        self.ui.Delete_all.clicked.connect(lambda : Thread(target=self.Delete).start())
        self.ui.Write_Change.clicked.connect(self.handle_item_change)
        self.ui.Checker.clicked.connect(lambda : Thread(target=self.Checker).start())


        
        self.ui.table.verticalHeader().hide()
        self.Refresh()
        self.ui.table.itemChanged.connect(lambda item: {self.changed_items.append(item) , self.ui.Write_Change.setEnabled(True)})

        self.changed_items = []
        self.update_run = False
    def loadTableData(self,data):
        try:
            self.ui.table.setRowCount(len(data))
            for row, row_data in enumerate(data):
                select_checkbox_item = QTableWidgetItem()
                select_checkbox_item.setFlags(select_checkbox_item.flags() | Qt.ItemIsUserCheckable)
                select_checkbox_item.setCheckState(Qt.CheckState.Unchecked)
                select_checkbox_item.setText(str(row + 1))
                self.ui.table.setItem(row, 0, select_checkbox_item)

                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.ui.table.setItem(row, col + 1, item)

            self.ui.table.setColumnWidth(0, 50)
            self.ui.table.setColumnWidth(1, 80)
            self.ui.table.setColumnWidth(1, 100)
            self.ui.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
            headers = ["#"] + [description[0] for description in cursor.description]
            self.ui.table.setHorizontalHeaderLabels(headers)
            self.ui.table.setContextMenuPolicy(Qt.CustomContextMenu)
            self.ui.table.customContextMenuRequested.connect(self.show_context_menu)
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        except:pass
    def Refresh(self):
        self.data = cursor.execute("SELECT * FROM Account").fetchall()
        self.loadTableData(self.data)
    def show_context_menu(self, position):
        context_menu = QMenu(self)
    
        Update = context_menu.addAction("Update" , lambda : Thread(target=self.Update).start())
        show = context_menu.addAction("Show in Browser", lambda : Thread(target=self.View).start())
        Delete = context_menu.addAction("Delete", lambda : Thread(target=self.Delete_row).start())

        show.setShortcut(Qt.CTRL + Qt.Key_S)
        Update.setShortcut(Qt.CTRL + Qt.Key_U)
        Delete.setShortcut(Qt.Key_Delete)
        context_menu.exec_(self.mapToGlobal(position))

    def select_all_rows(self): 
        all_selected = all(self.ui.table.item(row, 0).checkState() == Qt.Checked for row in range(self.ui.table.rowCount()))
        for row in range(self.ui.table.rowCount()):
            checkbox_item = self.ui.table.item(row, 0)
            if all_selected: checkbox_item.setCheckState(Qt.Unchecked)  
            else: checkbox_item.setCheckState(Qt.Checked)  
                
    def filter_table(self):
        search_text = self.ui.lineEdit.text().lower().strip()
        selected_column = self.ui.comboBox.currentIndex()

        if not search_text: self.loadTableData(self.data)
        else: 
            self.changed_items.clear()
            filtered_data = [item for item in self.data if item[selected_column] and str(search_text).lower() in str(item[selected_column]).lower()]
            self.loadTableData(filtered_data)
    def handle_item_change(self):
        try:
            for i in self.changed_items:
                item = [self.ui.table.item(i.row(), col).text() for col in range(1, self.ui.table.columnCount())]
                cursor.execute('UPDATE Account SET groupname = ? WHERE cookies = ?', (item[0], item[5]))
                cursor.execute('UPDATE Account SET name = ? WHERE cookies = ?', (item[1], item[5]))
                cursor.execute('UPDATE Account SET password = ? WHERE cookies = ?', (item[3], item[5]))
                cursor.execute('UPDATE Account SET username = ? WHERE cookies = ?', (item[4], item[5]))
                cursor.execute('UPDATE Account SET cookies = ? WHERE cookies = ?', (item[5], item[5]))
                conn.commit()
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        except Exception as e:
            print(e)
            pass
    def Add_Multi_Account(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '')
        def thread():
            self.Info.Update(0,0,0)
            with open(fname[0], 'r', encoding='utf-8') as file:
                line =  file.readlines()
                for index,i in enumerate(line):
                    group = "None"
                    name= "None"
                    email = "None"
                    password= "None"
                    username= "None"
                    cookies= "None"
                    try:
                        if i.strip():
                            elements = i.replace(" ", "").split(':')
                            self.Info.ui.label.setText(f"Try Add {index}")
                            if len(elements) == 2:
                                email , password = elements
                            elif len(elements) == 3:
                                email , password , cookies = elements
                            cookies = cookies.strip().replace(" ", "")
                            existing_id = cursor.execute(f"SELECT * FROM Account WHERE email = '{email}' ").fetchall()
                            if not existing_id:
                                cursor.execute('INSERT INTO Account (groupname ,name ,email, password, username ,cookies) VALUES (?, ?, ?, ?, ?, ?)', (group, name, email.strip(), password.strip(),username, cookies )); conn.commit() 
                                self.succes += 1
                            else : self.failed += 1
                    except Exception as e: print(f'Failed Format {e}')
                self.Info.Add(1,'Add Multi Account','Account Manager',"Add Account",f"Done Add {self.succes} Accounts")
                self.Refresh()
                self.Info.ui.label.setText(f"Finished")
        if fname[0]:
            Thread(target=thread).start()
    def Update(self):
        if self.update_run == False:
            self.ui.Update_all.setText("Stop")
            self.Info.Update(0,0,0)
            self.update_run = True
        elif self.update_run == True:
            self.ui.Update_all.setText("Update")
            self.ui.Update_all.setChecked(False)
            self.update_run = False
            self.Info.ui.label.setText(f"Finished Update ")
        for row in range(self.ui.table.rowCount()):
            if self.update_run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    item = self.ui.table.item(row, 6)
                    if item is None or item.text() == '' or item.text() == 'None':
                        i = [self.ui.table.item(row, col).text() for col in range(1,self.ui.table.columnCount())]
                        self.Info.ui.label.setText(f"Logging {i[2]}:{i[3]}")
                        result = Chrom().Login(i[2],i[3])
                        try:
                            if result[0]  == 'success':
                                try:
                                    cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (result[2], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(result[2])))
                                    cursor.execute('UPDATE Account SET cookies = ? WHERE email = ?', (result[1], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(result[1])))
                                    username = re.search(r'c_user=(\d+)', result[1]).group(1)
                                    cursor.execute('UPDATE Account SET username = ? WHERE email = ?', (username, i[2])); self.ui.table.setItem(row, 5, QTableWidgetItem(str(username)))
                                    conn.commit()
                                    self.Info.Add(1,result[2],'Account Manager',"Login",f"Done Login {i[2]}:{i[3]}")
                                    self.Info.Update(s=self.succes,f=self.failed,o=self.order)
                                except Exception as e:
                                    self.Info.ui.label.setText(f"Faield Login {i[2]}:{i[3]}")
                                    self.Info.Add(0,f"{i[2]}:{i[3]}",'Account Manager',"Login",f'{e}')
                                    self.Info.Update(f=1)
                            else :
                                self.Info.ui.label.setText(f"Faield Login {i[2]}:{i[3]}")
                                cursor.execute('UPDATE Account SET cookies = ? WHERE email = ?', (result[0], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(result[0])))
                                try:cursor.execute('UPDATE Account SET username = ? WHERE email = ?', (re.search(r'c_user=(\d+)', result[1]).group(1), i[2])); self.ui.table.setItem(row, 5, QTableWidgetItem(str(re.search(r'c_user=(\d+)', result[1]).group(1))))
                                except:pass
                                conn.commit()
                                self.Info.Add(0,f"{i[2]}:{i[3]}",'Account Manager',"Login",f'{result[0]}')
                                self.Info.Update(f=1)
                        except:pass
                    else:
                        item = self.ui.table.item(row, 2)
                        if item is None or item.text() == '' or item.text() == 'None':
                            i = [self.ui.table.item(row, col).text() for col in range(1,self.ui.table.columnCount())]
                            self.Info.ui.label.setText(f"Update {i[2]}:{i[3]}")
                            result = Get_Name(i[5]).Get()
                            cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (result, i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(result)))
                            try:
                                username = re.search(r'c_user=(\d+)', i[5]).group(1)
                                cursor.execute('UPDATE Account SET username = ? WHERE email = ?', (username, i[2])); self.ui.table.setItem(row, 5, QTableWidgetItem(str(username)))
                            except: pass
                            conn.commit()
                            self.Info.Add(1,result,'Account Manager',"Update",f"Done Update {i[2]}:{i[3]}")
                            self.Info.Update(s=self.succes,f=self.failed,o=self.order)
        self.ui.Update_all.setText("Update")
        self.ui.Update_all.setChecked(False)
        self.update_run = False
        self.Info.ui.label.setText(f"Finished Update")

    def Delete(self):
        if not self.update_run:
            self.ui.Delete_all.setText("Stop")
            self.update_run = True
        else:
            self.ui.Delete_all.setText("Delete")
            self.ui.Delete_all.setChecked(False)
            self.update_run = False
            self.Info.ui.label.setText("Finished")
            return  

        for row in reversed(range(self.ui.table.rowCount())):
            checkbox_item = self.ui.table.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                item = self.ui.table.item(row, 3)
                cursor.execute(f'DELETE FROM Account WHERE email = "{item.text()}" '); conn.commit()
                conn.commit()
                self.ui.table.removeRow(row)

        self.ui.Delete_all.setText("Delete")
        self.ui.Delete_all.setChecked(False)
        self.update_run = False
        self.Refresh()
        self.Info.ui.label.setText("Finished Delete")

    def View(self):
        selected_row = self.ui.table.currentRow()
        if selected_row >= 0:
            i = []
            for col in range(1,self.ui.table.columnCount()):
                item = self.ui.table.item(selected_row, col)
                i.append(item.text())
            value = Chrom().View(i[5])
            if value == "" : pass
            else : 
                if value[0] == 'checkpoint':
                    cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(selected_row, 2, QTableWidgetItem(str(value[0])))
                else:
                    cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(selected_row, 6, QTableWidgetItem(str(value[1])))

        else: print("لا يوجد صف محدد.")
    def Delete_row(self):
        selected_row = self.ui.table.currentRow()
        if selected_row >= 0:
            deleted_row_data = []
            for col in range(1,self.ui.table.columnCount()):
                item = self.ui.table.item(selected_row, col)
                deleted_row_data.append(item.text())
            self.ui.table.removeRow(selected_row)
            cursor.execute(f'DELETE FROM Account WHERE email = "{deleted_row_data[2]}" '); conn.commit()
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        else: print("لا يوجد صف محدد.")
    def Checker(self):
        if self.update_run == False:
            self.ui.Checker.setText("Stop")
            self.Info.Update(0,0,0)
            self.update_run = True
        elif self.update_run == True:
            self.ui.Checker.setText("Checker")
            self.ui.Checker.setChecked(False)
            self.update_run = False
            self.Info.ui.label.setText(f"Finished Checker ")
        for row in range(self.ui.table.rowCount()):
            if self.update_run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    i = [self.ui.table.item(row, col).text() for col in range(1, self.ui.table.columnCount())]
                    value = Chrom().View(i[5],"close")
                    if value == "" : pass
                    else :
                        try:
                            username = re.search(r'c_user=(\d+)', i[5]).group(1)
                            cursor.execute('UPDATE Account SET username = ? WHERE email = ?', (username, i[2])); self.ui.table.setItem(row, 5, QTableWidgetItem(str(username)))
                        except: pass
                        if value[0] == 'checkpoint':
                            cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(value[0])))
                        else:
                            result = Get_Name(value[1]).Get()
                            cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (result, i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(result)))
                            cursor.execute('UPDATE Account SET cookies = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(value[1])))

        self.ui.Checker.setText("Checker")
        self.ui.Checker.setChecked(False)
        self.update_run = False
        self.Info.ui.label.setText(f"Finished Checker ")
    def Export(self):
        table_dialog = Export(self,self.ui.table )
        table_dialog.exec()
