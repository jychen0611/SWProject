import bbc_news_mainwindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = bbc_news_mainwindow.Ui_MainWindow()
ui.setupUi(MainWindow)


MainWindow.show()
sys.exit(app.exec_())