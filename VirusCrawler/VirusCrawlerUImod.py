from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
import bs4
import time
from selenium import webdriver
from urllib.request import urlopen
from VirusCrawlerUI import Ui_Flight
from VirusCrawlerCode import crawler
import json

class Flight(QtWidgets.QMainWindow):
    def __init__(self):
        super(Flight, self).__init__()
#        self.driver = webdriver.Chrome(executable_path='C:\Code\VirusCrawler\venv\Lib\site-packages\selenium\webdriver\remote\chromedriver.exe')
        json_file = open("C:\Code\VirusCrawler\jsonfiles\TestData", "r", encoding='utf-8')
        self.FData = json.load(json_file)
        print(self.FData["Flight1"][0])
        json_file.close()
        self.ui = Ui_Flight()
        self.ui.setupUi(self)
        self.ui.flighttable.hide()
        self.ui.retranslateUi(Fl)
        _translate = QtCore.QCoreApplication.translate
        for i in range(100):
            for j in range(8):
                self.ui.item = QtWidgets.QTableWidgetItem()
                self.ui.flighttable.setItem(i, j, self.ui.item)
        for i in range(3):
            for j in range(8):
                self.ui.item = self.ui.flighttable.item(i, j)
                self.ui.item.setText(_translate("Flight", self.FData["Flight"+str(i)][j]))

        self.ui.flighttable.itemActivated.connect(itemActivated_event)
 #       self.ui.search.clicked.connect(self.handleButton)   #search button ( not completed

def itemActivated_event(item):
    json_file = open("C:\Code\VirusCrawler\jsonfiles\FlightUrl","r",encoding='utf-8')
    Flight.FData = json.load(json_file)
#    print(Flight.FData["中華航空"])
    json_file.close()
    if item.text() == '亞州航空' or item.text() == '中華航空' or item.text() == '馬來西亞':
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(Flight.FData[item.text()]))
    else:
        print(item.text())

#    def handleButton(self):     # search function (not completed
#        items = self.ui.flighttable.findItems(self.ui.edit.text(), QtCore.Qt.MatchExactly)
#        if items:
#            results = '\n'.join(
#                'row %d column %d' % (item.row() + 1, item.column() + 1)
#                for item in items)
#        else:
#            results = 'Found Nothing'
#        QtGui.QMessageBox.information(self, 'Search Results', results)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fl = QtWidgets.QWidget()
#    ui = Ui_Flight()     #original
    Fl = Flight()
#    Fl.ui.setupUi(Fl)
    Fl.show()
    sys.exit(app.exec_())
