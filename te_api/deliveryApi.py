# 发货
# express_number	String	Y	K73487736	快递单号
# id	int	Y	12323	订单id
# express_id	int	Y	1	快递id
# user_id	int	Y	10023	管理员用户id
from te_api import base
from setting import HEADERS
class Delivery:
    def __init__(self):
        self.url = 'http://121.42.15.146:9090/mtx/admin.php?s=/order/delivery.html'

    def delivery(self,session,order_id,user_id):
        data = {
            'express_number': '44444445',
            'id': order_id,
            'express_id': 1,
            'user_id': user_id,
        }

        resp_deli = session.post(self.url, data=data, headers=HEADERS)

        return resp_deli
