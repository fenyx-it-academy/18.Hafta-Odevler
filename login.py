# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(798, 600)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-color:rgb(170, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loginbutton.setEnabled(False)
        self.loginbutton.setGeometry(QtCore.QRect(70, 30, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.loginbutton.setFont(font)
        self.loginbutton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.loginbutton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255))\n"
"")
        self.loginbutton.setObjectName("loginbutton")
        self.userbutton = QtWidgets.QLabel(self.centralwidget)
        self.userbutton.setEnabled(False)
        self.userbutton.setGeometry(QtCore.QRect(30, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.userbutton.setFont(font)
        self.userbutton.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.userbutton.setFrameShape(QtWidgets.QFrame.Box)
        self.userbutton.setTextFormat(QtCore.Qt.AutoText)
        self.userbutton.setObjectName("userbutton")
        self.paswoordbutton = QtWidgets.QLabel(self.centralwidget)
        self.paswoordbutton.setEnabled(False)
        self.paswoordbutton.setGeometry(QtCore.QRect(30, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.paswoordbutton.setFont(font)
        self.paswoordbutton.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.paswoordbutton.setFrameShape(QtWidgets.QFrame.Box)
        self.paswoordbutton.setTextFormat(QtCore.Qt.AutoText)
        self.paswoordbutton.setObjectName("paswoordbutton")
        self.userbox = QtWidgets.QLineEdit(self.centralwidget)
        self.userbox.setGeometry(QtCore.QRect(150, 149, 161, 31))
        self.userbox.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.userbox.setObjectName("userbox")
        self.paswoordbox = QtWidgets.QLineEdit(self.centralwidget)
        self.paswoordbox.setGeometry(QtCore.QRect(150, 189, 161, 31))
        self.paswoordbox.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.paswoordbox.setObjectName("paswoordbox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 260, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 260, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.forgettext = QtWidgets.QTextBrowser(self.centralwidget)
        self.forgettext.setGeometry(QtCore.QRect(150, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setUnderline(True)
        font.setKerning(True)
        self.forgettext.setFont(font)
        self.forgettext.setObjectName("forgettext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginbutton.setText(_translate("MainWindow", "LOGIN"))
        self.userbutton.setText(_translate("MainWindow", "Username"))
        self.paswoordbutton.setText(_translate("MainWindow", "Passwoord"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign In"))
        self.pushButton_3.setText(_translate("MainWindow", "Sign Up"))
        self.forgettext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gabriola\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ff0000;\">Do you forget paswoord?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

