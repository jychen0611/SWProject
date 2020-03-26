# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbc_news_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


##### My Code #####
import urllib.request
import pathlib

class MyGroupBox(QtWidgets.QGroupBox):
    class MyLabel(QtWidgets.QLabel):
        def __init__(self, *args, **kwargs):
            QtWidgets.QLabel.__init__(self, *args, **kwargs)

        def enterEvent(self, event):
            self.setStyleSheet("QLabel {color: #1167ad};")

        def leaveEvent(self, event):
            self.setStyleSheet("QLabel {color: #000000};")

    def createMyLabel(self, title):
        return MyGroupBox.MyLabel(title)

    def __init__(self, title, picture_link, news_url, *args, **kwargs):
        QtWidgets.QGroupBox.__init__(self, *args, **kwargs)
        self.picture_link = picture_link
        self.news_url = news_url

        # define two label
        self.mousePressEvent = self.Clicked_Label
        self.picture = QtWidgets.QLabel()

        if len(title) > 16:
            title = title[:16] + "..."
        self.title = self.createMyLabel(title)
        self.title.mousePressEvent = self.Clicked_Label

        # let picture fit label size
        self.picture.setScaledContents(True)

        # set Picture
        image = None
        if self.picture_link not in Ui_MainWindow.webImage:
            data = urllib.request.urlopen(self.picture_link).read()
            image = QtGui.QImage()
            image.loadFromData(data)
            Ui_MainWindow.webImage[self.picture_link] = image
        else:
            image = Ui_MainWindow.webImage[self.picture_link]
        self.picture.setPixmap(QtGui.QPixmap(image.smoothScaled(400, 300)))  # set picture size to 400*300

        # set title style
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        # vertical grid
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.picture)
        vbox.addWidget(self.title)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def Clicked_Label(self, event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.news_url))
####################

class Ui_MainWindow(object):
    webImage = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1600, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_mainTable = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_mainTable.setGeometry(QtCore.QRect(0, 200, 1600, 1000))
        self.scrollArea_mainTable.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea_mainTable.setObjectName("scrollArea_mainTable")
        self.scrollArea_mainTable.setWidget(self.scrollAreaWidgetContents)
        self.label_bbc_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_bbc_logo.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.label_bbc_logo.setObjectName("label_bbc_logo")
        self.label_bbc_red_bar = QtWidgets.QLabel(self.centralwidget)
        self.label_bbc_red_bar.setGeometry(QtCore.QRect(0, 100, 1600, 100))
        self.label_bbc_red_bar.setObjectName("label_bbc_red_bar")
        self.pushButton_go_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go_back.setGeometry(QtCore.QRect(1200, 50, 400, 50))
        self.pushButton_go_back.setObjectName("pushButton_go_back")
        MainWindow.setCentralWidget(self.centralwidget)

        ##### My Code #####
        MainWindow.setStyleSheet("QMainWindow {background: 'white';}") # set background color of window to white
        self.curPath = str(pathlib.Path(__file__).parent.absolute())
        self.label_bbc_logo.setPixmap(QtGui.QPixmap(self.curPath+'/src/BBC.png'))  # set while BBC logo
        self.label_bbc_logo.mousePressEvent = self.Clicked_label_bbc_logo
        self.label_bbc_red_bar.setPixmap(QtGui.QPixmap(self.curPath+'/src/NEWS_Chinese.png'))   # set while BBC logo
        self.label_bbc_red_bar.mousePressEvent = self.Clicked_label_bbc_red_bar

        self.test = 0
        self.PreLoad()
        ####################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ##### My Code #####
    def UpdateNews(self):
        # clear all object in news table
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().deleteLater()

        returnData = self.WebCrawer()
        i=0
        for key, values in returnData.items():
            title = key
            picture_link = values[0]
            news_url = values[1]
            self.gridLayout.addWidget(MyGroupBox(title, picture_link, news_url), i//3, i%3)
            i += 1

    def PreLoad(self):
        returnData = self.WebCrawer()
        for key, values in returnData.items():
            data = urllib.request.urlopen(values[0]).read()
            image = QtGui.QImage()
            image.loadFromData(data)
            Ui_MainWindow.webImage[values[0]] = image

    def WebCrawer(self):
        # do something

        # key = title, value = [picture_link, news_url]
        example = {}
        if self.test % 2 == 1:
            example['肺炎疫情：分析中美背後的政治角力'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/DBE1/production/_111398265_673d94a6-cb9b-4a33-a2a6-67940b35aff4.jpg','https://www.bbc.com/zhongwen/trad/world-52016078']
            example['英國王儲查爾斯王子確診感染新冠病毒 「症狀輕微」'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/95E3/production/_111417383_5d7748e8-87bd-458a-baef-af40d207d905.jpg', 'https://www.bbc.com/zhongwen/trad/uk-52034402']
            example['肺炎疫情：無症狀感染者是否會導致第二次大爆發'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/0E99/production/_110873730_p0831myp.jpg','https://www.bbc.com/zhongwen/trad/chinese-news-52016649']
            example['肺炎疫情：印度13億人口「宵禁」21天，全球最大規模封國面臨的挑戰'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/F604/production/_111408926_gettyimages-1208075838.jpg', 'https://www.bbc.com/zhongwen/trad/world-52031681']
            example['肺炎疫情：特朗普冀復活節美國恢復正常'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/5989/production/_111412922_hi060717157.jpg', 'https://www.bbc.com/zhongwen/trad/world-52032689']
            example['肺炎疫情：特朗普從堅稱「中國病毒」到表態「不是美國亞裔的錯」'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/8D6D/production/_111050263_gettyimages-1205108047.jpg', 'https://www.bbc.com/zhongwen/trad/world-52027635']
            example['肺炎疫情：居家隔離如何鍛煉和保持最佳狀態'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/BF8D/production/_111373094_070cb94f-a4b7-424c-8477-99259708e66d.jpg', 'https://www.bbc.com/zhongwen/trad/world-51977605']
        else:
            example['肺炎疫情：分析中美背後的政治角力'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/DBE1/production/_111398265_673d94a6-cb9b-4a33-a2a6-67940b35aff4.jpg','https://www.bbc.com/zhongwen/trad/world-52016078']
            example['英國王儲查爾斯王子確診感染新冠病毒 「症狀輕微」'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/95E3/production/_111417383_5d7748e8-87bd-458a-baef-af40d207d905.jpg','https://www.bbc.com/zhongwen/trad/uk-52034402']
            example['肺炎疫情：無症狀感染者是否會導致第二次大爆發'] = ['https://ichef.bbci.co.uk/news/660/cpsprodpb/0E99/production/_110873730_p0831myp.jpg','https://www.bbc.com/zhongwen/trad/chinese-news-52016649']

        self.test += 1
        return example

    def Clicked_label_bbc_logo(self, event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://www.bbc.com/'))

    def Clicked_label_bbc_red_bar(self, event):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://www.bbc.com/zhongwen/trad'))

    ####################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BBC News"))
        self.pushButton_go_back.setText(_translate("MainWindow", "回首頁"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.UpdateNews()
    MainWindow.show()
    sys.exit(app.exec_())
