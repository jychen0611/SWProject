from PyQt5 import QtCore, QtGui, QtWidgets
from bbc_news_UI import Ui_MainWindow
from BBC_WebCrawer import CoronavirusTopic
import json, sys

class BBCWindow(QtWidgets.QMainWindow):
    goBackToStartupSignal = QtCore.pyqtSignal()

    def __init__(self, parent= None):
        super(BBCWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_go_back.clicked.connect(self.goBackToStartup)
        self.ui.PreLoad()

    def goBackToStartup(self):
        self.goBackToStartupSignal.emit()
        self.hide()

    def update(self):
        CoronavirusTopic() # generate new data.json in src and download new picture to picture folder
        self.ui.UpdateNews(self.getData())

    def getData(self):
        with open(self.ui.curPath + '/src/data.json', 'r') as f:
            return json.load(f)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    bbc = BBCWindow()
    bbc.update()
    bbc.show()
    sys.exit(app.exec_())