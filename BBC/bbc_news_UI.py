# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbc_news_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json, pathlib

##### My Code #####
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

        if len(title) > 12:
            title = title[:12] + "..."
        self.title = self.createMyLabel(title)
        self.title.mousePressEvent = self.Clicked_Label

        # let picture fit label size
        self.picture.setScaledContents(True)

        # set Picture
        if self.picture_link not in Ui_MainWindow.webImageDict:
            Ui_MainWindow.webImageDict[self.picture_link] = QtGui.QPixmap(QtGui.QImage(Ui_MainWindow.curPath + self.picture_link[1:]).smoothScaled(300,225))
        self.picture.setPixmap(Ui_MainWindow.webImageDict[self.picture_link])

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
    webImageDict = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_mainTable = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_mainTable.setGeometry(QtCore.QRect(0, 150, 1200, 750))
        self.scrollArea_mainTable.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea_mainTable.setObjectName("scrollArea_mainTable")
        self.scrollArea_mainTable.setWidget(self.scrollAreaWidgetContents)
        self.label_bbc_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_bbc_logo.setGeometry(QtCore.QRect(0, 0, 600, 75))
        self.label_bbc_logo.setObjectName("label_bbc_logo")
        self.label_bbc_red_bar = QtWidgets.QLabel(self.centralwidget)
        self.label_bbc_red_bar.setGeometry(QtCore.QRect(0, 75, 1200, 75))
        self.label_bbc_red_bar.setObjectName("label_bbc_red_bar")
        self.pushButton_go_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_go_back.setGeometry(QtCore.QRect(900, 25, 300, 50))
        self.pushButton_go_back.setObjectName("pushButton_go_back")
        MainWindow.setCentralWidget(self.centralwidget)

        ##### My Code #####
        MainWindow.setStyleSheet("QMainWindow {background: 'white';}") # set background color of window to white
        self.curPath = str(pathlib.Path(__file__).parent.absolute())
        self.label_bbc_logo.setPixmap(QtGui.QPixmap(self.curPath+'/src/BBC.png'))  # set while BBC logo
        self.label_bbc_logo.mousePressEvent = self.Clicked_label_bbc_logo
        self.label_bbc_red_bar.setPixmap(QtGui.QPixmap(self.curPath+'/src/NEWS_Chinese.png'))   # set while BBC logo
        self.label_bbc_red_bar.mousePressEvent = self.Clicked_label_bbc_red_bar
        ####################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ##### My Code #####
    def UpdateNews(self, returnData):
        # clear all object in news table
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().deleteLater()

        i=0
        for key, values in returnData.items():
            title = key
            picture_link = values[0]
            news_url = values[1]
            self.gridLayout.addWidget(MyGroupBox(title, picture_link, news_url), i//3, i%3)
            print("News ", i, "created!")
            i += 1

    def PreLoad(self):
        with open(self.curPath+'/src/data.json', 'r') as f:
            returnData = json.load(f)

        ### for example
        example = {}
        example['肺炎疫情：中國造新冠病毒測試盒為何在歐洲遭遇質量質疑'] = ["./picture/_111481192_whatsubject.jpg",
                                                 "https://www.bbc.com/zhongwen/trad/world-52102670"]
        example['習近平到訪浙江力推復工 全球需求仍陷停滯'] = ['./picture/_111481964_3.xinhua.jpg',
                                           'https://www.bbc.com/zhongwen/trad/chinese-news-52103506']
        example['肺炎疫情：為什麼印度全國封鎖後數百萬人走路回家'] = ['./picture/_111467867_gettyimages-1208531019.jpg',
                                              'https://www.bbc.com/zhongwen/trad/world-52103978']
        example['肺炎疫情：這場危機映照出的美國和美國總統'] = ['./picture/_111411989_mask_nyc_976getty.jpg',
                                           'https://www.bbc.com/zhongwen/trad/world-52082393']
        returnData = example
        ###

        for key, values in returnData.items():
            Ui_MainWindow.webImageDict[values[0]] = QtGui.QPixmap(QtGui.QImage(self.curPath + values[0][1:]).smoothScaled(400, 300))

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
    # print(ui.webImageDict)
    example = {}
    example['肺炎疫情：中國造新冠病毒測試盒為何在歐洲遭遇質量質疑'] = ["./picture/_111481192_whatsubject.jpg", "https://www.bbc.com/zhongwen/trad/world-52102670"]
    example['習近平到訪浙江力推復工 全球需求仍陷停滯'] = ['./picture/_111481964_3.xinhua.jpg','https://www.bbc.com/zhongwen/trad/chinese-news-52103506']
    example['肺炎疫情：為什麼印度全國封鎖後數百萬人走路回家'] = ['./picture/_111467867_gettyimages-1208531019.jpg','https://www.bbc.com/zhongwen/trad/world-52103978']
    example['肺炎疫情：這場危機映照出的美國和美國總統'] = ['./picture/_111411989_mask_nyc_976getty.jpg','https://www.bbc.com/zhongwen/trad/world-52082393']


    ui.UpdateNews(example)
    MainWindow.show()
    sys.exit(app.exec_())
