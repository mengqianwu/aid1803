# -*- coding: utf-8 -*-

# Auther: Kepner Wu
# Date: 2018-06-07
# Version: v0.2

'''
浏览页面判断用户没有登录后启动

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_signin_signup import Ui_Login
from Ui_signup import Ui_Signup


class Ui_tip(object):
    def setupUi(self, tip):
        tip.setObjectName("tip")
        tip.setEnabled(True)
        tip.resize(400, 600)
        tip.setMinimumSize(QtCore.QSize(400, 600))
        tip.setMaximumSize(QtCore.QSize(400, 600))
        tip.setMouseTracking(False)
        tip.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.tip = tip
        self.centralWidget = QtWidgets.QWidget(tip)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 90, 291, 371))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.login = QtWidgets.QPushButton(self.groupBox)
        self.login.setGeometry(QtCore.QRect(70, 110, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.signup = QtWidgets.QPushButton(self.groupBox)
        self.signup.setGeometry(QtCore.QRect(70, 230, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup.setFont(font)
        self.signup.setObjectName("signup")

        self.retranslateUi(tip)
        self.signup.clicked.connect(self.do_signup)
        self.login.clicked.connect(self.do_login)
        QtCore.QMetaObject.connectSlotsByName(tip)

    def retranslateUi(self, tip):
        _translate = QtCore.QCoreApplication.translate
        tip.setWindowTitle(_translate("tip", "微博"))
        self.groupBox.setTitle(_translate("tip", "欢迎您使用微博"))
        self.login.setText(_translate("tip", "登   录"))
        self.signup.setText(_translate("tip", "注   册"))

    def do_login(self):
        self.tip.hide()
        Go_signup = QtWidgets.QDialog()
        signup = Ui_Login()
        signup.setupUi(Go_signup)
        Go_signup.show()
        self.tip.close

    def do_signup(self):
        self.tip.hide()
        Go_signup = QtWidgets.QDialog()
        signup = Ui_Signup()
        signup.setupUi(Go_signup)
        Go_signup.show()
        self.tip.close


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tip = QtWidgets.QMainWindow()
    ui = Ui_tip()
    ui.setupUi(tip)
    tip.show()
    sys.exit(app.exec_())

