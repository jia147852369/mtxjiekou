# 支付订单
from setting import HEADERS


class PayOrder:
    def __init__(self):
        self.url = 'http://121.42.15.146:9090/mtx/admin.php?s=/order/pay.html'

    def pay_order(self,session,order_id,payment_id):
        data = {
            'id': order_id,
            'payment_id': payment_id
        }
        resp_payment = session.post(self.url, data=data, headers=HEADERS)

        return resp_payment