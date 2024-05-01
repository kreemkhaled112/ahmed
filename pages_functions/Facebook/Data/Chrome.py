from pages_functions.__init__ import *
from pages_functions.Facebook.Data.Edit import *

class Chrom:
    def __init__(self):
        self = self
        try:
            service = Service(executable_path="pages_functions/chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_extension('pages_functions/cookie.crx')
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2}
            # chrome_prefs = {"profile.default_content_setting_values.notifications": 2,"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", chrome_prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("--log-level=3")
            self.bot = webdriver.Chrome(service=service , options=options)
        except Exception as e:
            print(f"Failed to start the browser : \n{e}")

    def Login(self,email, password):
        try:
            bot = self.bot
            self.bot.get("https://www.facebook.com/login/")
            WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email.strip())
            WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.NAME, "pass"))).send_keys(password.strip())
            try:WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.NAME, "login"))).click()
            except:pass
            sleep(5)
            self.bot.get("https://www.facebook.com/profile.php?")
            sleep(2)
            cookies = bot.get_cookies()
            format = {}
            for cookie in cookies :
                format[cookie['name']] = cookie['value']
            cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
            bot.quit()
            return 'success' , cookie_string , Get_Name(cookie_string).Get()

        except Exception as e : return e
        
    def View(self,cook,close=None):
        try:
            self.bot.get("https://www.facebook.com/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.get("https://www.facebook.com/profile.php?")
            if 'checkpoint' in self.bot.current_url :
                if close == 'close':self.bot.quit()
                return 'checkpoint'
            else:
                cookie_string = self.update_cookie(cook)
                if close == 'close':self.bot.quit()
                return cookie_string
        except : return ''
    def Epsilon(self,user,password,cook):
        try:
            self.bot.get('https://moakt.com/ar')
            sleep(1)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/span[3]/input"))).send_keys(user)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/input[2]"))).click()
            self.bot.execute_script("window.open()")
            self.bot.switch_to.window(self.bot.window_handles[-1])
            self.bot.get("https://www.facebook.com/login/")
            WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(user.strip())
            WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.NAME, "pass"))).send_keys(password.strip())
            try:WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.NAME, "login"))).click()
            except:pass
            # cookies = cook.strip().split(";")
            # for cookie in cookies:
            #     cookie_parts = cookie.split("=")
            #     if len(cookie_parts) == 2:
            #         cookie_name, cookie_value = cookie_parts
            #         self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            # self.bot.get("https://www.facebook.com/profile.php?")
            if 'checkpoint' in self.bot.current_url :
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Get started')]"))).click()
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next')]"))).click()
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Get a code by email')]"))).click()
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Get code')]"))).click()
                # code = input("code: ")
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/label/div/div/input"))).send_keys(code)
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Submit')]"))).click()
                # input("......")
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next')]"))).click()
                # input("......")
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[4]/div/div/div/div/div[1]/div/span/span"))).click()
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[5]/div/div[2]/div/div/div[1]/div/span/span"))).click()
                # WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Back to Facebook')]"))).click()
                input("......")
                cookie_string = self.update_cookie(cook)
                self.bot.quit()
                return cookie_string
            else:
                input("......")
                cookie_string = self.update_cookie(cook)
                self.bot.quit()
                return cookie_string
        except : return ''
    def update_cookie(self,cook):
        try:
            cookies = self.bot.get_cookies()
            format = {}
            for cookie in cookies :
                format[cookie['name']] = cookie['value']
            cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
            try:
                cursor.execute(f"UPDATE account SET cookies = '{cookie_string} ' WHERE cookies = '{cook}'") ;conn.commit()
                return cookie_string
            except Exception as e : print(f"Faild Contect Database \n {e}")
        except : print("Faild Update Cookie")

    def scrap(self,id,cook):
        bot = self.bot
        files_in_folder = os.listdir('photo')
        largest_number = None
        for file_name in files_in_folder:
            numbers = file_name.replace(".jpg", "")
            numbers = [int(num) for num in numbers.split()]
            if numbers:
                current_largest = max(numbers)
                if largest_number is None or current_largest > largest_number:
                    largest_number = current_largest
        bot.get("https://www.facebook.com/")
        self.Add_cookie(cook)
        
        for user in id :
            bot.get(f"https://www.facebook.com/profile.php?id={user}")
            sleep(2)
            try:
                button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x1jx94hy x14yjl9h xudhj91 x18nykt9 xww2gxu x1iorvi4 x150jy0e xjkvuk6 x1e558r4']")))
                button.click()
                sleep(2)
                imag = bot.find_elements(By.CSS_SELECTOR, "img[class='x1bwycvy x193iq5w x4fas0m x19kjcj4']")

                p = [element.get_attribute('src') for element in imag]
                response = requests.get(p[0])
                open(f"photo/{largest_number+1}.jpg", "wb").write(response.content)
                largest_number += 1
            except:
                print("Not Found Photo")
