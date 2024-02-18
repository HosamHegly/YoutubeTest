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
from Logic.youtube_video_page import YouTubeVideoPage


class YoutubeVideoPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("https://www.youtube.com/")
        self.youtube_page = YoutubePage(self.driver)
        search_text = 'la campanella'
        self.youtube_page.search_flow(search_text)

    '''def test_like_video_button(self): user needs to be logged in first

        youtube_results = YouTubeResultsPage(self.driver)
        video_title_name = youtube_results.click_video_by_index(0)
        youtube_video_page = YouTubeVideoPage(self.driver)
        youtube_video_page.click_like_button()
        self.assertTrue(youtube_video_page.is_like_button_clicked())'''

    def test_check_if_video_plays(self):
        youtube_results = YouTubeResultsPage(self.driver)
        video_title_name = youtube_results.click_video_by_index(0)
        youtube_video_page = YouTubeVideoPage(self.driver)
        self.assertTrue(youtube_video_page.is_video_playing())

    def test_check_if_video_pauses(self):
        youtube_results = YouTubeResultsPage(self.driver)
        video_title_name = youtube_results.click_video_by_index(0)
        youtube_video_page = YouTubeVideoPage(self.driver)
        youtube_video_page.click_play_button()
        self.assertTrue(youtube_video_page.is_video_paused())

    def test_fullscreen_button(self):
        youtube_results = YouTubeResultsPage(self.driver)
        video_title_name = youtube_results.click_video_by_index(0)
        youtube_video_page = YouTubeVideoPage(self.driver)
        self.assertTrue(youtube_video_page.is_full_screen())



    def tearDown(self):
        self.browser.close_browser()
