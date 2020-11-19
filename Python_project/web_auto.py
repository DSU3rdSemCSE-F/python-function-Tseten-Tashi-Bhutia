from selenium import webdriver
import pyttsx3 as p

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Tseten\chromedriver_win32\chromedriver')

    def get_info(self, query):
        self.query =query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath(r'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element_by_xpath(r'//*[@id="search-form"]/fieldset/button')
        enter .click()

        info = self.driver.find_element_by_xpath(r'//*[@id="mw-content-text"]/div[1]/p[1]')
        read_txt = info.text
        eng = p.init()
        eng.say(read_txt)
        eng.runAndWait()


#bot = info()
#bot.get_info("liberty bell")
