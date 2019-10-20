from PyQt5.QtWidgets import *
from odev2 import Ui_MainWindow


class first_GUI(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
uygulama = QApplication([])
pencere = first_GUI()
pencere.setWindowTitle("CREATE A NEW ACCOUNT")
pencere.resize(400, 300)
pencere.show()
uygulama.exec_()