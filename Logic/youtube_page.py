from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage


class YoutubePage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@id='search']")
    VIDEO_TITLES = (By.ID, 'video-title')
    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = self._driver.find_element(*self.SEARCH_INPUT)

    def fill_search_input(self,text):
        self.search_input.send_keys(text)

    def enter_on_search_input(self):
        self.search_input.send_keys(Keys.ENTER)


    def search_flow(self,text):
        self.fill_search_input(text)
        self.enter_on_search_input()
        self.wait_for_element_in_page_by_xpath("//a[@id='video-title']")
        self.enter_on_search_input()


    def get_first_video_title(self):
       title = self._driver.find_element(By.XPATH, "//a[@id='video-title']").text.lower()
       return title







