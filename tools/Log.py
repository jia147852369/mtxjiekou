import logging
import logging.handlers

# 一般来讲，我们在程序中记录日志出自下面几个方面的需求。
#
# *快速定位问题的根源，
# *追踪程序执行的过程
# *追踪数据的变化



class GetLooger:
    def __init__(self):
        self.logger = logging.getLogger()# 获取日志器(日记本)
    def get_logger(self):

        # 给日志器设置总的级别,级别是封装在logging里面的
        # 我要设置错误级别,完全大写
        self.logger.setLevel(logging.INFO)
        # 2.获取格式器
        # 2.1这个只是要输出的样式
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
        # 2.2 获取格式器 参数  具体要输出什么样的样式
        fm = logging.Formatter(fmt)
        # 3.获取处理器  按时间切割的文件处理器工作中用midnight  ,backupCount=3  除了原件，只保存最新的三个
        tf = logging.handlers.TimedRotatingFileHandler(filename='../logger/test.logger',
                                                  when='H',
                                                  interval=1,
                                                  backupCount=3,
                                                  encoding='utf-8')

        # 在处理器中添加格式器
        tf.setFormatter(fm)
        # 在日志器中添加处理器
        self.logger.addHandler(tf)

        #实际上我们希望记录日志文件的同时，也能在控制台进行输出。方便调试。
        #所以我们为这个日志对象，新建一个用于输出的处理器
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(fm)
        self.logger.addHandler(ch)
        conslon = self.logger.addHandler(ch)

        self.logger.removeHandler(conslon)

        return self.logger

if __name__ == '__main__':
    # 测试日志调用的时候
    logger = GetLooger().get_logger()
    logger.debug('调试')
    logger.info('信息')
    logger.warning('警告')
    logger.error('错误')
    logger.critical('致命的')