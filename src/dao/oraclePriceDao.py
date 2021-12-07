'''
Author: your name
Date: 2021-10-24 11:35:42
LastEditTime: 2021-11-02 15:39:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/src/dao/oraclePriceDao.py
'''

from dao import GeneralDao
import traceback
from util import getTimeStamp

class oraclePriceDao(GeneralDao):

    def __init__(self) -> None:
        super(oraclePriceDao, self).__init__()
    
    def insert(self, source, price, symbol, avg_time, txHash):     

        create_time = getTimeStamp()
        update_time = getTimeStamp()
        sql = "insert into `oracle_price` (`source`, `price`, `symbol`, `avg_time`, `txHash`, `create_time`, `update_time`) values('%s', %d, '%s', %d, '%s', %d, %d)"%(source, price, symbol, avg_time, txHash ,create_time, update_time)

        try:
            with self.connection.cursor() as cursor:
                # TypeError: %d format: a number is required, not str
                cursor.execute(sql)
                self.connection.commit()

                return True
        except:
            print(sql)
            traceback.print_exc()
            return False

    # get the lastest symbol price
    def getTheLatestOraclePrice(self, symbol):
        try:
            sql = "select `source`, `price`, `symbol`, `avg_time`,  `update_time`, `create_time`, `txHash` from oracle_price where `symbol` = %s"
            cursor.execute(sql, (symbol))
            data = cursor.fetchall()
            return True, data

        except:
            traceback.print_exc()
            return False
            
    