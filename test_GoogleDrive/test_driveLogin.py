import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver

from PyTest.PageObject.DriveHomePage import GoogleDrivePage
from PyTest.PageObject.DriveLogin import LoginPage
from PyTest.PageObject.GoogleDoc import DocHomePage


# @pytest.fixture()
# def test_setup():
#     global driver
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield
#     driver.close()
#     driver.switch_to.window(driver.window_handles[1])
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])
#     driver.close()
from PyTest.utilities.BaseClass import BaseClass


class TestGoogleDrive(BaseClass):

    def test_Login_To_Google_Sheet(self):
        self.driver.get("https://drive.google.com")
        print(self.driver.title)
        self.driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        login = LoginPage(self.driver)
        login.enter_username("testuser30071")
        login.click_on_next_button()
        login.enter_password("Test@3007")
        login.click_on_pwd_next_button()
        time.sleep(2)
        drive = GoogleDrivePage(self.driver)
        time.sleep(2)
        drive.click_new_button()
        drive.click_google_sheet()
        print("Welcome to Google Sheet")
        self.driver.switch_to.window(self.driver.window_handles[2])
        print(self.driver.title)
        self.driver.find_element_by_css_selector("input[class='docs-title-input']").click()
        self.driver.implicitly_wait(3)
        act = ActionChains(self.driver)
        act.send_keys(Keys.BACKSPACE).perform()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/Sheettitlecleared.png")
        self.driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Sheet Experiment")
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/Sheettitleupdated.png")
        time.sleep(3)


    def test_Login_to_Google_Doc(self):
        self.driver.get("https://drive.google.com")
        print(self.driver.title)
        self.driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        login = LoginPage(self.driver)
        login.enter_username("testuser30071")
        login.click_on_next_button()
        login.enter_password("Test@3007")
        login.click_on_pwd_next_button()
        time.sleep(2)
        drive = GoogleDrivePage(self.driver)
        time.sleep(2)
        drive.click_new_button()
        drive.click_google_doc()
        print("welcome to Google Doc")
        self.driver.switch_to.window(self.driver.window_handles[2])
        print(self.driver.title)
        googledoc = DocHomePage(self.driver)
        googledoc.click_on_title()
        self.driver.implicitly_wait(3)
        act = ActionChains(self.driver)
        act.send_keys(Keys.BACKSPACE).perform()
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/DocTiltleCleared.png")
        googledoc.document_title("Automation Doc Experimet")
        # driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Doc Experiment")
        self.driver.get_screenshot_as_file(
            "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/DocTitleUpdated.png")


    # def test_Login_to_Google_slides(self):
    #     self.driver.get("https://drive.google.com")
    #     print(self.driver.title)
    #     self.driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
    #     #self.driver.switch_to.window(self.driver.window_handles[1])
    #     login = LoginPage(self.driver)
    #     login.enter_username("testuser30071")
    #     login.click_on_next_button()
    #     login.enter_password("Test@3007")
    #     login.click_on_pwd_next_button()
    #     time.sleep(2)
    #     drive = GoogleDrivePage(self.driver)
    #     time.sleep(2)
    #     drive.click_new_button()
    #     drive.click_google_slide()
    #     print("welcome to Google Slide")
    #     self.driver.switch_to.window(self.driver.window_handles[2])
    #     print(self.driver.title)
    #     self.driver.find_element_by_css_selector("input[class='docs-title-input']").click()
    #     self.driver.implicitly_wait(3)
    #     act = ActionChains(self.driver)
    #     act.send_keys(Keys.BACKSPACE).perform()
    #     self.driver.get_screenshot_as_file(
    #         "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/SlideTiltleCleared.png")
    #     self.driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Slide Experiment")
    #     self.driver.get_screenshot_as_file(
    #         "/Users/priyamvadaanand/PycharmProjects/google_selenium/POM/screenshots/SlideTitleUpdated.png")
    #
    #
    #
    # def test_Login_to_Google_createfolder(self):
    #     self.driver.get("https://drive.google.com")
    #     print(self.driver.title)
    #     self.driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
    #     #self.driver.switch_to.window(self.driver.window_handles[1])
    #     login = LoginPage(self.driver)
    #     login.enter_username("testuser30071")
    #     login.click_on_next_button()
    #     login.enter_password("Test@3007")
    #     login.click_on_pwd_next_button()
    #     drive = GoogleDrivePage(self.driver)
    #     time.sleep(2)
    #     drive.click_new_button()
    #     drive.create_folder("testcase6")
    #     time.sleep(2)
    #     drive.click_new_button()
    #     drive.create_folder("testcase7")
    #
    #     time.sleep(5)


    # @classmethod
    # # def tearDownClass(cls):
    # def tearDown(self):
    #     self.driver.quit()

