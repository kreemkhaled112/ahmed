from pages_functions.__init__ import *

class Follow:
    def __init__(self, url ,cookie):
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        
        self.id = (re.search(r'/([^/]+)$', url) or re.search(r'facebook.com/([^/]+)', url) or re.search(r'id=(\d+)', url) or "").group(1)

        try:self.url = url.replace("www", "mbasic")
        except:pass

    def Start(self):
        response = self.req.get(self.url)
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                try: 
                    self.href = soup.select_one('a[href^="/a/subscribe.php?"]').get('href')
                    sleep(1)
                    return self.Follow_Profile()
                except : 
                    self.href = soup.select_one('a[href^="/a/subscriptions/remove?"]').get('href')
                    return "Already followed" , 2
            else:
                return "Faild Follow" , 0
        except: 
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            return "Faild Follow" , 0

    def Follow_Profile(self):
        self.headers['referer'] = self.url
        self.req.headers.update(self.headers)

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        if response.status_code == 200 :
            return (f'Done Follow : {self.id}') , 1

class Like_Page:
    def __init__(self, url ,cookie):
        self.req = requests.Session()
        self.id = re.search(r'c_user=(\d+)', cookie).group(1)
        self.cookie = {'cookie':cookie}
        self.req.cookies.update(self.cookie)
        self.url = url

    def Start(self):
        response = self.req.get(self.url ,allow_redirects=True)
        open("html.html" , "w" , encoding="utf-8").write(response.text)
        input(".....")
        req = BeautifulSoup(response.content, 'html.parser')
        haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
        rev = re.search('{"rev":(.*?)}',str(req)).group(1)
        hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
        # dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
        jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
        lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
        spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
        spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
        var = {"input":{"is_tracking_encrypted":'false',"page_id":"103424319386989","source":0,"tracking":0,"actor_id":self.id,"client_mutation_id":"5"},"scale":1}
        data = {'av':self.id,'__user':self.id,'__a':'1','__hs':haste,'dpr':'1.5','__ccg':'EXCELLENT','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': 'NAcNdzbZgm9trLGDL9EMUavCDR3PFSpnqgxMRG3s1bCwpg7bIS-60Sg:36:1705079016','jazoest': jazoest,'lsd': lsd,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometProfilePlusLikeMutation','variables':json.dumps(var),'server_timestamps':'true','doc_id':'6716077648448761'}
        header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,image/jpeg,image/jpg,image/png,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':self.url,'Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'CometProfilePlusLikeMutation','X-Fb-Lsd':lsd}
        pos = self.req.post('https://www.facebook.com/api/graphql/',data=data,headers=header,allow_redirects=True)
        open("html.html" , "w" , encoding="utf-8").write(pos.text)
        print(pos.json())
        
    def Follow_Profile(self):
        self.headers['referer'] = self.url
        self.req.headers.update(self.headers)

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        if response.status_code == 200 :
            return (f'Done Follow ') , 1

