#!/usr/bin /env  python
# coding:utf-8 
"""
@version:  2.7.14
@author:  Long
@file:  crawl_url.py
@time: 2018/7/18 10:19
"""
import json
import requests
import re
import bs4
from bs4 import BeautifulSoup

class CrawlUrl(object):
    """
    根据给定的url，关键字，起止时间来爬取页面
    """
    results_test = 0
    @classmethod
    def _multi_two_crawl(cls, url, key_words, limit_times):
        """
        针对关键字和起止时间都是list
        :param url: 主站url
        :param key_words: 关键字
        :param limit_time: 起止时间
        :return: 所有包含关键字的urls
        """
        urls = []
        url_json = {}
        for key_word,limit_time in key_words, limit_times:
            url_res = cls._single_crawl(url, key_word, limit_time)
            url_json[key_word] = url_res
            urls.append(url_json)
        return urls

    @classmethod
    def _multi_single_crawl(cls, url, key_words, limit_time):
        """
        针对关键字是list
        :param url: 主站url
        :param key_words: 关键字 list
        :param limit_time: 起止时间 str
        :return: 所有包含关键字的urls
        """
        urls = []
        url_json = {}
        for key_word in key_words:
            url_res = cls._single_crawl(url, key_word, limit_time)
            url_json[key_word] = url_res
            urls.append(url_json)
        return urls

    @classmethod
    def _single_crawl(cls, url, key_word, limit_time):
        """
        大豆:soybean 豆粕:sbm 乳清粉:whey 玉米:yumi
        :param url: 主站url
        :param key_words: 关键字 str
        :param limit_time: 起止时间 str
        :return: 所有包含关键字的urls
        """
        crawl_url = ""
        start_time = limit_time.split("-")[0]
        stop_time = limit_time.split("-")[1]
        if key_word == "大豆":
            crawl_url = url[:28] + "soybean"
        if key_word == "豆粕":
            crawl_url = url[:28] + "sbm"
        if key_word == "乳清粉":
            crawl_url = url[:28] + "whey"
        if key_word == "玉米":
            crawl_url = url[:28] + "yumi"
        urls = cls._parse_page(crawl_url, start_time, stop_time)
        return urls

    @classmethod
    def _parse_page(cls, url, start_time, stop_time):
        #print url
        url_result = []
        results_test = url
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        soup = bs4.BeautifulSoup(response.content,"html.parser")
        key_word = soup.title.contents[0][:2]
        results = soup.find_all(class_="globalRight")
        for result in results:
            a_tag = result.select("a")[0]

            if key_word in a_tag["title"]:
                target_date = result.find_all(class_="globalSpanTime")[0].text[1:6]
                if cls._compare_date(start_time, stop_time, target_date):
                    url_result.append(a_tag["href"])

        return url_result

    @classmethod
    def _compare_date(cls, start_time, stop_time, target_date):
        """比较日期是否在区间"""
        min_month = int(start_time[:2])
        min_day = int(start_time[2:])
        max_month = int(stop_time[:2])
        max_day = int(stop_time[2:])
        target_month = int(target_date[:2])
        target_day = int(target_date[3:])
        if min_month <= target_month <= max_month:
            if min_day <= target_day <= max_day:
                return True
        return False

    @classmethod
    def start_crawl(cls, url, key_words, limit_time):
        """
        根据关键字，起止时间，和url来爬取页面的urls
        :param url: 主站url
        :param key_words: 关键字
        :param limit_time: 起止时间
        :return: 所有包含关键字的urls
        """
        key_words = str(key_words.decode("utf-8"))
        limit_time = str(limit_time.decode("utf-8"))
        url = url.decode("utf-8")
        urls = []
        if isinstance(key_words, list) and isinstance(limit_time, list):
            urls = cls._multi_two_crawl(url, key_words, limit_time)
            CrawlUrl.results_test = 1
        elif isinstance(key_words, list) and isinstance(limit_time, str):
            urls = cls._multi_single_crawl(url, key_words, limit_time)
            CrawlUrl.results_test = 2
        elif isinstance(key_words, str) and isinstance(limit_time, str):
            urls = cls._single_crawl(url, key_words, limit_time)
            urls = {key_words:urls}
            CrawlUrl.results_test = 3
        CrawlUrl.results_test = 4
        return urls


