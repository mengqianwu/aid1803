学习中期项目
实现微博基础功能(发布微博, 点赞, 转发, 评论)
页面实现使用pyqt5
通信连接是基于TCP的短连接
通信采用xml格式化报文
用户密码采用哈希散列中的MD5算法转换
数据库使用MySQL

项目所需的环境在requirement.py中

运行项目需要修改包内每一个__init__.py中的路径为当前工作路径

一些可能用到的命令:
pip3 install pipreqs
pipreqs /path

pip --- Python2的标准第三方库管理工具
pip3 --- Python3的标准第三方库管理工具

安装软件
pip3 install Package
升级软件
pip3 install --upgrade Package
卸载软件
pip3 uninstall Package
查看软件包清单
pip3 list

查找软件包
pip3 search Package

查看软件包信息
pip3 show Package

记录软件环境
pip3 freeze >requirement.txt

根据环境文件进行环境安装
pip3 install -r requirement.txt