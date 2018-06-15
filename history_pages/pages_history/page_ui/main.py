# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-06
# Version: v0.1

'''
页面调用的主函数
负责所有页面按钮的监控及调用

'''

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_signin_signup import Ui_Login
from Ui_signup import Ui_Signup
from Ui_me import Ui_me
from Ui_me_changeinfo import Ui_changeinfo
from Ui_me_changepwd import Ui_changepwd
from Ui_login_tip import Ui_tip

static = 0


class Main(object):
    def __init__(self, Ui_me):
        app = QtWidgets.QApplication(sys.argv)
        self.Me = Ui_me()
        self.MeWindows = QtWidgets.QMainWindow()
        self.Me.setupUi(self.MeWindows)
        self.MeWindows.show()
        sys.exit(app.exec_())
        self.btn_click()

    def logstatic(self):
        if not static:
            self.loginTip = Ui_tip()
            self.logindialog = QtWidgets.QDialog()
            self.loginTip.setupUi(self.logindialog)
            self.Me.hide()
            self.logindialog.show()
        else:
            pass

    def btn_click(self):
        # 首页
        self.Me.home_page.clicked.connect(self.MeWindows.close)
        # 消息页面
        self.Me.message.clicked.connect(self.MeWindows.close)
        # 发布微博
        self.Me.new_blog.clicked.connect(self.logstatic)
        # 搜索
        self.Me.search.clicked.connect(self.MeWindows.close)
        # 修改信息
        self.Me.change_info.clicked.connect(self.changeInfo)
        # 修改密码
        self.Me.change_pwd.clicked.connect(self.changePwd)
        # # 微博及点赞记录页面
        # self.Me.blog.clicked.connect(self.blog.click)
        # self.Me.good.clicked.connect(self.good.click)
        # 修改信息页面按钮
        # Ui_changeinfo.cancle_btn.clicked.connect(self.cancle_info)
        # Ui_changeinfo.confirm_btn.clicked.connect(self.confirm_info)
        # # 修改密码页面按钮
        # Ui_changepwd.cancle_btn.clicked.connect(self.cancle_pwd)
        # Ui_changepwd.confirm_btn.clicked.connect(self.confirm_pwd)
        # # 提示登录页面
        # Ui_tip.signup.clicked.connect(self.do_signup)
        # Ui_tip.login.clicked.connect(self.do_login)
        # # 登录页面
        # Ui_Login.Signin.clicked.connect(self.judgement)
        # Ui_Login.Signup.clicked.connect(self.signup_page)
        # # 注册页面
        # Ui_Signup.return_home.clicked.connect(self.back_signin)
        # Ui_Signup.signup.clicked.connect(self.go_main)

    def changeInfo(self):
        self.info = Ui_changeinfo()
        self.changeinfo_dialog = QtWidgets.QDialog()
        self.info.setupUi(self.changeinfo_dialog)
        self.MeWindows.hide()
        self.info.show()

    def changePwd(self):
        self.pwd = Ui_changepwd()
        self.changepwd_dialog = QtWidgets.QDialog()
        self.pwd.setupUi(self.changepwd_dialog)
        self.MeWindows.hide()
        self.pwd.show()

    def cancle_info(self):
        self.changeinfo_dialog.close
        self.MeWindows.show()

    def confirm_info(self):
        self.changeinfo_dialog.close
        self.MeWindows.show()

    def cancle_pwd(self):
        pass

    def confirm_pwd(self):
        pass


Main(Ui_me)
