from PyQt5 import QtCore, QtGui, QtWidgets
from BBC.bbc_news_UI import Ui_MainWindow
from BBC.BBC_WebCrawer import CoronavirusTopic
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
        # CoronavirusTopic() # generate new data.json in src and download new picture to picture folder
        # self.ui.UpdateNews(self.getData())

        ### example
        example = {}
        example['肺炎疫情：中國造新冠病毒測試盒為何在歐洲遭遇質量質疑'] = ["./picture/_111481192_whatsubject.jpg",
                                                 "https://www.bbc.com/zhongwen/trad/world-52102670"]
        example['習近平到訪浙江力推復工 全球需求仍陷停滯'] = ['./picture/_111481964_3.xinhua.jpg',
                                           'https://www.bbc.com/zhongwen/trad/chinese-news-52103506']
        example['肺炎疫情：為什麼印度全國封鎖後數百萬人走路回家'] = ['./picture/_111467867_gettyimages-1208531019.jpg',
                                              'https://www.bbc.com/zhongwen/trad/world-52103978']
        example['肺炎疫情：這場危機映照出的美國和美國總統'] = ['./picture/_111411989_mask_nyc_976getty.jpg',
                                           'https://www.bbc.com/zhongwen/trad/world-52082393']
        self.ui.UpdateNews(example)
        ###
        pass

    def getData(self):
        with open(self.ui.curPath + '/src/data.json', 'r') as f:
            return json.load(f)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    bbc = BBCWindow()
    bbc.update()
    bbc.show()
    sys.exit(app.exec_())