# -*- coding:UTF-8 -*-
import os
import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains

from crawling.utils.readFile import ReadFile

class HtmlDownLoad(object):

    def __init__(self):
        config = ReadFile().readFile()
        self.driver = webdriver.PhantomJS(executable_path=config["path"])
        self.yz = True
        # self.yz = False

    # 实现页面的下载
    def DownLoad(self, url):
        if url is None:
            return None
        # 使用浏览器请求页面
        self.driver.get(url)
        # 获取整个加载后的网站
        # html = driver.find_element_by_tag_name("body")

        html = self.driver.page_source.encode()
        try:
            cat = self.driver.find_element_by_id("captchacharacters")
            cat.clear()
            print(self.driver.find_element_by_tag_name("img").get_attribute("src"))
            num = input("请输入验证码：")
            cat.click()
            cat.send_keys(num)
            self.driver.find_element_by_class_name("a-button-text").click()
            time.sleep(3)
            self.yz = False
        except:
            1
        html = self.driver.page_source.encode()
        # 返回下载好的内容
        return html

    def cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        return

    def getBrowser(self):
        return self.driver

    def closeBrowser(self):
        # 关闭浏览器
        if self.driver is None:
            self.driver.close()

    def checkLanguage(self, url):
        if url is None:
            return None
        # 使用浏览器请求页面
        self.driver.get(url)

        if self.yz:
            html = self.driver.page_source.encode()
            yanzheng = "lablpu"
            cat = self.driver.find_element_by_id("captchacharacters")
            cat.clear()
            cat.click()
            cat.send_keys(yanzheng)
            self.driver.find_element_by_class_name("a-button-text").click()
            time.sleep(3)
            self.yz = False

        html = self.driver.page_source.encode()
        dr = self.driver.find_element_by_class_name("icp-nav-link-inner")
        dr.click()
        time.sleep(2)
        html = self.driver.page_source.encode()


        self.closeBrowser()
        return
