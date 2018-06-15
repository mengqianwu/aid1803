# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\Study\Tedu_AID1803\micro\microblog\pages\page_ui\me_changepwd.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

old_pwd = ['123456']

class Ui_changepwd(object):
    def setupUi(self, changepwd):
        changepwd.setObjectName("changepwd")
        changepwd.setEnabled(True)
        changepwd.resize(400, 600)
        changepwd.setMinimumSize(QtCore.QSize(400, 600))
        changepwd.setMaximumSize(QtCore.QSize(400, 600))
        changepwd.setMouseTracking(False)
        changepwd.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                         "color: rgb(0, 0, 0);")
        # changepwd.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.changepwd = changepwd

        self.centralWidget = QtWidgets.QWidget(changepwd)
        self.centralWidget.setObjectName("centralWidget")
        self.userinfo = QtWidgets.QGroupBox(self.centralWidget)
        self.userinfo.setGeometry(QtCore.QRect(10, 40, 381, 501))
        self.userinfo.setObjectName("userinfo")
        self.uname = QtWidgets.QLabel(self.userinfo)
        self.uname.setGeometry(QtCore.QRect(16, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uname.setFont(font)
        self.uname.setAlignment(QtCore.Qt.AlignCenter)
        self.uname.setObjectName("uname")
        self.stime = QtWidgets.QLabel(self.userinfo)
        self.stime.setGeometry(QtCore.QRect(120, 100, 230, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stime.setFont(font)
        self.stime.setText("")
        self.stime.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.stime.setObjectName("stime")
        self.nickname = QtWidgets.QLabel(self.userinfo)
        self.nickname.setGeometry(QtCore.QRect(120, 40, 230, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nickname.setFont(font)
        self.nickname.setText("")
        self.nickname.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nickname.setObjectName("nickname")
        self.confirm_pwd = QtWidgets.QLineEdit(self.userinfo)
        self.confirm_pwd.setGeometry(QtCore.QRect(110, 303, 241, 35))
        self.confirm_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_pwd.setObjectName("confirm_pwd")
        self.layoutWidget_2 = QtWidgets.QWidget(self.userinfo)
        self.layoutWidget_2.setGeometry(QtCore.QRect(15, 150, 81, 201))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.old = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.old.setFont(font)
        self.old.setAlignment(QtCore.Qt.AlignCenter)
        self.old.setObjectName("old")
        self.verticalLayout_2.addWidget(self.old)
        self.new = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new.setFont(font)
        self.new.setAlignment(QtCore.Qt.AlignCenter)
        self.new.setObjectName("new")
        self.verticalLayout_2.addWidget(self.new)
        self.confirm = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirm.setFont(font)
        self.confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm.setObjectName("confirm")
        self.verticalLayout_2.addWidget(self.confirm)
        self.old_pwd = QtWidgets.QLineEdit(self.userinfo)
        self.old_pwd.setGeometry(QtCore.QRect(110, 163, 241, 35))
        self.old_pwd.setMaxLength(9)
        self.old_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_pwd.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.old_pwd.setObjectName("old_pwd")
        self.new_pwd = QtWidgets.QLineEdit(self.userinfo)
        self.new_pwd.setGeometry(QtCore.QRect(110, 234, 241, 35))
        self.new_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pwd.setObjectName("new_pwd")
        self.confirm_btn = QtWidgets.QCommandLinkButton(self.userinfo)
        self.confirm_btn.setGeometry(QtCore.QRect(230, 400, 101, 41))
        self.confirm_btn.setObjectName("confirm_btn")
        self.cancle_btn = QtWidgets.QCommandLinkButton(self.userinfo)
        self.cancle_btn.setGeometry(QtCore.QRect(40, 400, 101, 41))
        self.cancle_btn.setObjectName("cancle_btn")
        self.siguptime = QtWidgets.QLabel(self.userinfo)
        self.siguptime.setGeometry(QtCore.QRect(16, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.siguptime.setFont(font)
        self.siguptime.setAlignment(QtCore.Qt.AlignCenter)
        self.siguptime.setObjectName("siguptime")
        self.home_page = QtWidgets.QPushButton(self.centralWidget)
        self.home_page.setGeometry(QtCore.QRect(10, 540, 71, 41))
        self.home_page.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/white house.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_page.setIcon(icon)
        self.home_page.setIconSize(QtCore.QSize(30, 30))
        self.home_page.setFlat(True)
        self.home_page.setObjectName("home_page")
        self.home = QtWidgets.QLabel(self.centralWidget)
        self.home.setGeometry(QtCore.QRect(30, 575, 41, 20))
        self.home.setObjectName("home")
        self.message = QtWidgets.QPushButton(self.centralWidget)
        self.message.setGeometry(QtCore.QRect(88, 545, 75, 31))
        self.message.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/white information.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.message.setIcon(icon1)
        self.message.setIconSize(QtCore.QSize(30, 30))
        self.message.setFlat(True)
        self.message.setObjectName("message")
        self.msg = QtWidgets.QLabel(self.centralWidget)
        self.msg.setGeometry(QtCore.QRect(110, 575, 41, 20))
        self.msg.setObjectName("msg")
        self.new_blog = QtWidgets.QPushButton(self.centralWidget)
        self.new_blog.setGeometry(QtCore.QRect(144, 545, 111, 51))
        self.new_blog.setAutoFillBackground(False)
        self.new_blog.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/plus sign.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_blog.setIcon(icon2)
        self.new_blog.setIconSize(QtCore.QSize(50, 50))
        self.new_blog.setFlat(True)
        self.new_blog.setObjectName("new_blog")
        self.search = QtWidgets.QPushButton(self.centralWidget)
        self.search.setGeometry(QtCore.QRect(240, 545, 61, 31))
        self.search.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/white search.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon3)
        self.search.setIconSize(QtCore.QSize(30, 30))
        self.search.setFlat(True)
        self.search.setObjectName("search")
        self.me_ = QtWidgets.QPushButton(self.centralWidget)
        self.me_.setGeometry(QtCore.QRect(320, 545, 61, 31))
        self.me_.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/black.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.me_.setIcon(icon4)
        self.me_.setIconSize(QtCore.QSize(30, 30))
        self.me_.setFlat(True)
        self.me_.setObjectName("me_")
        self.aboutme = QtWidgets.QLabel(self.centralWidget)
        self.aboutme.setGeometry(QtCore.QRect(330, 575, 41, 20))
        self.aboutme.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutme.setObjectName("aboutme")
        self.search_ = QtWidgets.QLabel(self.centralWidget)
        self.search_.setGeometry(QtCore.QRect(260, 575, 41, 20))
        self.search_.setObjectName("search_")

        self.tip_pwd = QtWidgets.QLabel(self.userinfo)
        self.tip_pwd.setGeometry(QtCore.QRect(80, 350, 241, 35))
        self.tip_pwd.setText("")
        self.tip_pwd.setObjectName("tip_pwd")


        # changepwd.setCentralWidget(self.centralWidget)

        self.retranslateUi(changepwd)
        # self.home_page.clicked.connect(self.home_page.click)
        # self.message.clicked.connect(self.message.click)
        # self.new_blog.clicked.connect(self.new_blog.click)
        # self.search.clicked.connect(self.search.click)
        # self.me_.clicked.connect(self.me_.click)
        self.cancle_btn.clicked.connect(self.cancle_btn.click)
        self.confirm_btn.clicked.connect(self.confirm_btn.click)
        # QtCore.QMetaObject.connectSlotsByName(changepwd)

        self.old_pwd.textChanged[str].connect(self.onChanged)
        self.new_pwd.textChanged[str].connect(self.onChanged)
        self.confirm_pwd.textChanged[str].connect(self.pwdCheck)

        self.get_info()

    def retranslateUi(self, changepwd):
        _translate = QtCore.QCoreApplication.translate
        changepwd.setWindowTitle(_translate("changepwd", "密码修改"))
        self.userinfo.setTitle(_translate("changepwd", "账号信息"))
        self.uname.setText(_translate("changepwd", "昵    称"))
        self.old.setText(_translate("changepwd", "旧的密码"))
        self.new.setText(_translate("changepwd", "新的密码"))
        self.confirm.setText(_translate("changepwd", "确认密码"))
        self.old_pwd.setPlaceholderText(
            _translate("changepwd", "请输入您旧的的密码"))
        self.new_pwd.setPlaceholderText(
            _translate("changepwd", "密码6-9位，数字字母，必须以字母开头"))
        self.confirm_btn.setText(_translate("changepwd", "确认修改"))
        self.cancle_btn.setText(_translate("changepwd", "取消返回"))
        self.siguptime.setText(_translate("changepwd", "注册时间"))
        self.home.setText(_translate("changepwd", "微 博"))
        self.msg.setText(_translate("changepwd", "消 息"))
        self.aboutme.setText(_translate("changepwd", "我"))
        self.search_.setText(_translate("changepwd", "发 现"))


    def onChanged(self, text):
        if not text:
            self.tip_pwd.setText("您输入的密码为空， 请重新输入！")
        elif len(text) < 6:
            self.tip_pwd.setText("您输入的密码长度小于6， 请重新输入！")
        else:
            self.tip_pwd.setText('')

    def usr_input(self):
        self.old_t = self.old_pwd.text()
        self.passwd_t = self.new_pwd.text()
        self.passwd_confirm_t = self.confirm_pwd.text()

    def pwdCheck(self, text):
        self.usr_input()
        if self.old_t != old_pwd[0]:
            self.tip_pwd.setText("您的密码不正确，请重新输入！")
        elif self.passwd_t != text:
            self.tip_pwd.setText("您两次输入的密码不一致，请重新输入！")
        else:
            self.tip_pwd.setText("")

    def get_info(self):
        self.nickname.setText('翱翔的格格巫')
        info = ['F','1991-01-24','2018-05-20','既然选择了远方,便只顾风雨兼程! 乘风破浪会有时,直挂云帆济沧海!','1024','256']
        self.stime.setText(info[2])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changepwd = QtWidgets.QMainWindow()
    ui = Ui_changepwd()
    ui.setupUi(changepwd)
    changepwd.show()
    sys.exit(app.exec_())
