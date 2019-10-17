# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KAYIT_FORMU_ODEV.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(549, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_6_email_tk = QtWidgets.QLabel(Form)
        self.label_6_email_tk.setObjectName("label_6_email_tk")
        self.gridLayout.addWidget(self.label_6_email_tk, 4, 0, 1, 1)
        self.label_ad = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_ad.setFont(font)
        self.label_ad.setOpenExternalLinks(False)
        self.label_ad.setObjectName("label_ad")
        self.gridLayout.addWidget(self.label_ad, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.label_4_yas = QtWidgets.QLabel(Form)
        self.label_4_yas.setObjectName("label_4_yas")
        self.gridLayout.addWidget(self.label_4_yas, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 8, 1, 1, 1)
        self.label_11_soz_kur = QtWidgets.QLabel(Form)
        self.label_11_soz_kur.setObjectName("label_11_soz_kur")
        self.gridLayout.addWidget(self.label_11_soz_kur, 9, 0, 1, 1)
        self.checkBox_oay_tik = QtWidgets.QCheckBox(Form)
        self.checkBox_oay_tik.setObjectName("checkBox_oay_tik")
        self.gridLayout.addWidget(self.checkBox_oay_tik, 10, 1, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 7, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.pushButton_kayit = QtWidgets.QPushButton(Form)
        self.pushButton_kayit.setObjectName("pushButton_kayit")
        self.gridLayout.addWidget(self.pushButton_kayit, 11, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5_email = QtWidgets.QLabel(Form)
        self.label_5_email.setObjectName("label_5_email")
        self.gridLayout.addWidget(self.label_5_email, 3, 0, 1, 1)
        self.label_2_soyad = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2_soyad.setFont(font)
        self.label_2_soyad.setObjectName("label_2_soyad")
        self.gridLayout.addWidget(self.label_2_soyad, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.label_7_cinsiyt = QtWidgets.QLabel(Form)
        self.label_7_cinsiyt.setObjectName("label_7_cinsiyt")
        self.gridLayout.addWidget(self.label_7_cinsiyt, 5, 0, 1, 1)
        self.label_3_medeni_dur = QtWidgets.QLabel(Form)
        self.label_3_medeni_dur.setObjectName("label_3_medeni_dur")
        self.gridLayout.addWidget(self.label_3_medeni_dur, 6, 0, 1, 1)
        self.label_9_parola = QtWidgets.QLabel(Form)
        self.label_9_parola.setObjectName("label_9_parola")
        self.gridLayout.addWidget(self.label_9_parola, 7, 0, 1, 1)
        self.label_10_parl_tek = QtWidgets.QLabel(Form)
        self.label_10_parl_tek.setObjectName("label_10_parl_tek")
        self.gridLayout.addWidget(self.label_10_parl_tek, 8, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 9, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton_2_iptal = QtWidgets.QPushButton(Form)
        self.pushButton_2_iptal.setObjectName("pushButton_2_iptal")
        self.gridLayout.addWidget(self.pushButton_2_iptal, 12, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">KAYIT FORMU</span></p></body></html>"))
        self.label_6_email_tk.setText(_translate("Form", "E-mail tekrar "))
        self.label_ad.setText(_translate("Form", "Ad                                "))
        self.label_4_yas.setText(_translate("Form", "Yasiniz "))
        self.label_11_soz_kur.setText(_translate("Form", "Sozlesme kurallari"))
        self.checkBox_oay_tik.setText(_translate("Form", "okudum onayliyorum"))
        self.radioButton_3.setText(_translate("Form", "BEKAR"))
        self.radioButton_4.setText(_translate("Form", "EVLI"))
        self.radioButton_5.setText(_translate("Form", "DUL"))
        self.pushButton_kayit.setText(_translate("Form", "Kayit ol"))
        self.label_5_email.setText(_translate("Form", "E-mail "))
        self.label_2_soyad.setText(_translate("Form", "Soyad"))
        self.radioButton_2.setText(_translate("Form", "BAYAN"))
        self.radioButton.setText(_translate("Form", "ERKEK"))
        self.label_7_cinsiyt.setText(_translate("Form", "Cinsiyet           "))
        self.label_3_medeni_dur.setText(_translate("Form", "Medeni durumunuz "))
        self.label_9_parola.setText(_translate("Form", "Parola"))
        self.label_10_parl_tek.setText(_translate("Form", "Parola tekrar"))
        self.plainTextEdit.setPlainText(_translate("Form", "This license applies to the Visual Studio Code product. Source Code for Visual Studio Code is available at https://github.com/Microsoft/vscode under the MIT license agreement at https://github.com/Microsoft/vscode/blob/master/license.txt. Additional license information can be found in our FAQ at https://code.visualstudio.com/docs/supporting/faq.\n"
"MICROSOFT SOFTWARE LICENSE TERMS\n"
"MICROSOFT VISUAL STUDIO CODE\n"
"These license terms are an agreement between you and Microsoft Corporation (or based on where you live, one of its affiliates). They apply to the software named above. The terms also apply to any Microsoft services or updates for the software, except to the extent those have different terms.\n"
"IF YOU COMPLY WITH THESE LICENSE TERMS, YOU HAVE THE RIGHTS BELOW.\n"
"1.    INSTALLATION AND USE RIGHTS.\n"
"a.    General.  You may use any number of copies of the software to develop and test your applications, including deployment within your internal corporate network.\n"
"b.    Demo use. The uses permitted above include use of the software in demonstrating your applications.\n"
"c.    Third Party Components. The software may include third party components with separate legal notices or governed by other agreements, as may be described in the ThirdPartyNotices file accompanying the software.\n"
"d.    Extensions. The software gives you the option to download other Microsoft and third party software packages from our extension marketplace or package managers. Those packages are under their own licenses, and not this agreement. Microsoft does not distribute, license or provide any warranties for any of the third party packages. By accessing or using our extension marketplace, you agree to the extension marketplace terms located at https://aka.ms/VSMarketplace-ToU. \n"
"2.    DATA.  \n"
"a.    Data Collection. The software may collect information about you and your use of the software, and send that to Microsoft. Microsoft may use this information to provide services and improve our products and services. You may opt-out of many of these scenarios, but not all, as described in the product documentation located at https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting. There may also be some features in the software that may enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable law, including providing appropriate notices to users of your applications together with Microsoft’s privacy statement. Our privacy statement is located at https://go.microsoft.com/fwlink/?LinkID=824704. You can learn more about data collection and use in the help documentation and our privacy statement. Your use of the software operates as your consent to these practices.\n"
"b.    Processing of Personal Data. To the extent Microsoft is a processor or subprocessor of personal data in connection with the software, Microsoft makes the commitments in the European Union General Data Protection Regulation Terms of the Online Services Terms to all customers effective May 25, 2018, at http://go.microsoft.com/?linkid=9840733.\n"
"3.    UPDATES.  The software may periodically check for updates and download and install them for you. You may obtain updates only from Microsoft or authorized sources. Microsoft may need to update your system to provide you with updates. You agree to receive these automatic updates without any additional notice. Updates may not include or support all existing software features, services, or peripheral devices. If you do not want automatic updates, you may turn them off by following the instructions in the documentation at http://go.microsoft.com/fwlink/?LinkID=616397.\n"
"4.    FEEDBACK.  If you give feedback about the software to Microsoft, you give to Microsoft, without charge, the right to use, share and commercialize your feedback in any way and for any purpose.   You will not give feedback that is subject to a license that requires Microsoft to license its software or documentation to third parties because we include your feedback in them.  These rights survive this agreement.\n"
"5.    SCOPE OF LICENSE. This license applies to the Visual Studio Code product. Source code for Visual Studio Code is available at https://github.com/Microsoft/vscode under the MIT license agreement. The software is licensed, not sold. This agreement only gives you some rights to use the software. Microsoft reserves all other rights. Unless applicable law gives you more rights despite this limitation, you may use the software only as expressly permitted in this agreement. In doing so, you must comply with any technical limitations in the software that only allow you to use it in certain ways. You may not\n"
"·    reverse engineer, decompile or disassemble the software, or otherwise attempt to derive the source code for the software except and solely to the extent required by third party licensing terms governing use of certain open source components that may be included in the software; \n"
"·    remove, minimize, block or modify any notices of Microsoft or its suppliers in the software;\n"
"·    use the software in any way that is against the law;\n"
"·    share, publish, rent or lease the software, or provide the software as a stand-alone offering for others to use.\n"
"6.    SUPPORT SERVICES. Because this software is “as is,” we may not provide support services for it.\n"
"7.    ENTIRE AGREEMENT. This agreement, and the terms for supplements, updates, Internet-based services and support services that you use, are the entire agreement for the software and support services.\n"
"8.    EXPORT RESTRICTIONS.  You must comply with all domestic and international export laws and regulations that apply to the software, which include restrictions on destinations, end-users, and end use. For further information on export restrictions, see www.microsoft.com/exporting.\n"
"9.    APPLICABLE LAW. If you acquired the software in the United States, Washington law applies to interpretation of and claims for breach of this agreement, and the laws of the state where you live apply to all other claims. If you acquired the software in any other country, its laws apply.\n"
"10.    CONSUMER RIGHTS; REGIONAL VARIATIONS. This agreement describes certain legal rights. You may have other rights, including consumer rights, under the laws of your state or country. Separate and apart from your relationship with Microsoft, you may also have rights with respect to the party from which you acquired the software. This agreement does not change those other rights if the laws of your state or country do not permit it to do so. For example, if you acquired the software in one of the below regions, or mandatory country law applies, then the following provisions apply to you:\n"
"a)    Australia. You have statutory guarantees under the Australian Consumer Law and nothing in this agreement is intended to affect those rights.\n"
"b)    Canada. If you acquired this software in Canada, you may stop receiving updates by turning off the automatic update feature, disconnecting your device from the Internet (if and when you re-connect to the Internet, however, the software will resume checking for and installing updates), or uninstalling the software. The product documentation, if any, may also specify how to turn off updates for your specific device or software.\n"
"c)    Germany and Austria.\n"
"(i)    Warranty. The properly licensed software will perform substantially as described in any Microsoft materials that accompany the software. However, Microsoft gives no contractual guarantee in relation to the licensed software.\n"
"(ii)    Limitation of Liability. In case of intentional conduct, gross negligence, claims based on the Product Liability Act, as well as, in case of death or personal or physical injury, Microsoft is liable according to the statutory law.\n"
"Subject to the foregoing clause (ii), Microsoft will only be liable for slight negligence if Microsoft is in breach of such material contractual obligations, the fulfillment of which facilitate the due performance of this agreement, the breach of which would endanger the purpose of this agreement and the compliance with which a party may constantly trust in (so-called \"cardinal obligations\"). In other cases of slight negligence, Microsoft will not be liable for slight negligence.\n"
"11.    DISCLAIMER OF WARRANTY. The software is licensed “as-is.”  You bear the risk of using it. Microsoft gives no express warranties, guarantees or conditions. To the extent permitted under your local laws, Microsoft excludes the implied warranties of merchantability, fitness for a particular purpose and non-infringement.\n"
"12.    LIMITATION ON AND EXCLUSION OF DAMAGES. You can recover from Microsoft and its suppliers only direct damages up to U.S. $5.00. You cannot recover any other damages, including consequential, lost profits, special, indirect or incidental damages.\n"
"This limitation applies to (a) anything related to the software, services, content (including code) on third party Internet sites, or third party applications; and (b) claims for breach of contract, breach of warranty, guarantee or condition, strict liability, negligence, or other tort to the extent permitted by applicable law.\n"
"It also applies even if Microsoft knew or should have known about the possibility of the damages. The above limitation or exclusion may not apply to you because your state or country may not allow the exclusion or limitation of incidental, consequential or other damages.\n"
"EULA ID: Visual Studio Code 14 November 2018"))
        self.pushButton_2_iptal.setText(_translate("Form", "Iptal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
