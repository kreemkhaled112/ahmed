from pages_functions.__init__ import *
from pages_functions.Facebook.Data.Edit import *
import time 
from urllib.parse import urlencode
from requests.exceptions import ReadTimeout, ConnectTimeout

class Login:
    def __init__(self,email,password):
        self.req = requests.Session()
        self.email = email
        self.password = password
        headers = {
            'Host': 'www.facebook.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Connection': 'close',
        }
        self.req.headers.update(headers)

    def Start(self):
        try:
            response = self.req.get('https://www.facebook.com/')
            sleep(5)
            fr=response.cookies['fr']
            sb=response.cookies['sb']
            _datr=response.text.split('"_js_datr","')[1].split('"')[0]
            _token=response.text.split('privacy_mutation_token=')[1].split('"')[0]
            _jago=response.text.split('"jazoest" value="')[1].split('"')[0]
            _lsd=response.text.split('name="lsd" value="')[1].split('"')[0]

            cookie = {'fr': fr,'sb': sb,'_js_datr': _datr,'wd': '717x730','dpr': '1.25'}
            self.req.cookies.update(cookie)

            data = urlencode({
                'jazoest': _jago,
                'lsd': _lsd,
                'email': self.email,
                'login_source': 'comet_headerless_login',
                'next': '',
                'encpass': f'#PWD_BROWSER:0:{round(time.time())}:{self.password}',
            })

            headers = {
                'Host': 'www.facebook.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'https://www.facebook.com/',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': str(len(data)),
                'Origin': 'https://www.facebook.com',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
            self.req.headers.update(headers)

            response = self.req.post(f'https://www.facebook.com/login/?privacy_mutation_token={_token}', data=data)
            cookie_string = (';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", "")
            if 'Chat' in response.text or "دردشة" in response.text :
                return 'success' , cookie_string , Get_Name(cookie_string).Get()
            elif  "We suspended your account" in response.text :
                return "checkpoint" , cookie_string
            elif "The email address you entered isn&#039;t connected to an account." in response.text:
                return "The email address you entered isn't connected to an account" , cookie_string
            elif 'Try another way' in response.text:
                return "The password that you entered is incorrect. " , cookie_string
            elif "You've entered an old password" in response.text :
                return "You've entered an old password" , cookie_string
            elif 'Enter the code from your email' in response.text:
                return 'Enter the code from your email' , cookie_string
            elif 'Choose a way to confirm that it&#039;s you' in response.text:
                return 'Two Factor Code Sended.....' , cookie_string
            else:
                return 'None' , cookie_string
                print(cookie_string)
                open("html.html" , "w" , encoding="utf-8").write(response.text)
                webbrowser.open('html.html')
            
        except (ReadTimeout, ConnectTimeout):
            return "failed"
        except Exception as e: return e
