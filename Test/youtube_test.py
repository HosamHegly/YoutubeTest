import time

import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import unittest

from Infra.browser_wrapper import BrowserWrapper
from Logic.youtube_page import YoutubePage
import Utils
from Logic.youtube_result_page import YouTubeResultsPage


class YoutubeHomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("https://www.youtube.com/")
        self.youtube_page = YoutubePage(self.driver)

    def test_search_for_video_title(self):
        search_text = 'la campanella'
        self.youtube_page.search_flow(search_text)
        self.youtube_result = YouTubeResultsPage(self.driver)
        first_video_title = self.youtube_result.get_first_video_title().lower()
        self.assertTrue(Utils.have_common_word(search_text, first_video_title))

    def tearDown(self):
        self.browser.close_browser()
