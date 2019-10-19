# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kullanici_kayit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(704, 584)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 470, 201, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(40, 20, 131, 17))
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(130, 130, 111, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 350, 611, 101))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(40, 530, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 330, 111, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 170, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 200, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 240, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 280, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 90, 111, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 101, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_ad = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_ad.setObjectName("lbl_ad")
        self.verticalLayout.addWidget(self.lbl_ad)
        self.lbl_soyad = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_soyad.setObjectName("lbl_soyad")
        self.verticalLayout.addWidget(self.lbl_soyad)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Onay"))
        self.checkBox.setText(_translate("Form", "Okudum Onayladim"))
        self.comboBox.setItemText(0, _translate("Form", "Evli"))
        self.comboBox.setItemText(1, _translate("Form", "Bekar"))
        self.plainTextEdit.setPlainText(_translate("Form", "Genel Koşullar\n"
"\n"
"Bu bölüm Kariyer.net\'in genel ve kanuni sorumluluklarını içerir. Lütfen, sitemizi kullanmadan önce aşağıda yazılı olanları dikkatli bir şekilde okuyunuz. Eğer aşağıda belirtilen şartları kısmen ve/veya tamamen kabul etmiyorsanız, Kariyer.net\'i herhangi bir amaçla kullanmayınız.\n"
"\n"
"Kariyer.net, bu sayfalarda belirtilen genel koşulları dilediği zaman ve şekilde değiştirme hakkını kendinde saklı tutar. Kariyer.net\'in www.kariyer.net adresini ziyaret ettiğinizde bu sayfayı da ziyaret etmeniz gerekmektedir. Bu nedenle www.kariyer.net adresini ziyaret ettiğinizde bu sayfayı da ziyaret ettiğiniz kabul edilir.\n"
"\n"
"Kopyalama\n"
"\n"
"Kariyer.net ticari amaçlarla olmamak koşulu ve sadece kendiniz tarafından kullanılmak şartı ile bir kereye mahsus olmak üzere, sitede belirtilen bilgilerin kopyalanmasına izin verir.\n"
"\n"
"Kariyer.net\'in içeriğinde yer alan bütün bilgilerin, yazıların, logoların, grafiklerin ve bunlarla sınırlı olmamak üzere her türlü görsel ve resimlerin her hakkı saklıdır. İzinsiz kullanılamaz. Bu sitede yer alan herhangi bir unsuru diğer bir internet sitesinde ve/veya başka bir mecrada yazılı, sözlü ve/veya elektronik olarak ve bunlarla sınırlı olmamak üzere her türlü şekilde yayınlamak ve/veya Kariyer.net\'in haberi olmadan link vermek kesinlikle yasaktır.\n"
"\n"
"Ayrıca bu sayfaların tasarımında ve veritabanı oluşturulmasında kullanılan bilgi ve/veya yazılımın kopyalanması ve/veya kullanılması kesinlikle yasaktır.\n"
"\n"
"Sitede bulunan yazılım, görsel ve tasarımların her türlü hakkı Kariyer.net\'e aittir.\n"
"\n"
"Kullanım\n"
"\n"
"Bu site herkese açıktır. Yalnızca aşağıdaki hallerde, Kariyer.net sitenin kullanımını geçici ve/veya sürekli olarak engelleyebilir:\n"
"Yanlış, düzensiz, eksik ve/veya yanıltıcı bilgi ve/veya uygun olmayan fotoğraf içeren özgeçmişin siteye kaydedilmesi halinde,\n"
"Özgeçmiş dışı bilgilerin; özel ve/veya genel duyuruların, reklam amaçlı firma bilgilerinin ve/veya üyelik satış formasyonları gibi bilgilerin ilave edilmesi halinde,\n"
"Diğer bir şahıs ve/veya kurum tarafından ilan edilen her türlü bilgi, görsel ve/veya logonun silinmesi tahrif edilmesi ve/veya değiştirilmesi halinde,\n"
"Internet Sitesi Güvenlik Kuralları\n"
"\n"
"Belirtilen güvenlik kurallarına kısmen ve/veya tamamen uyulmaması halinde ya da kasıtlı veya kasıtsız olarak aşağıda belirtilenlerden herhangi birini yapan kişi, kişiler ve/veya kurum, kurumlar hakkında Kariyer.net\'in her türlü kanuni hakkı saklıdır.\n"
"Kullanıcıların diğer özgeçmiş bilgilerine girme çabaları ve/veya sitenin genel güvenliğini tehdit edecek her türlü doğrudan ve/veya dolaylı çalışmalar,\n"
"Sitede kullanılan yazılımların çalışmasını engelleyebilecek her türlü doğrudan ve/veya dolaylı faaliyetler,\n"
"Virüs vasıtası ile sitenin çalışmasına engel olma,\n"
"Sitenin genel kurallarına uygun olmayan her türlü elektronik postanın yollanması ve/veya sitenin kilitlenmesini sağlama amacıyla aynı anda oldukça fazla ticari ve/veya kişisel elektronik postanın yollanması gibi.\n"
"Kariyer.net\'in Sorumlulukları;\n"
"\n"
"Kariyer.net, site üzerinde yer alan firma ve aday bilgilerinin içeriğinden hiçbir şekilde sorumlu tutulamaz. Bu sitede yer alan bilgilerle ilgili her türlü risk kullanıcılara aittir. Site üzerinde önceden herhangi bir haber vermeye gerek duyulmadan, istediği değişiklikleri yapma hakkı bizzat Kariyer.net\'e aittir.\n"
"\n"
"Özgeçmişini sitede bulunduran kullanıcı; özgeçmişinde bulunan her türlü bilginin tek sorumlusudur.\n"
"\n"
"Kariyer.net bir işveren değildir; sitede yer alan özgeçmişler Kariyer.net\'in sorumluluğu altında yer almamaktadır. İşveren firma ile kendi vasıtasıyla ilişkiye geçen özgeçmiş sahibi, bütün sorumluluğu üzerine almış olur.\n"
"\n"
"Kariyer.net, sitenin yazılımının her türlü hatadan arınmış olduğunu ve sitede herhangi bir virüs yer alıp almadığı konusunda herhangi bir sorumluluk yüklenmemektedir. Eğer bu sitede yer alan herhangi bir yazılım sebebi ile kullandığınız yazılım ve/veya donanım unsurlarına herhangi bir zarar gelirse firmamız bu konuda hiçbir sorumluluk yüklenmez.\n"
"\n"
"Bu sitede bulunan internet bağlantıları (linkler) ile ilgili her türlü risk kullanıcıya aittir. Kariyer.net özgeçmişinize bağlı olan bütün bilgileri kendi pazarlama faaliyetleri ile ilgili olarak kullanma hakkına sahiptir.\n"
"\n"
"Kariyer.net\'i tercih ederek bize gösterdiğiniz ilgi ve güven için çok teşekkür ederiz."))
        self.label_6.setText(_translate("Form", "Uyelik Sozlesmesi"))
        self.radioButton.setText(_translate("Form", "Kadin"))
        self.radioButton_2.setText(_translate("Form", "Erkek"))
        self.lbl_ad.setText(_translate("Form", "Ad       :"))
        self.lbl_soyad.setText(_translate("Form", "Soyad :"))
        self.label_7.setText(_translate("Form", "Cınsıyet"))
        self.label.setText(_translate("Form", "Medeni Durum :"))
        self.label_2.setText(_translate("Form", "Mail"))
        self.label_3.setText(_translate("Form", "Mail (Tekrar)"))
        self.label_4.setText(_translate("Form", "Password"))
        self.label_5.setText(_translate("Form", "Password Tekrar"))
