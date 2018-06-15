# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\xiangmu\项目\page_ui\me_changeinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_comment1 import *
from Ui_praise1 import *

import sys
from client_msg_deal import ClientMsgDeal
from admin import Admin
from messagestable import Messages
from commentstable import Comments


client = ClientMsgDeal()
username = 'wumeng'
userid = 1

# from Ui_me import *


class Ui_message1(object):

    def __init__(self, client):
        self.client = client

    def setupUi(self, message1):
        # 创建Comment对象属性
        self.u = Comment()
        self.Dialog = QtWidgets.QDialog()
        self.u.setupUi1(self.Dialog)

        # 创建praise对象的属性
        self.p = Praise()
        self.Dialog2 = QtWidgets.QDialog()
        self.p.setupUi2(self.Dialog2)

        # 把窗口变为属性
        self.message1 = message1
        # 居中
        self.center()
        # 对话框命名
        message1.setObjectName("message1")
        message1.setEnabled(True)
        # 对话框大小
        message1.resize(400, 600)
        message1.setMinimumSize(QtCore.QSize(400, 600))
        message1.setMaximumSize(QtCore.QSize(400, 600))
        message1.setMouseTracking(False)
        message1.setStyleSheet("border-color: rgb(255, 0, 0);\n"
                               "color: rgb(0, 0, 0);")
        self.centralWidget = QtWidgets.QWidget(message1)
        self.centralWidget.setObjectName("centralWidget")
        # 创建home_page按钮
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
        icon1.addPixmap(QtGui.QPixmap("imgs/black information.png"),
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
        icon4.addPixmap(QtGui.QPixmap("imgs/white.png"),
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
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 81, 18))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.toolButton_comment = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton_comment.setGeometry(QtCore.QRect(0, 60, 401, 91))
        self.toolButton_comment.setMinimumSize(QtCore.QSize(401, 91))
        self.toolButton_comment.setMaximumSize(QtCore.QSize(401, 91))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_comment.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imgs/comments.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_comment.setIcon(icon5)
        self.toolButton_comment.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_comment.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_comment.setObjectName("toolButton_comment")
        self.toolButton_praise = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton_praise.setGeometry(QtCore.QRect(0, 149, 401, 91))
        self.toolButton_praise.setMinimumSize(QtCore.QSize(401, 91))
        self.toolButton_praise.setMaximumSize(QtCore.QSize(401, 91))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_praise.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("imgs/good-filling.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_praise.setIcon(icon6)
        self.toolButton_praise.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_praise.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_praise.setObjectName("toolButton_praise")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 241, 400, 291))
        self.textBrowser.setMinimumSize(QtCore.QSize(400, 291))
        self.textBrowser.setMaximumSize(QtCore.QSize(400, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("font: 12pt \"Arial\";background-color:rgba(235,237,244,0.8);")
        message1.setCentralWidget(self.centralWidget)

        self.retranslateUi(message1)

        self.home_page.clicked.connect(self.home_page_fun)
        # 调消息页面绑定
        self.message.clicked.connect(self.message_fun)
        # 发微博页面的绑定
        self.new_blog.clicked.connect(self.new_blog_fun)
        self.search.clicked.connect(self.search_fun)
        # self.search.clicked.connect(self.s)
        # 调我的页面绑定
        self.me_.clicked.connect(self.me_fun)
        # comment评论键链接评论页面
        self.toolButton_comment.clicked.connect(self.comment_function)
        # 绑定评论页面返回键
        self.u.toolButton.clicked.connect(self.back)
        # praise键绑定praise页面
        self.toolButton_praise.clicked.connect(self.praise_function)
        # self.toolButton_comment.clicked.connect(self.comment_news)
        # praise页面返回键链接主页面
        self.p.toolButton.clicked.connect(self.praise_back)
        QtCore.QMetaObject.connectSlotsByName(message1)

    # 调消息页面
    def message_fun(self, username):
        l='新功能敬请期待!'
        self.textBrowser.setText(l)

    # 调管理员消息
    #def administrator_message(self):
        

        
            
        #self.textBrowser.setText(l)

    def new_blog_fun(self):
        pass

    # 调我的页面
    def me_fun(self):
        pass

    def home_page_fun(self):
        pass

    def search_fun(self):
        pass

    # 调comment页面的函数
    def comment_function(self):
        #ut = Ui_Dialog()

        self.Dialog.show()
        self.message1.hide()
        l = ''
        # 通过用户id和评论块调用
        statuscode, blogmsglist = self.client.do_show_bloginfo(1, 2)
        if statuscode == '0000':
            print(len(blogmsglist))
           
            for admin in blogmsglist:

                msg = admin.getmessagesobject()
                # 本用户消息
                znews = msg.getmessagesinfo()
                print('1234456788', znews)
                l+='****************************************'+'\n'
                l += '消息' + '\n'
                l += znews
                l += '\n'
                l += '------------------------------------------------------'+'\n'
                l += '用户评论' + '\n'
                

                comname = admin.getusername()

                l += comname
                comtime = admin.getadminstime()
                l += '\n'
                l += comtime
                l += '\n'
                comcontent = admin.getcommentinfo()
                l += comcontent+'\n'
                l += '\n'
                    # l += '----------------------------------------------------------------------'+'\n'
            l += '****************************************'+'\n'
            l+='\n'
            self.u.textBrowser.setText(l)

        elif statuscode == '0001':
            l += '暂时没有评论呦!'
            self.u.textBrowser.setText(l)

        else:
            l += '请稍后刷新重试!'
            self.u.textBrowser.setText(l)

     # comment页面返回消息页面
    def back(self):
        self.message1.show()
        self.Dialog.hide()
        self.u.textBrowser.setText('')
    # 调praise页面
    def praise_function(self):

        self.Dialog2.show()
        self.message1.hide()
        l = ''
        statuscode, blogmsglist = self.client.do_show_bloginfo(1, 0)
        if statuscode == '0001':
            l += '暂时没有点赞呦!'
            self.p.textBrowser.setText(l)
           
        elif statuscode == '0002':
            l += '请稍后刷新重试!'
            self.p.textBrowser.setText(l)
            
        else:
        # 通过用户id和赞块调用
            statuscode, blogmsglist = self.client.do_show_bloginfo(1, 2)
            if statuscode == '0000':

                for admin in blogmsglist:
                    msg = admin.getmessagesobject()
                    # 本用户消息
                    znews = msg.getmessagesinfo()
                    print('1234456788', znews)
                    l+='****************************************'+'\n'
                    l += '消息' + '\n'
                    l += znews
                    l += '\n'
                    l += '-----------------------------------------------------------------'+'\n'
                    l += '点赞用户' + '\n'
                   
                    comname = admin.getusername()
                    l += comname
                    comtime = admin.getadminstime()
                    l += comtime
                    l += '\n'
                l += '****************************************'+'\n'
                l+='\n'
                self.p.textBrowser.setText(l)

    # praise页面返回消息页面
    def praise_back(self):
        self.message1.show()
        self.Dialog2.hide()
        self.p.textBrowser.setText('')

    # 居中
    def center(self):
        qr = self.message1.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.message1.move(qr.topLeft())

    

    def retranslateUi(self, message1):
        _translate = QtCore.QCoreApplication.translate
        message1.setWindowTitle(_translate("message1", "weibo"))
        self.home.setText(_translate("message1", "微 博"))
        self.msg.setText(_translate("message1", "消 息"))
        self.aboutme.setText(_translate("message1", "我"))
        self.search_.setText(_translate("message1", "发 现"))
        self.label.setText(_translate("message1", "消息"))
        self.toolButton_praise.setText(_translate("message1", "赞"))
        self.toolButton_comment.setText(_translate("message1", "评论"))


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    message1 = QtWidgets.QMainWindow()
    ui = Ui_message1(client)
    ui.setupUi(message1)
    message1.show()
    sys.exit(app.exec_())
