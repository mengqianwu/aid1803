# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-04
# Version: v0.3

'''
登录页面
登录成功进入下一页
登录失败判断原因进一步操作

'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_signup import Ui_Signup
# from client_msg_deal import ClientMsgDeal


class Ui_Login(object):
    # def __init__(self, server):
    #     self.server = server

    def setupUi(self, Login):
        # self.s = Ui_Signup()
        # self.dialog = QtWidgets.QDialog()
        # self.s.setupUi(self.dialog)
        Login.setObjectName("Login")
        Login.resize(400, 480)
        self.login = Login
        self.Signin = QtWidgets.QPushButton(Login)
        self.Signin.setGeometry(QtCore.QRect(50, 360, 110, 41))
        self.Signin.setObjectName("Signin")
        self.Signup = QtWidgets.QPushButton(Login)
        self.Signup.setGeometry(QtCore.QRect(240, 360, 110, 41))
        self.Signup.setObjectName("Signup")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username = QtWidgets.QLabel(Login)
        self.username.setGeometry(QtCore.QRect(25, 120, 91, 51))
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setScaledContents(False)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userpwd = QtWidgets.QLabel(Login)
        self.userpwd.setGeometry(QtCore.QRect(25, 210, 91, 51))
        self.userpwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userpwd.setScaledContents(False)
        self.userpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.userpwd.setObjectName("userpwd")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.welcome = QtWidgets.QLabel(Login)
        self.welcome.setGeometry(QtCore.QRect(40, 20, 201, 71))
        self.welcome.setObjectName("welcome")
        self.name = QtWidgets.QLineEdit(Login)
        self.name.setGeometry(QtCore.QRect(95, 130, 260, 31))
        self.name.setObjectName("name")
        self.passwd = QtWidgets.QLineEdit(Login)
        self.passwd.setGeometry(QtCore.QRect(95, 220, 260, 31))
        self.passwd.setObjectName("passwd")
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(60, 300, 281, 31))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Login)
        # 按钮绑定事件
        self.Signin.clicked.connect(self.judgement)
        self.Signup.clicked.connect(self.signup_page)
        # 从属注册页面的按钮事件
        # self.s.return_home.clicked.connect(self.back_signin)
        QtCore.QMetaObject.connectSlotsByName(Login)
        # 设置密码密文
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        # 调用保存设置文件查看用户名密码
        self.check_info()

        self.name.textChanged[str].connect(self.nameCheck)
        self.passwd.textChanged[str].connect(self.onChanged)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录/注册"))
        self.Signin.setText(_translate("Login", "登   录"))
        self.Signup.setText(_translate("Login", "注   册"))
        self.username.setText(_translate("Login", "用户名："))
        self.userpwd.setText(_translate("Login", "密  码："))
        self.welcome.setText(_translate("Login", "欢迎您登录/注册微博！"))

    # 用户名输入为空判定
    def nameCheck(self, text):
        if not text:
            self.label.setText("您输入的用户名为空， 请重新输入！")
        elif len(text) < 3:
            self.label.setText("您输入的用户名长度小于3， 请重新输入！")
        else:
            self.label.setText('')

    # 用户输入密码判断
    def onChanged(self, text):
        if not text:
            self.label.setText("您输入的密码为空， 请重新输入！")
        elif len(text) < 6:
            self.label.setText("您输入的密码长度小于6， 请重新输入！")
        else:
            self.label.setText('')

    def signup_page(self):
        self.login.hide()
        Go_signup = QtWidgets.QDialog()
        signup = Ui_Signup()
        signup.setupUi(Go_signup)
        Go_signup.show()
        sys.exit(Go_signup.exec_())
        self.login.show()

    # 从属注册页面的返回绑定
    # def back_signin(self):
    #     self.dialog.close
    #     self.login.show()

    # 获取用户输入信息
    def signin_info(self):
        self.name_text = self.name.text()
        self.passwd_text = self.passwd.text()
        # return (self.name_text, self.passwd_text)

    # 检查登录配置用户信息文件
    def check_info(self):
        self.signin_info()
        try:
            with open('user_information.txt', 'rb') as f:
                uname = f.readline().decode().strip()
                upwd = f.readline().decode().strip()
        except:
            pass
        else:
            self.name.setText(uname)
            self.passwd.setText(upwd)
            self.label.setText('')

     # 将用户信息保存到登录配置文件
    def save_info(self):
        try:
            with open('user_information.txt', 'wb') as f:
                f.writeline(self.name_text+'\n')
                f.writeline(self.passwd_text+'\n')
        except:
            pass

    # def go_main(self):
    #     self.dialog.hide()
    #     Main_page = QtWidgets.QDialog()
    #     main = Ui_Login()
    #     main.setupUi(Main_page)
    #     Main_page.show()
    #     sys.exit(Main_page.exec_())
    #     self.dialog.show()

    def judgement(self):
        self.signin_info()
        # self.label.setText('您输入的用户名是%s, 密码是%s' % (self.name_text, self.passwd_text))
        if not self.label.text():
            # info = self.server.do_login(self.name_text, self.passwd_text)
            info = ['0000']
            if info[0] == '0000':
                self.save_info()
                # 前往主页
                # go_main()
            elif info[0] == '0002':
                self.label.setText('您输入的用户名不存在, 请重新输入, 如没有账号请点击注册!')
            elif info[0] == '0003':
                self.label.setText('您输入的密码不正确!')
            else:
                self.label.setText('未知错误, 请重试!')
        else:
            self.label.setText("请输入您的用户名及密码...")


if __name__ == "__main__":
    # server = ClientMsgDeal()
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
