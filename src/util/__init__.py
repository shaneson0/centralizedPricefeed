'''
Author: your name
Date: 2021-10-24 11:37:19
LastEditTime: 2021-11-02 11:33:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/src/util/__init__.py
'''


'''
Author: your name
Date: 2021-06-22 00:33:35
LastEditTime: 2021-08-17 17:00:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /rtoken-user-info/util/__init__.py
'''


import json
from urllib import request
import time


def transferETHUseraddress(user_address, rsymbol):
    if rsymbol == SymbolMapId["RETH"]:
        return user_address.lower()
    else:
        return user_address

def getLastMonthTimeStamp():
    # 1天的时间戳是86400，这里假设每个月是30天。
    return getTimeStamp() - 86400 * 30;

def getTimeStamp():
    timeStamp = time.time()
    return int(timeStamp)

def http_post(url, data_json): 
    header_dict = { 'User-Agent': 'PostmanRuntime/7.26.8', 'Content-Type': 'application/json'} 
    jdata = json.dumps(data_json).encode('utf-8')    
    req = request.Request(url, headers=header_dict) 
    response = request.urlopen(req, jdata) 
    body = response.read()
    response = json.loads(body)
    return response

def http_get(url):
    TimeLimit = 3
    while TimeLimit > 0:
        try:
            header_dict = { 'User-Agent': 'PostmanRuntime/7.26.8', 'Content-Type': 'application/json'} 
            req = request.Request(url, headers=header_dict) 
            response = request.urlopen(req) 
            body = response.read()
            response = json.loads(body)
            return response
        except:
            # too many connnection问题
            TimeLimit = TimeLimit - 1
            time.sleep(5)
            print("http_get error !! retry %s time !!"%(TimeLimit))

    return None


