import os
from git import Repo
import subprocess , sys
from pages_functions.Facebook.Data.Chrome import *

# استدعاء الدالة للتحقق من المكتبة وتثبيتها إذا لزم الأمر
# install_package("requests")
def language(cookie):
        try:
            cookies= {'cookie': cookie }
            with requests.Session() as xyz:
                req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookies)
                pra = BeautifulSoup(req.content,'html.parser')
                for x in pra.find_all('form',{'method':'post'}):
                    if 'English (US)' in str(x):
                        bahasa = {
                            "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                            "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                            "submit"  : "English (US)"}
                        url = 'https://mbasic.facebook.com' + x['action']
                        exec = xyz.post(url,data=bahasa,cookies=cookies)
                        return cookie
        except Exception as e : print(e)
cookie =  'fr=0bCuhpAj9EIzsnnux.AWVfJuXRPeiE99YTDJDaex2sudQ.BmHsbp..AAA.0.0.BmHsbw.AWW-_icLM8U;xs=14%3ApLrFqvtoCkJXgg%3A2%3A1713293039%3A-1%3A-1;c_user=61558145110966;m_page_voice=61558145110966;wd=500x158;datr=6cYeZpiMo-1KgOsQyzK40Cm-;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1713293041305%2C%22v%22%3A1%7D;sb=KhMyZqYe0_Vg3lBHHWFJpFPb '
print(language(cookie.replace(" ", "")))

# def clone_repository(repo_url):
#     current_dir = os.getcwd()
#     target_dir = os.path.join(current_dir, repo_url.split('/')[-1].replace('.git', ''))

#     try:
#         print(f"Cloning from {repo_url} into {target_dir}")
#         Repo.clone_from(repo_url, target_dir)
#         print("Repository cloned successfully!")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# repository_url = "https://github.com/kreemkhaled112/ahmed"
# clone_repository(repository_url)
