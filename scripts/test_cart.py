import requests
import pytest
from te_api.addCartApi import addCartApi
from te_api.loginApi import MtxLogin


class TestCart:
    def setup(self):
        self.session = requests.session()
        self.cart_obj = addCartApi()
        self.login_obj = MtxLogin()

    def test_add_cart(self):

        self.login_obj.login(self.session)
        resp_cart = self.cart_obj.add_cart(self.session)
        # print(resp_cart.json().get('msg'))
        assert resp_cart.status_code == 200
        # assert resp_cart.json().get('msg') == "加入成功"

    def teardown(self):
        self.session.close()
