from selenium import webdriver


class youtube():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Tseten\chromedriver_win32\chromedriver')

    def music(self, name):
        self.name = name
        self.driver.get(url="https://www.youtube.com/results?search_query="+ name)
        vid = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        vid.click()


#bot = youtube()
#bot.music("BTS Dynamite")