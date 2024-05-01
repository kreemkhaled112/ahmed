from pages_functions.__init__ import *

class get_follower:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.url = url.strip()
        with open('pages_functions\cookie.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            random_line = random.choice(lines)  
        self.cookie = random_line.strip()
        cookie = {'cookie': self.cookie  }
        self.req.cookies.update(cookie)

    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:
            match = re.search(r'"text":"([\d.,]+)\s+Follower"', response.text)
            if not match:
                match = re.search(r'"text":"([\d.,]+)\s+Personen\s+sind\s+Follower"', response.text)
            if match:
                number_of_followers = int(match.group(1).replace(",", "").replace(".", ""))
                return "" , number_of_followers
            else:
                print("No match found")
                return 'No match found' , self.cookie
    
class get_likes:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        with open('pages_functions\cookie.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            random_line = random.choice(lines)  
        self.cookie = random_line.strip()
        cookie = {'cookie': self.cookie  }
        self.req.cookies.update(cookie)
        self.url = url.strip()
    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:
            match = re.search(r'"if_viewer_cannot_see_seen_by_member_list":{[^}]*"reaction_count":{"count":(\d+)}', response.text)
            if match: return '' , int(match.group(1).replace(",", "").replace(".", ""))
            else:
                return 'No match found' , ''

class get_share:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.url = url
    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:
            match = re.search(r'"i18n_share_count":"(\d+)"', response.text)
            if match: return '' , int(match.group(1).replace(",", "").replace(".", ""))
            else:
                return 'No match found', ''
class get_comment:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.url = url
    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:
            match = re.search(r'"comment_rendering_instance":{[^}]*"total_count":(\d+)[^}]*}', response.text)
            if match: return int(match.group(1).replace(",", "").replace(".", ""))
            else:
                return 'No match found'

