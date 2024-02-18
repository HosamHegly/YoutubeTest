from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Infra.base_page import BasePage


class YouTubeResultsPage(BasePage):
    VIDEO_TITLES = (By.XPATH, "//a[@id='video-title']")
    CHANNEL_NAME = (By.CLASS_NAME, 'ytd-channel-name')

    def __init__(self, driver):
        super().__init__(driver)
        self.video_titles = self.get_video_titles()
        self.channels = self.get_channel_names()

    def get_video_titles(self):
        return self._driver.find_elements(*self.VIDEO_TITLES)

    def get_channel_names(self):
        return self._driver.find_elements(*self.CHANNEL_NAME)

    def get_first_video_title(self):
        return self.video_titles[0].text

    def click_video_by_index(self, index):
        if index >= len(self.video_titles):
            raise IndexError("The index for the video you want to click is out of bound")
        title_name = self.video_titles[index].text
        self.get_video_titles()[index].click()
        self.wait_for_element_in_page_by_CSS('button[aria-label*="like this video"]')
        return title_name
