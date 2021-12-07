'''
Author: Junior

'''



import sys
import os
cwdPath = os.getcwd()

sys.path.insert(0, cwdPath)

import traceback
import pymysql.cursors
import config
from dbutils.pooled_db import PooledDB

# from DBUtils.PooledDB import PooledDB

pool = PooledDB(pymysql, maxconnections=6, host=config.HOST, port=config.PORT, db=config.DATABASE, user=config.USER, passwd=config.PASSWORD, charset=config.CHARSET, cursorclass=pymysql.cursors.DictCursor )

# def getConnection():
#     # Connect to the database
#     conn = pool.connection()  #以后每次需要数据库连接就是用connection（）函数获取连接就好了
#     return conn

class MetaSingleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance

class GeneralDao(metaclass=MetaSingleton):

    # 共享connection
    connection = None

    def __init__(self) -> None:
        self.connect()
    
    def __del__(self):
        if self.connection is not None:
            self.connection.close()

        print("db connection return connection pool")

    def connect(self):
        if self.connection is None:
            self.connection = pool.connection()

    def insert(self):
        pass
    
    def pageQuery(self, table, fields , page, row, wherelimits = None, orderBy = None, desc = False, spcialCaesForReward = True):

        sql = "select " + ",".join(fields) + " from %s "%(table)
  
        if wherelimits is not None:
            sql = sql + " where "
            
            wherelimitsLen = len(wherelimits)
            for idx, wherelimit in enumerate(wherelimits):         
                res = []
                for k, t in wherelimit.items():
                    v, relation = t
                    res.append(" `%s` %s '%s' "%(k,relation,v))
               
                sql = sql + "( " + "and".join(res) + " )"
                if wherelimitsLen > 1 and idx < wherelimitsLen - 1:
                    sql = sql + " or "
            

        # order By
        if orderBy is not None:
            sql = sql + " order by %s"%(orderBy)
            if desc is True:
                sql = sql + " DESC "

        # 分页逻辑
        # 这里也有一个很特殊的分页逻辑，RewardList的计算需要查多一条数据

        if spcialCaesForReward:
            sql = sql + " limit %s, %s " %(page * row, row + 1)
        else:
            sql = sql + " limit %s, %s " %(page * row, row )

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchall()

                return True, data
        except:
            traceback.print_exc()
            print(" ============ sql error ============")
            print(sql)
            print(wherelimits)
            print(" ============ sql error ============")
            return False, None
        

    def delete(self):
        pass

    def update(self):
        pass



if __name__ == "__main__":
    dao = GeneralDao()
