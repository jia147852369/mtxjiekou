# 加入购物车
from te_api.base import baseReq


class addCartApi(baseReq):
    def add_cart(self,session):
        url = self.url + 'mtx/index.php?s=/index/cart/save.html'
        data = {'goods_id': 1, 'stock': 2}
        # headers = {'X-Requested-With': 'XMLHttpRequest'}
        resp_add = session.post(self.url, data=data, headers=self.HEADERS)
        return resp_add