import hashlib, base64


class Encrypt(object):
    """
    实现简单的md5 sha1 base64等加密算法的简单封装

    """

    def __init__(self, string):
        self._string = string.encode('utf-8')

    def md5(self):
        """
        实现MD5算法封装
        """
        try:
            md5String = hashlib.md5(self._string)
            return md5String.hexdigest()
        except:
            return False

    def sha1(self):
        """
        实现sha1算法封装
        """
        try:
            sha1String = hashlib.sha1(self._string)
            return sha1String.hexdigest()
        except:
            return False

    def base64encode(self):
        """
        实现base64 encode方法封装
        """
        try:
            return base64.b64encode(self._string).decode('utf-8')
        except:
            return False

    def base64decode(self):
        """
        实现base64 decode方法封装
        """
        try:
            return base64.b64decode(self._string).decode('utf-8')
        except:
            return False


if __name__ == '__main__':

    e = Encrypt("hello")  # 根据字符串初始化一个加密类

    e.md5()
    e.sha1()
    e.base64encode()
