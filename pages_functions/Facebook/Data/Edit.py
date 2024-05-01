from pages_functions.__init__ import *
class Name:
    def __init__(self,url) :
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.url = url
    def Get(self):
        try:  
            response = self.req.get( self.url )
            name = re.search(r'<title>(.*?)</title>', response.text).group(1)
            return name
        except :
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            return ""
class Get_Name:
    def __init__(self, cookie) :
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
    def Get(self):
        try:  
            response = self.req.get( 'https://mbasic.facebook.com/profile.php?' )
            name = re.search(r'<title>(.*?)</title>', response.text).group(1)
            if name == "" :
                return "CheckPoint" 
            return name
        except :
            return ""
class Get_i_user:
    def __init__(self , cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
    def Get(self):
        try:
            response = self.req.get( 'https://www.facebook.com/profile.php?' )
            id_index_start = response.text.find('"id":"', response.text.find('{"profile":{"id":"')) + len('"id":"')
            id_index_end = response.text.find('"', id_index_start)
            profile_id = response.text[id_index_start:id_index_end]
            cookie = f"{self.cookie};i_user={profile_id};"
            return "success" , cookie , Get_Name(cookie).Get()
        except : return "" 
class Edit_Photo:
    def __init__(self, photo, cookie) :
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.photo = photo
        self.url = "https://mbasic.facebook.com/profile_picture/"
    def Start(self):
        try:           
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'  : 'Save'}
            fil = {'pic' : open(self.photo, 'rb')}
            sleep(1)
            pos = BeautifulSoup(self.req.post(raq['action'],data=dat,files=fil).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return "Failed Change Profile Photo" , 0
            else: 
                return "Successfully Change Profile Photo" , 1
        except Exception as e: return "Failed Change Profile Photo" , 0
class Edit_Cover:
    def __init__(self, photo, cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.photo = photo
        self.url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
    def Start(self,):
        try:
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                  : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                  : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri'               : re.search('name="return_uri" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri_error'         : re.search('name="return_uri_error" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ref'                      : re.search('name="ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'csid'                     : re.search('name="csid" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ctype'                    : re.search('name="ctype" type="hidden" value="(.*?)"',str(raq)).group(1),
                'profile_edit_logging_ref' : re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'                   : 'Upload'}
            fil = {'file1' : open(self.photo, 'rb')}
            sleep(1)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat,files=fil).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return "Failed Change Cover Photo" , 0
            else: 
                return "Successfully Change Cover Photo" , 1
        except Exception as e: return "Failed Change Cover Photo" , 0
class Edit_bio:
    def __init__(self, bio ,cookie) -> None:
        self.req = requests.Session()
        self.bio = bio
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.url = "https://mbasic.facebook.com/profile/basic/intro/bio/"
    def Start(self):
        try:
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'bio'             : self.bio,
                'publish_to_feed' : False,
                'submit'          : 'Save'}
            sleep(2)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return "Failed Change Bio" , 0
            else: 
                return "Successfully Change Bio" , 1
        except Exception as e: return "Failed Change Bio" , 0
class Edit_City:
    def __init__(self, city ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.city = city
        self.url = 'https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city'   
    def Start(self):
        try:
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : 'current_city',
                'type'       : 'basic',
                'current_city[]' : self.city,
                'save'       : 'submit'}
            sleep(2)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return 'Failed Change City' , 0
            else: 
                return f'Successfully Change City To {self.city}' , 1 
        except Exception as e: return 'Failed Change City' , 0
class Edit_Hometown:
    def __init__(self, hometown ,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.hometown = hometown
        self.url = 'https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown'        
    def Start(self):
        try:
            req = BeautifulSoup(self.req.get(self.url).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : "hometown",
                'type'       : 'basic',
                'hometown[]' : self.hometown,
                'save'       : 'submit'}
            sleep(2)
            pos = BeautifulSoup(self.req.post('https://mbasic.facebook.com'+raq['action'],data=dat).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Your account is restricted at this time' or cek == 'You are Temporarily Blocked' or cek == 'Error' : return 'Failed Change Hometown' , 0
            else: 
                return f'Successfully Change Hometown To {self.hometown}' , 1
        except Exception as e: return 'Failed Change Hometown' , 0
class lock_profile:
    def __init__(self,cookie) -> None:
        self.req = requests.Session()
        self.req.headers.update(Header())
        self.cookie = {'cookie':cookie}
        self.req.cookies.update(self.cookie)
        self.id = re.search('c_user=(.*?);',self.cookie['cookie']).group(1)
        # action = input('Enable/Disable [a/n] : ').lower()
        # if action in ['a','active','activate','1']:
        #     stat = True
        #     self.execute(stat)
        # elif action in ['n','disabled','disabled','2']:
        #     stat = False
        #     self.execute(stat)
        # else:
        #     print('Correct Contents!')
        stat = True
    def Start(self):
        try:
            stat = True
            req = BeautifulSoup(self.req.get(f'https://www.facebook.com/{self.id}',allow_redirects=True).content,'html.parser')
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            var = {"enable":stat}
            data = {'av':self.id,'__user':self.id,'__a':'1','__hs':haste,'dpr':'1.5','__ccg':'EXCELLENT','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'WemPrivateSharingMutation','variables':json.dumps(var),'server_timestamps':'true','doc_id':'5507005232662559'}
            headpos = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,image/jpeg,image/jpg,image/png,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'WemPrivateSharingMutation','X-Fb-Lsd':lsd}
            pos = self.req.post('https://www.facebook.com/api/graphql/',data=data,headers=headpos,cookies=self.cookie,allow_redirects=True).json()
            if str(pos['data']['toggle_wem_private_sharing_control_enabled']) == 'None': return 'Locked Profile Not Available!' , 0
            elif str(pos['data']['toggle_wem_private_sharing_control_enabled']['private_sharing_enabled']) == 'True': return 'Successfully Activating the Locked Profile' , 1
            elif str(pos['data']['toggle_wem_private_sharing_control_enabled']['private_sharing_enabled']) == 'False': return 'Successfully Deactivated the Locked Profile' , 1
            else: print(pos)
        except Exception as e:
            print(e)

class Change_Password:
    def __init__(self, password , new_password) -> None:
        pass
