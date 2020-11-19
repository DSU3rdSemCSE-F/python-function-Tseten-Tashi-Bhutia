from selenium import webdriver

class Google:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Tseten\chromedriver_win32\chromedriver')

    def search(self, key):






