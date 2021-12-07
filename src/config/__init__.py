'''
Author: your name
Date: 2021-10-23 12:54:28
LastEditTime: 2021-11-02 14:08:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /triangleBlockchainOracle/config/__init__.py
'''

# pool = PooledDB(pymysql, maxconnections=6, host=config.HOST, port=config.PORT, db=config.DATABASE, user=config.USER, passwd=config.PASSWORD, charset=config.CHARSET, cursorclass=pymysql.cursors.DictCursor )

# HOST="localhost"
# PORT=3306
# DATABASE="triangleOracle"
# USER="root"
# PASSWORD="triangleDao2021"
# CHARSET="utf8"

HOST="triangle-dao-dev.cn5pjjgx2jud.us-west-1.rds.amazonaws.com"
PORT=3306
DATABASE="triangledao-pricefeed"
USER="admin"
PASSWORD="XTMejoJfSpzz0yyCgHTw"
CHARSET="utf8"

# AWS MySQL 数据库, 外网可以连接
# host: triangle-dao-dev.cn5pjjgx2jud.us-west-1.rds.amazonaws.com
# port: 3306
# username: admin
# password: XTMejoJfSpzz0yyCgHTw

# Price status


STATUS = {
    "SUBMITTED": 0, # 数据提交
    "SUCCESS": 1    # 区块数据成功被打包
}


# For conflux

owner_private_key = "0B6A7A4CF9C143421D948E6E33C7C84BF6882E39F8B2EE56FD29303E659E4F3B"
owner_user_address = "cfxtest:aate5nxwmdrdavgwjb46ntn3k6zfym9z76s1jckvud"



# Wrapped XD, [Nov 2, 2021 at 5:50:50 PM (Nov 2, 2021 at 10:42:54 PM)]:
# AWS EC2 登录, 测试用途, 在美西, ssh 需要命令行里翻墙一下:

# ssh ubuntu@13.57.204.164
# 密码: triangle1234

# nvm 装好了, 切换 node 版本可以用 nvm use 14 或者 nvm use 12
# python3.8 也已经装好了, 直接可以用, 命令是 python3, 不过最好都用虚拟环境

# 代码都可以放在 ~/workspace 里面, 这样回头好记一点

# Wrapped XD, [Nov 2, 2021 at 5:51:15 PM (Nov 2, 2021 at 6:05:18 PM)]:
# @ranlix @junior_shanxuan A  需要的话可以用，有其他需求就和我说。然后你们可以注册个 https://leancloud.app 然后把帐号给我, 我把你们加入到一个 app 里，大家共用一个数据库。

