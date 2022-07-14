from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException   
import time

class FacebookLogin():
    
    def __init__(self):
        '''    Access Credentials From Config File    '''
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
            
            return True
        
        except Exception as e:
            return False
    
    def search(self):
        if self.login():
            try:
                self.driver.find_element('xpath', "//*[contains(text(), 'The password')]")
                print("Login Failed..!, please check your password")
                self.driver.close()
                self.driver.quit()
            except NoSuchElementException:
                try:
                    print("Successfully Login..!")
                    '''    wait 10 seconds before looking for element    '''
                    search_option = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(('xpath', "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input")))
                    search_option.send_keys(self.search_name)
                    time.sleep(5)
                except NoSuchElementException:
                    print("Failed to locate search element")
                finally:
                    self.driver.close()
                    self.driver.quit()
          
 
 
if __name__ == '__main__':
    '''    Created Instance Object For Main Class    '''
    fb_login = FacebookLogin()
    fb_login.search()
    
