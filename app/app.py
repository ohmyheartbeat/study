#!/usr/bin /env  python
# coding:utf-8 
"""
@version:  2.7.14
@author:  Long
@file:  app.py
@time: 2018/7/18 10:18
"""
import json

from flask import Flask
from flask import request,render_template
from flask.wrappers import Response
from main.crawl_url import CrawlUrl
import sys
import os

# Other imports

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder,static_folder=static_folder)
else:
    app = Flask(__name__)

@app.route("/crawl",methods=['POST','GET'])
def crawl_page():
    key_word = request.form["key_word"].encode("utf-8")
    url = request.form["url"].encode("utf-8")
    limit_time = request.form["limit_time"].encode("utf-8")
    urls = CrawlUrl.start_crawl(url,key_word,limit_time)
    return Response(json.dumps(urls), content_type="application/json")

@app.route("/", methods=['GET'])
def index_page():
    return render_template("index.html")
if __name__ == "__main__":
    app.run("0.0.0.0",9098,debug=True)
