from pages_functions.__init__ import *

class Like:
    def __init__(self, url ,type ,cookie) -> None:
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.url = url.replace('reel/', '')
        self.type = type
        try:self.url = self.url.replace("www", "mbasic")
        except:pass
        self.Type_reaction()
    def Type_reaction (self):
        if self.type == "Like" :
            self.reaction_id = '1635855486666999'
            self.reaction_type = "1"
        if self.type == "Love" :
            self.reaction_id = '1678524932434102'
            self.reaction_type = "2"
        if self.type == "Care" :
            self.reaction_id = '613557422527858'
            self.reaction_type = "16"
        if self.type == "Haha" :
            self.reaction_id = '115940658764963'
            self.reaction_type = "4"
        if self.type == "Wow" :
            self.reaction_id = '478547315650144'
            self.reaction_type = '3'
        if self.type == "Sad" :
            self.reaction_id = '908563459236466'
            self.reaction_type = "7"

    def Start(self):
        response = self.req.get(self.url)
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.href = soup.select_one('a[href^="/reactions/picker/?"]').get('href')
                sleep(1)
                return self.Get_reactions()
            else:
                return "Faild Get_reactions" , 0
        except:
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            return "Faild Get_reactions" , 0

    def Get_reactions(self):
        self.headers['referer'] = self.url
        self.req.headers.update(self.headers)

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        self.referer = response.url
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for a in soup.find_all('a', href=True):
                parsed_url = urlparse(a['href'])
                query_params = parse_qs(parsed_url.query)

                if 'reaction_type' in query_params and query_params['reaction_type'][0] == "0":
                    return (f"Already {self.type} befor :") , 2
                elif 'reaction_id' in query_params and query_params['reaction_id'][0] == self.reaction_id:
                    href = a['href']
                    sleep(1)
                    return self.Like_post(href)
        else:
            return "Faild Get_reactions" , 0

    def Like_post(self,href):
        self.headers['referer'] = self.referer
        self.req.headers.update(self.headers)

        response = self.req.get( f'https://mbasic.facebook.com/{href}' )
        if response.status_code == 200 :
            return f"Done {self.type} :" , 1
