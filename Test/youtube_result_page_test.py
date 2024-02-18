import time

import selenium
from selenium import  webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import  unittest

from Infra.browser_wrapper import BrowserWrapper
from Logic.youtube_page import YoutubePage
import Utils
from Logic.youtube_result_page import YouTubeResultsPage
from Logic.youtube_video_page import YouTubeVideoPage


class YoutubeResultPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("https://www.youtube.com/")
        self.youtube_page = YoutubePage(self.driver)


    def test_select_video_by_title_check_if_title_matches_in_video_page(self):
        search_text = 'la campanella'
        self.youtube_page.search_flow(search_text)
        youtube_results = YouTubeResultsPage(self.driver)
        video_title_name = youtube_results.click_video_by_index(0)
        youtube_video_page = YouTubeVideoPage(self.driver)

        self.assertEqual(video_title_name,youtube_video_page.get_video_title())


    def tearDown(self):
        self.browser.close_browser()

