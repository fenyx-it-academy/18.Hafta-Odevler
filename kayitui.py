# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cinsiyet_group = QtWidgets.QGroupBox(self.centralwidget)
        self.cinsiyet_group.setObjectName("cinsiyet_group")
        self.gridLayout = QtWidgets.QGridLayout(self.cinsiyet_group)
        self.gridLayout.setObjectName("gridLayout")
        self.bayan = QtWidgets.QRadioButton(self.cinsiyet_group)
        self.bayan.setObjectName("bayan")
        self.gridLayout.addWidget(self.bayan, 0, 0, 1, 1)
        self.erkek = QtWidgets.QRadioButton(self.cinsiyet_group)
        self.erkek.setObjectName("erkek")
        self.gridLayout.addWidget(self.erkek, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.cinsiyet_group, 7, 0, 1, 1)
        self.soyad_line = QtWidgets.QLineEdit(self.centralwidget)
        self.soyad_line.setObjectName("soyad_line")
        self.gridLayout_2.addWidget(self.soyad_line, 1, 2, 1, 2)
        self.ad = QtWidgets.QLabel(self.centralwidget)
        self.ad.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.ad.setObjectName("ad")
        self.gridLayout_2.addWidget(self.ad, 0, 0, 1, 1)
        self.ad_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ad_line.setObjectName("ad_line")
        self.gridLayout_2.addWidget(self.ad_line, 0, 2, 1, 2)
        self.soyadi = QtWidgets.QLabel(self.centralwidget)
        self.soyadi.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.soyadi.setObjectName("soyadi")
        self.gridLayout_2.addWidget(self.soyadi, 1, 0, 1, 2)
        self.mail_line = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_line.setObjectName("mail_line")
        self.gridLayout_2.addWidget(self.mail_line, 3, 2, 1, 2)
        self.mail = QtWidgets.QLabel(self.centralwidget)
        self.mail.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mail.setObjectName("mail")
        self.gridLayout_2.addWidget(self.mail, 3, 0, 1, 1)
        self.mail_tekrar = QtWidgets.QLabel(self.centralwidget)
        self.mail_tekrar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.mail_tekrar.setObjectName("mail_tekrar")
        self.gridLayout_2.addWidget(self.mail_tekrar, 4, 0, 1, 2)
        self.pas_tek_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pas_tek_line.setObjectName("pas_tek_line")
        self.gridLayout_2.addWidget(self.pas_tek_line, 6, 2, 1, 2)
        self.medeni_durum = QtWidgets.QLabel(self.centralwidget)
        self.medeni_durum.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.medeni_durum.setObjectName("medeni_durum")
        self.gridLayout_2.addWidget(self.medeni_durum, 2, 0, 1, 1)
        self.medeni_hal = QtWidgets.QLineEdit(self.centralwidget)
        self.medeni_hal.setObjectName("medeni_hal")
        self.gridLayout_2.addWidget(self.medeni_hal, 2, 2, 1, 2)
        self.mail_tekrar_line = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_tekrar_line.setObjectName("mail_tekrar_line")
        self.gridLayout_2.addWidget(self.mail_tekrar_line, 4, 2, 1, 2)
        self.pasword = QtWidgets.QLabel(self.centralwidget)
        self.pasword.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.pasword.setObjectName("pasword")
        self.gridLayout_2.addWidget(self.pasword, 5, 0, 1, 1)
        self.pas_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pas_line.setObjectName("pas_line")
        self.gridLayout_2.addWidget(self.pas_line, 5, 2, 1, 2)
        self.pasword_tekrar = QtWidgets.QLabel(self.centralwidget)
        self.pasword_tekrar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.pasword_tekrar.setObjectName("pasword_tekrar")
        self.gridLayout_2.addWidget(self.pasword_tekrar, 6, 0, 1, 1)
        self.kurallar = QtWidgets.QTextEdit(self.centralwidget)
        self.kurallar.setStyleSheet("font: 8pt \"MS UI Gothic\";\n"
"COLOR:rgb(255, 0, 0)")
        self.kurallar.setObjectName("kurallar")
        self.gridLayout_2.addWidget(self.kurallar, 7, 2, 1, 2)
        self.kontrol = QtWidgets.QCheckBox(self.centralwidget)
        self.kontrol.setObjectName("kontrol")
        self.gridLayout_2.addWidget(self.kontrol, 8, 0, 1, 1)
        self.buton_kayit = QtWidgets.QPushButton(self.centralwidget)
        self.buton_kayit.setObjectName("buton_kayit")
        self.gridLayout_2.addWidget(self.buton_kayit, 9, 3, 1, 1)
        self.buton_esc = QtWidgets.QPushButton(self.centralwidget)
        self.buton_esc.setObjectName("buton_esc")
        self.gridLayout_2.addWidget(self.buton_esc, 9, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.MENU = QtWidgets.QMenuBar(MainWindow)
        self.MENU.setGeometry(QtCore.QRect(0, 0, 790, 23))
        self.MENU.setObjectName("MENU")
        MainWindow.setMenuBar(self.MENU)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cinsiyet_group.setTitle(_translate("MainWindow", "CINSIYET"))
        self.bayan.setText(_translate("MainWindow", "BAYAN"))
        self.erkek.setText(_translate("MainWindow", "ERKEK"))
        self.ad.setText(_translate("MainWindow", "ADINIZ"))
        self.soyadi.setText(_translate("MainWindow", "SOYADINIZ"))
        self.mail.setText(_translate("MainWindow", "MAIL"))
        self.mail_tekrar.setText(_translate("MainWindow", "MAIL TEKRAR"))
        self.medeni_durum.setText(_translate("MainWindow", "MEDENI DURUMUNUZ"))
        self.pasword.setText(_translate("MainWindow", "PASWORD"))
        self.pasword_tekrar.setText(_translate("MainWindow", "PASWORD TEKRAR"))
        self.kurallar.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">KURALLAR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">1- LUTFEN BILGILERINIZI DOGRU GIRINIZ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">2- PASWORDUNUZ EN AZ 8 KARAKTERDEN OLUSMALIDIR.LUTFEN GUCLU BIR PASWORD ICIN EN AZ BIR SAYI ,BIR BUYUK HARF,BIR SAYI VE BIR ISARET KARAKTERLERIYLE GUCLENDIRMEYI UNUTMAYIN.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\">3- BU BILGILER 3.SAHISLARLA PARA KARSILIGINDA PAYLASILABILIR</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt;\"><br /></p></body></html>"))
        self.kontrol.setText(_translate("MainWindow", "OKUDUM KABUL EDIYORUM"))
        self.buton_kayit.setText(_translate("MainWindow", "KAYDET"))
        self.buton_esc.setText(_translate("MainWindow", "IPTAL"))
