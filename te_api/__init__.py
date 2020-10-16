'''
接口发起请求
'''

from te_api.addCartApi import addCartApi
from te_api.loginAdminApi import AdminLogin
from te_api.loginApi import MtxLogin
from te_api.orderApi import Order
from te_api.payOrderApi import PayOrder
from te_api.deliveryApi import Delivery

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))