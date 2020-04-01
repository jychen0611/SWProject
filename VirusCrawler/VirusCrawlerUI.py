# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VirusCrawlerUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Flight(object):
    def setupUi(self, Flight):
        Flight.setObjectName("Flight")
        Flight.resize(1200, 900)
        self.background = QtWidgets.QLabel(Flight)
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("pic/abstract-blue-geometric-shapes-background_1035-17545.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.flightinfo = QtWidgets.QPushButton(Flight)
        self.flightinfo.setGeometry(QtCore.QRect(490, 460, 93, 28))
        self.flightinfo.setObjectName("flightinfo")
        self.main = QtWidgets.QPushButton(Flight)
        self.main.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.main.setObjectName("main")
        self.flighttable = QtWidgets.QTableWidget(Flight)
        self.flighttable.setGeometry(QtCore.QRect(0, 100, 1200, 900))
        self.flighttable.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.flighttable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.flighttable.setRowCount(100)
        self.flighttable.setColumnCount(8)
        self.flighttable.setObjectName("flighttable")
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.flighttable.setHorizontalHeaderItem(7, item)
        self.flighttable.horizontalHeader().setDefaultSectionSize(140)

        self.retranslateUi(Flight)
        self.main.clicked.connect(self.flighttable.hide)
        self.flightinfo.clicked.connect(self.flighttable.show)
        QtCore.QMetaObject.connectSlotsByName(Flight)

    def retranslateUi(self, Flight):
        _translate = QtCore.QCoreApplication.translate
        Flight.setWindowTitle(_translate("Flight", "Form"))
        self.flightinfo.setText(_translate("Flight", "flightinfo"))
        self.main.setText(_translate("Flight", "main"))
        item = self.flighttable.horizontalHeaderItem(0)
        item.setText(_translate("Flight", "出入境"))
        item = self.flighttable.horizontalHeaderItem(1)
        item.setText(_translate("Flight", "表定時間"))
        item = self.flighttable.horizontalHeaderItem(2)
        item.setText(_translate("Flight", "航空公司"))
        item = self.flighttable.horizontalHeaderItem(3)
        item.setText(_translate("Flight", "班機編號"))
        item = self.flighttable.horizontalHeaderItem(4)
        item.setText(_translate("Flight", "往來城市"))
        item = self.flighttable.horizontalHeaderItem(5)
        item.setText(_translate("Flight", "航廈"))
        item = self.flighttable.horizontalHeaderItem(6)
        item.setText(_translate("Flight", "狀態"))
        item = self.flighttable.horizontalHeaderItem(7)
        item.setText(_translate("Flight", "預計時間"))
