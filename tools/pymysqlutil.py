import pymysql

class DataBaseHandle(object):
    """定义MYSQL数据库操作类"""
    def __init__(self):
        """初始化数据库信息创建连接"""
        self.host = 'host'
        self.username = 'root'
        self.password = '123456'
        self.database = 'dbname'
        self.port = 3306
        self.db = pymysql.connect(self.host,self.username,self.password,self.database,self.port,charset='utf8')

    def insertDB(self, sql):
        """插入数据"""
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('insert data error:', err)
            self.db.rollback()  # 发生错误时回滚
        finally:
            self.cursor.close()

    def deleteDB(self,sql):
        """删除数据"""
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('delete data error:',err)
            self.db.rollback()
        finally:
            self.cursor.close()

    def updateDB(self,sql):
        """修改数据"""
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('update data error:',err)
            self.db.rollback()
        finally:
            self.cursor.close()

    def selectDb(self,sql):
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchall() # 返回所有记录列表

            print(data)

            # 结果遍历
            for row in data:
                sid = row[0]
                name = row[1]
                # 遍历打印结果
                print('sid = %s,  name = %s'%(sid,name))
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()

    def closeDB(self):
        """关闭数据库连接"""
        self.db.close()

if __name__ == '__main__':
    DbHandle = DataBaseHandle()
    # DbHandle.insertDB('INSERT INTO minitor(id,used_order) VALUES ("999","321")')
    # DbHandle.deleteDB('DELETE FROM minitor WHERE id="999"')
    # DbHandle.updateDB('UPDATE minitor SET used_order="888" WHERE id="999"')
    # data = DbHandle.selectDB('SELECT * FROM minitor WHERE id="999" LIMIT 10')
    # dataList = [{'id':123,'used_order':777},{'id':789,'used_order':555}]
    # DbHandle.insertListDB('minitor',dataList)
    DbHandle.closeDB()
