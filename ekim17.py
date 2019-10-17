from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("kayit_deneme.ui",self)
        # self.show()

uygulama=QApplication([])
pencere=Pencere()
pencere.show()
uygulama.exec()