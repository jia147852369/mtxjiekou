import requests
from te_api.loginAdminApi import AdminLogin
class TestAdminLogin:
    def setup(self):
        self.session = requests.Session()
        self.adminlogin_obj = AdminLogin()

    def test_admin_login(self):
        resp_adminlogin = self.adminlogin_obj.admin_login(self.session)
        assert resp_adminlogin.status_code == 200
        assert resp_adminlogin.json().get('msg')=='登录成功'
