import os

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    os.system("python -m pip install pyqt5")
    from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 333)
        MainWindow.setStyleSheet("font:roboto;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 511, 141))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 441, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 300, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.downloadAll)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 230, 381, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 260, 551, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def downloadAll(self):
        links=self.textEdit.toPlainText()
        links=str(links).split('\n')
        path=self.lineEdit.text()
        print(path)
        print(links)
        numberOflinks=float(len(links))
        linkPercentage=100.0/numberOflinks
        progressbarPercentage=0
        for link in links:
            os.system("wget "+link+ " -P "+path)
            progressbarPercentage+=linkPercentage
            self.progressBar.setProperty("value", progressbarPercentage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WGET"))
        self.label_2.setText(_translate("MainWindow", "Paste here all the links you want to download:"))
        self.pushButton.setText(_translate("MainWindow", "DOWNLOAD!"))
        self.lineEdit.setText(_translate("MainWindow", "."))
        self.label_3.setText(_translate("MainWindow", "Path to download:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
