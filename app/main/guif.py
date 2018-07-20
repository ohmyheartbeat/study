#!/usr/bin /env  python
# coding:utf-8
"""
@version:  2.7.14
@author:  Long
@file:  crawl_url.py
@time: 2018/7/18 10:19
"""
from __future__ import print_function
import time
def main():
    # while True:
    for i in range(9):
        j = 1

        while j<=i+1:
            print("%d * %d = %d   " %(i+1,j,(i+1)*j),end="")
            j+=1
        print()
if __name__ == "__main__":
    main()
    raw_input("Press <enter>")