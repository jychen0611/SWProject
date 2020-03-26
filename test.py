from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QFrame,QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from good2 import Ui_MainWindow


import sys
import random
number=0
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #設定標題和圖示
        self.setWindowTitle('防疫一把罩')
        self.setWindowIcon(QtGui.QIcon('D:\PYQT\德賽.jpg'))
        #隱藏標題和圖示
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #設定背景
       # image=QtGui.QPixmap()
       # image.load('D:\PYQT\美景.jpg')
       # image=image.scaled(self.width(),self.height())
        palette=QtGui.QPalette()
        palette.setBrush(self.backgroundRole(),QtGui.QColor(80,150,210))#RGB
        self.setPalette(palette)
        #設定字體


        #設定選項(離開)
        self.ui.retranslateUi(self)
        self.ui.actionClose.setShortcut('Esc')
        self.ui.actionClose.triggered.connect(app.exit)
        # 設定ComboBox
        choices = ['全球','Taiwan','USA','China','Japan']
        self.ui.comboBox.addItems(choices)
        self.ui.comboBox.currentIndexChanged.connect(self.display)
        self.display()
        # 設定QLCDNumber
        self.ui.lcdNumber.display(number)
        # 設定Qtable
        self.ui.font = QFont('標楷體', 20)
        self.ui.font.setBold(True)  # 设置字体加粗

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(100)
        self.ui.tableWidget.setHorizontalHeaderLabels(['國家', '感染人數', '死亡人數'])  # 设置表头文字
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("China"))
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem("Italy"))
        self.ui.tableWidget.setItem(2, 0, QTableWidgetItem("United States of America"))
        self.ui.tableWidget.setItem(3, 0, QTableWidgetItem("Spain"))
        self.ui.tableWidget.setItem(4, 0, QTableWidgetItem("Germany"))


        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("81,869"))
        self.ui.tableWidget.setItem(1, 1, QTableWidgetItem("69,176"))
        self.ui.tableWidget.setItem(2, 1, QTableWidgetItem("51,914"))
        self.ui.tableWidget.setItem(3, 1, QTableWidgetItem("39,673"))
        self.ui.tableWidget.setItem(4, 1, QTableWidgetItem("31,554"))

        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("81,869"))
        self.ui.tableWidget.setItem(1, 2, QTableWidgetItem("6,820"))
        self.ui.tableWidget.setItem(2, 2, QTableWidgetItem("673"))
        self.ui.tableWidget.setItem(3, 2, QTableWidgetItem("2,696"))
        self.ui.tableWidget.setItem(4, 2, QTableWidgetItem("149"))

        # 設定字大小
        self.ui.label.setFont(QtGui.QFont('標楷體',30))
        self.ui.label_2.setFont(QtGui.QFont('標楷體', 10))
        self.ui.label_3.setFont(QtGui.QFont('標楷體', 25))
        self.ui.pushButton_2.setFont(QtGui.QFont('標楷體', 30))
        self.ui.pushButton.setFont(QtGui.QFont('標楷體', 25))

        pixmap = QPixmap("D:\PYQT\德賽.jpg")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        self.ui.label.setPixmap(pixmap)
        self.ui.label_2.setText('請選擇想查詢的位置')
        self.ui.label_3.setText('COVID-19 Situation Table')
        self.ui.pushButton_2.setText('回首頁')
        self.ui.pushButton.setText("清空")
        self.ui.pushButton_3.setText('NULL')


        self.ui.pushButton.clicked.connect(self.buttonClicked)






    def buttonClicked(self):

        self.ui.label.setText('示意圖')
        number =0
        self.ui.lcdNumber.display(number)
        self.ui.label_3.setText('COVID-19 Situation Table')

    def display(self):
        self.ui.label_3.setText('%s目前病例數為:'%self.ui.comboBox.currentText())
        pixmap = QPixmap("D:\PYQT\德賽.jpg")  # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        self.ui.label.setPixmap(pixmap)
        if self.ui.comboBox.currentText()=='Taiwan':
            number=195
        elif self.ui.comboBox.currentText()=='China':
            number=81116
        elif self.ui.comboBox.currentText()=='Japan':
            number=1111
        elif self.ui.comboBox.currentText()=='USA':
            number=35226
        else:
            number=99999
        self.ui.lcdNumber.display(number)



if __name__ == "__main__":
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())