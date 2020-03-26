from PyQt5 import QtCore, QtGui, QtWidgets
from .bbc_news_UI import Ui_MainWindow

class BBCWindow(QtWidgets.QMainWindow):
    goBackToStartupSignal = QtCore.pyqtSignal()

    def __init__(self, parent= None):
        super(BBCWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_go_back.clicked.connect(self.goBackToStartup)

    def goBackToStartup(self):
        self.goBackToStartupSignal.emit()
        self.hide()

    def update(self):
        self.ui.UpdateNews()