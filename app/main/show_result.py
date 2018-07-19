#!/usr/bin /env  python
# coding:utf-8 
"""
@version:  2.7.14
@author:  Long
@file:  show_result.py
@time: 2018/7/18 19:18
"""
from flask import Flask
from flask import request,render_template
from flask.wrappers import Response
from crawl_url import CrawlUrl

app = Flask(__name__)

@app.route("/crawl",methods=['POST','GET'])
def crawl_page():
    key_word = request.form["key_word"]
    limit_time = request.form["limit_time"]
    print key_word,limit_time
    return "OK"

@app.route("/", methods=['GET'])
def index_page():
    return render_template("index.html")