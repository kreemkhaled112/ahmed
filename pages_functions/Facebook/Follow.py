from pages_functions.__init__ import *

from ui.Facebook.Follow_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Facebook.Data.get_count import *
from pages_functions.Facebook.Data.Follow import Follow as follow
from pages_functions.Public.Select import Select

class Follow(QWidget):
    def __init__(self):
        super(Follow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.URL = "https://dlorx.com/adminapi/v1"
        self.API_KEY  = "gco5ezt5cr26seqzmzmx4fa311fya3gobajfojykuaypuwt2wzcjf1x3joomh7cm"
        self.TIMEOUT = 10
        self.time = 1
        self.succes = 0
        self.failed = 0
        self.order = 0
        self.is_running = False

        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.ui.Start.clicked.connect(lambda : Thread(target=self.Start).start())
        self.ui.Select_Account.clicked.connect(self.Select)
        self.ui.pushButton.clicked.connect(lambda: self.ui.label.setText(self.ui.lineEdit.text()))
        
    def Select(self):
        table_dialog = Select(self)
        table_dialog.exec()
    def Update_info(self,info):
        self.ui.Number_Account.setText(str(len(info)))
        self.info = info
        self.queue = queue.Queue()
        for i in self.info:
            self.queue.put(i)

    def get_pending_order(self,SERVICEs_ID):
        params = {
            "key": self.API_KEY,
            "type": SERVICEs_ID,
            "action": "getOrder",
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT).text)
    def get_remains(self,id):
        params = {
            "key": self.API_KEY,
            "action": 'status',
            "order": id,
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT).text)
    def set_start_count(self,order_id, start_count):
        params = {
            "key": self.API_KEY,
            "action": "setStartcount",
            "id": order_id,
            "start_count": start_count
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    
    def set_remains(self,order_id, remains):
        params = {
            "key": self.API_KEY,
            "action": "setRemains",
            "id": order_id,
            "remains": remains
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    def set_completed(self,order_id):
        params = {
            "key": self.API_KEY,
            "action": "setCompleted",
            "id": order_id
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    def set_Fail(self,order_id):
        params = {
            "key": self.API_KEY,
            "action": "setFail",
            "id": order_id
        }
        return json.loads(requests.get(self.URL, params=params, timeout=self.TIMEOUT, verify=False).text)
    
    def Start(self):
        if self.ui.Number_Account.text() == '0': QMessage(text = 'No Account Selected').mainloop() ; self.ui.Start.setChecked(False)
        else:
            if self.is_running == False : self.ui.Start.setText("Stop") ; self.is_running = True ; self.Info.Update(0,0,0,0)
            elif self.is_running : self.ui.Start.setText("Start") ; self.ui.Start.setChecked(False) ; self.is_running = False
            while  self.is_running :
                    pending = self.get_pending_order(int(self.ui.label.text()))
                    if pending["status"] == "fail": sleep(10) ; continue
                    if pending["status"] == "success":
                        self.succes = 0 ; self.failed = 0 ; self.Info.Update(s=0,f=0,o=self.order)
                        id = pending['id']
                        link = pending['link']
                        quantity = int(pending['quantity'])
                        result = get_follower(link).Start()
                        listt = []
                        if result[0] == 'No match found' :
                            self.Info.Add(0,id,'None',"Follow",f'Error {result[1]}')
                            # QMessage(text = 'Check cookie').mainloop() ; self.ui.Start.setChecked(False) ; self.ui.Start.setText("Start") 
                        else :
                            try:
                                self.set_start_count(int(id),int(result[1]))
                                def perfom():
                                    while not self.queue.empty() :
                                        if self.succes >= quantity : break
                                        else:
                                            try:
                                                cookie = self.queue.get()
                                                listt.append(cookie)
                                                result = follow(link,cookie[5]).Start()
                                                self.Info.Add(result[1],id,cookie[1],"Follow",f'{result[0]}')
                                                if result[1] == 1: self.succes += 1
                                                else: self.failed += 1
                                                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ;  sleep(self.time)
                                            except Exception as e:
                                                try: self.Info.Add(0,id,cookie[1],"Follow",e)
                                                except : self.Info.Add(0,id,'None',"Follow","No Account") 
                                                self.failed += 1
                                                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ;  sleep(self.time)
                                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                                    futures = [executor.submit(perfom) for _ in range(5)]
                                    concurrent.futures.wait(futures)
                            except Exception as e : input(e)
                        self.order += 1
                        self.Info.Add(1,id,'Compelet',"Follow",f'Succes : {self.succes} Failed : {self.failed}') ; self.Info.Update(s=self.succes,f=self.failed,o=self.order) 
                        if self.succes >= quantity  : self.set_completed(id)
                        else : self.set_remains(id,quantity-self.succes)
                        for i in listt:
                            self.queue.put(i)
    