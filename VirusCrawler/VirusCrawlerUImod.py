from PyQt5 import QtCore, QtGui, QtWidgets
from VirusCrawlerUI import Ui_Flight
#from VirusCrawlerCode import crawler
import json


class Flight(QtWidgets.QMainWindow):
    def __init__(self):
        super(Flight, self).__init__()
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
#        self.ui.item = self.ui.flighttable.item(0, 1)
#        self.ui.item.setText(_translate("Flight", self.FData["Flight1"][1]))
#        self.ui.item = self.ui.flighttable.item(0, 2)
#        self.ui.item.setText(_translate("Flight", self.FData["Flight1"][2]))
#        self.ui.item = self.ui.flighttable.item(1, 0)
#        self.ui.item.setText(_translate("Flight", self.FData["Flight2"][0]))
#        self.ui.item = self.ui.flighttable.item(1, 1)
#        self.ui.item.setText(_translate("Flight", self.FData["Flight2"][1]))
#        self.ui.item = self.ui.flighttable.item(1, 2)
#        self.ui.item.setText(_translate("Flight", self.FData["Flight2"][2]))
#        self.ui.flighttable.itemActivated.connect(Flight.itemActivated_event)

#       item = self.flighttable.item(1, 3)
#       item.setText(_translate("Flight", "Canceled"))
#       item = self.flighttable.item(0, 0)
#       item.setText(_translate("Flight", "AS164"))
#       item = self.flighttable.item(0, 1)
#       item.setText(_translate("Flight", "AirAsia"))
#       item = self.flighttable.item(0, 2)
#       item.setText(_translate("Flight", "14:00"))
#       item = self.flighttable.item(0, 3)
#       item.setText(_translate("Flight", "Late"))
    def itemActivated_event(item):
        json_file = open("C:\Code\VirusCrawler\jsonfiles\FlightUrl","r")
        Flight.FData = json.load(json_file)
#       print(Flight.FData["Flight0"][0])
        json_file.close()
        if (item.text() == 'China Airline' or item.text() == 'Scoot' or item.text() == 'Air Asia'):
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(Flight.FData[item.text()]))
        else:
            print(item.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fl = QtWidgets.QWidget()
#    ui = Ui_Flight()     #original
    Fl = Flight()
#    Fl.ui.setupUi(Fl)
    Fl.show()
    sys.exit(app.exec_())
