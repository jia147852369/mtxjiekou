# 访问登录接口
import requests

from te_api.base import baseReq
from tools.logger import GetLooger

import os,sys

sys.path.append(os.getcwd())            #告诉pytest运行前先检索当前路径


class MtxLogin(baseReq):
    logger = GetLooger().get_logger()

    def __init__(self):
        self.url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/login.html'

    def login(self,session=requests.Session()):
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {'accounts':'bull','pwd':'123456'}
        resp_login = session.post(self.url,data=data,headers=headers)
        self.logger.error('测试用的调试信息')

        return resp_login

    # def login(self):
    #     url = 'index.php?s=/index/user/login.html'
    #     data = {'accounts': 'yaoyao', 'pwd': 'yaoyao'}
    #
    #     req = baseReq()
    #     print(req.post_template(url,data).text)

# a=MtxLogin()
# a.login()