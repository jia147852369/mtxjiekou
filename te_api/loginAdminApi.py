# 登录管理员账号 /mtx/admin.php?s=/admin/login.html
from setting import HEADERS
class AdminLogin:
    def __init__(self):
        self.url = 'http://121.42.15.146:9090/mtx/admin.php?s=/admin/login.html'

    def admin_login(self,session):

        data = {
            'username': 'shamo',
            'login_pwd': 123456,
        }
        resp_admin_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_admin_login
