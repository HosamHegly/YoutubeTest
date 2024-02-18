import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Infra.base_page import BasePage


class YouTubeVideoPage(BasePage):
    VIDEO_TITLE = (By.XPATH, "//h1[@class='style-scope ytd-watch-metadata']")
    LIKE_BUTTON = (By.CSS_SELECTOR, "button[title*='I like this']")
    DISLIKE_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='Dislike this video']")
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, 'paper-button[aria-label*="Subscribe"]')
    RECOMMENDED_VIDEOS = (By.XPATH, '//a[@id="thumbnail"][@href]')
    CURRENT_TIME_ELEMENT = (By.XPATH, "//span[@class='ytp-time-current']")
    PLAY_BUTTON = (By.XPATH, "//div[@id='player-container-inner']//button[@class='ytp-play-button ytp-button']")
    FULLSCREEN_BUTTON = (By.XPATH, "//div[@id='movie_player']//button[@class='ytp-fullscreen-button ytp-button']")
    VIDEO_SCREEN = (By.XPATH, "//div[@id='content']//video")

    def __init__(self, driver):
        super().__init__(driver)
        self.init_elements()

    def init_elements(self):
        self.like_button = self.get_like_button()
        self.dislike_button = self.get_dislike_button()
        self.play_button = self.get_play_button()
        self.fullscreen_button = self.get_fullscreen_button()
        self.video_screen = self.get_video_screen()

    def get_current_play_time(self):
        return int(self._driver.find_element(*self.CURRENT_TIME_ELEMENT).text.split(":")[1])

    def get_play_button(self):
        return self._driver.find_element(*self.PLAY_BUTTON)

    def get_video_title(self):
        return self._driver.find_element(*self.VIDEO_TITLE).text

    def get_like_button(self):
        return self._driver.find_element(*self.LIKE_BUTTON)

    def get_fullscreen_button(self):
        return self._driver.find_element(*self.FULLSCREEN_BUTTON)

    def get_screen_height_width(self):
        style_string = self.video_screen.get_attribute('style')

        width_match = re.search(r'width: (\d+)px', style_string)
        height_match = re.search(r'height: (\d+)px', style_string)

        width = width_match.group(1) if width_match else None
        height = height_match.group(1) if height_match else None
        return int(width), int(height)

    def click_fullscreen_button(self):
        self.fullscreen_button.click()

    def click_like_button(self):
        self.like_button.click()
        self.like_button = self.get_like_button()
        self.dislike_button = self.get_dislike_button()

    def get_dislike_button(self):
        return self._driver.find_element(*self.DISLIKE_BUTTON)

    def click_dislike_button(self):
        self.dislike_button.click()
        self.like_button = self.get_like_button()
        self.dislike_button = self.get_dislike_button()

    def subscribe_to_channel(self):
        self._driver.find_element(*self.SUBSCRIBE_BUTTON).click()

    def get_recommended_video_titles(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_all_elements_located(self.RECOMMENDED_VIDEOS)
        )
        recommended_videos = self._driver.find_elements(*self.RECOMMENDED_VIDEOS)
        titles = []
        for video in recommended_videos:
            title = video.get_attribute('title')
            if title:  # Some thumbnails might not have a title attribute
                titles.append(title)
        return titles

    def is_like_button_clicked(self):
        if self.like_button.get_attribute('aria-pressed') == "true":
            return True
        else:
            return False

    def is_dislike_button_clicked(self):
        if self.like_button.get_attribute('aria-pressed') == "true":
            return True
        else:
            return False

    def is_video_playing(self):
        initial_time = self.get_current_play_time()
        time.sleep(2)
        final_time = self.get_current_play_time()
        return final_time > initial_time

    def click_play_button(self):
        self.play_button.click()
        self.play_button = self.get_play_button()
        time.sleep(1)

    def is_video_paused(self):
        initial_time = self.get_current_play_time()
        time.sleep(5)
        final_time = self.get_current_play_time()
        return final_time == initial_time

    def get_video_screen(self):
        return self._driver.find_element(*self.VIDEO_SCREEN)

    def is_full_screen(self):
        width_before, height_before = self.get_screen_height_width()
        self.click_fullscreen_button()
        self.video_screen = self.get_video_screen()
        width_after, height_after = self.get_screen_height_width()

        return width_before < width_after and height_before < height_after
