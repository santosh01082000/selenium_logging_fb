from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class FacebookLogin():
    
    def __init__(self):
        '''    Credentials    '''
        self.url = config.URL 
        self.email = config.EMAIL
        self.password = config.PWD
        self.search_name = config.SEARCH_NAME
        
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)
    
    
    def login(self):
        '''    Authentication    '''
        try:
            username = self.driver.find_element('id', 'email')
            username.send_keys(self.email)
            
            password = self.driver.find_element('id', 'pass')
            password.send_keys(self.password)
            
            login_button = self.driver.find_element('id', 'loginbutton')
            login_button.click()
            
            print("Login Success")
            
            return True
        except:
            return False
    
    def search(self):
        if self.login():
        
            try:
                # wait 10 seconds before looking for element
                search_option = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(('xpath', "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input"))
                )
                search_option.send_keys(self.search_name)
                time.sleep(10)
            except:
                print("not responding")
            # waite time 10 sec    
            finally:
                #else quit
                self.driver.quit()
          
 
 
if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = FacebookLogin()
    fb_login.search()
    
