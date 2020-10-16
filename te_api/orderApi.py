#提交订单(立即购买) 返回值里面有个id是订单号，与发货和支付进行关联
# /mtx/index.php?s=/index/buy/add.html

from setting import HEADERS

class Order:
    def __init__(self):
        self.url='http://121.42.15.146:9090/mtx/index.php?s=/index/buy/add.html'

    def order(self,session):

        data = {
            'goods_id': 1,
            'stock': 2,
            'buy_type': 'goods',
            'address_id': 600,
            'payment_id': 1,
            'spec': '',

        }
        resp_order = session.post(self.url,data=data,headers=HEADERS)


        # # 提取数据做数据关联
        order_id = resp_order.json().get('data').get('order').get('id')
        # setting.ORDER_ID = order_id
        # user_id = resp_order.json().get('data').get('order').get('user_id')
        # setting.USER_ID = user_id
        # payment_id = resp_order.json().get('data').get('order').get('payment_id')
        # setting.PAYMENT_ID = payment_id
        return resp_order