#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: base.py
# @Author: Bull
# ---
import requests
from setting import HEADERS
from tools.logger import GetLooger


class baseReq():
    logger = GetLooger().get_logger()

    def __init__(self,url='http://121.42.15.146:9090/mtx/'):
        self.url = url
        self.HEADERS = HEADERS

    def post_template(self,url:str,data:dict,session=requests.Session()):
        url = self.url + url
        print(url)
        self.logger.info(f'base方法请求的是:{url}')
        resp = session.post(url, data=data, headers=HEADERS)
        self.logger.info(f'base方法的响应是:{resp.text}')
        return resp
if __name__ == '__main__':


    url = 'index.php?s=/index/user/login.html'
    data = {'accounts': 'yaoyao', 'pwd': 'yaoyao'}

    req = baseReq()
    print(req.post_template(url,data).text)
