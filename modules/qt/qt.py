 #Qt module

import re
import os
import sys
import zmq
import time
import threading
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    root = "/opt/braintux-master"
elif sys.platform == "nt":
    root = r"%ProgramFiles%/braintux-master"

modules = ["qt", "terminal", "whatsapp"]

executing = True
port = 8652
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:{}".format(port))

def main():
    a = time.time()
    while executing:
        statusUpdate()
        a = time.time()
        #  Wait for next request from client
        message = socket.recv_json()[0]
        if message == "ping":
            socket.send_json(["pong"])
        elif message == "stop":
            socket.send_json(["stopped"])
            os._exit(0)
        else:
            ui.output_label.setText(message)
            socket.send_json(["sent"])

class Ui_Braintux(object):
    def setupUi(self, Braintux):
        Braintux.setObjectName("Braintux")
        Braintux.resize(512, 473)
        Braintux.setStyleSheet("background-color: rgb(173, 127, 168)")
        self.centralwidget = QtWidgets.QWidget(Braintux)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(170, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(243, 191, 255)")
        self.title.setObjectName("title")
        self.subtitle = QtWidgets.QLabel(self.centralwidget)
        self.subtitle.setGeometry(QtCore.QRect(100, 50, 311, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.subtitle.setFont(font)
        self.subtitle.setStyleSheet("color: rgb(243, 191, 255)")
        self.subtitle.setObjectName("subtitle")
        self.terminal_label = QtWidgets.QLabel(self.centralwidget)
        self.terminal_label.setGeometry(QtCore.QRect(100, 160, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.terminal_label.setFont(font)
        self.terminal_label.setStyleSheet("color: rgb(243, 191, 255)")
        self.terminal_label.setObjectName("terminal_label")
        self.whatsapp_label = QtWidgets.QLabel(self.centralwidget)
        self.whatsapp_label.setGeometry(QtCore.QRect(100, 190, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.whatsapp_label.setFont(font)
        self.whatsapp_label.setStyleSheet("color: rgb(243, 191, 255)")
        self.whatsapp_label.setObjectName("whatsapp_label")
        self.terminal_start_button = QtWidgets.QPushButton(self.centralwidget)
        self.terminal_start_button.setGeometry(QtCore.QRect(170, 160, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.terminal_start_button.setFont(font)
        self.terminal_start_button.setStyleSheet("color: rgb(92, 53, 102)")
        self.terminal_start_button.setObjectName("terminal_start_button")
        self.terminal_stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.terminal_stop_button.setGeometry(QtCore.QRect(270, 160, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.terminal_stop_button.setFont(font)
        self.terminal_stop_button.setStyleSheet("color: rgb(92, 53, 102)")
        self.terminal_stop_button.setObjectName("terminal_stop_button")
        self.whatsapp_stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.whatsapp_stop_button.setGeometry(QtCore.QRect(270, 190, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.whatsapp_stop_button.setFont(font)
        self.whatsapp_stop_button.setStyleSheet("color: rgb(92, 53, 102)")
        self.whatsapp_stop_button.setObjectName("whatsapp_stop_button")
        self.whatsapp_start_button = QtWidgets.QPushButton(self.centralwidget)
        self.whatsapp_start_button.setGeometry(QtCore.QRect(170, 190, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.whatsapp_start_button.setFont(font)
        self.whatsapp_start_button.setStyleSheet("color: rgb(92, 53, 102)")
        self.whatsapp_start_button.setObjectName("whatsapp_start_button")
        self.qt_stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.qt_stop_button.setGeometry(QtCore.QRect(270, 130, 89, 25))
        font = QtGui.QFont()
        self.qt_stop_button.setFont(font)
        self.qt_stop_button.setStyleSheet("color: rgb(92, 53, 102)")
        self.qt_stop_button.setObjectName("qt_stop_button")
        self.qt_start_button = QtWidgets.QPushButton(self.centralwidget)
        self.qt_start_button.setGeometry(QtCore.QRect(170, 130, 89, 25))
        font = QtGui.QFont()
        self.qt_start_button.setFont(font)
        self.qt_start_button.setStyleSheet("color: rgb(92, 53, 102)")
        self.qt_start_button.setObjectName("qt_start_button")
        self.output_title = QtWidgets.QFrame(self.centralwidget)
        self.output_title.setGeometry(QtCore.QRect(10, 70, 491, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.output_title.setFont(font)
        self.output_title.setFrameShape(QtWidgets.QFrame.HLine)
        self.output_title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_title.setObjectName("output_title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 100, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(243, 191, 255)")
        self.label.setObjectName("label")
        self.terminal_status_label = QtWidgets.QLabel(self.centralwidget)
        self.terminal_status_label.setGeometry(QtCore.QRect(370, 160, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.terminal_status_label.setFont(font)
        self.terminal_status_label.setStyleSheet("color: rgb(243, 191, 255)")
        self.terminal_status_label.setObjectName("terminal_status_label")
        self.whatsapp_status_label = QtWidgets.QLabel(self.centralwidget)
        self.whatsapp_status_label.setGeometry(QtCore.QRect(370, 190, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.whatsapp_status_label.setFont(font)
        self.whatsapp_status_label.setStyleSheet("color: rgb(243, 191, 255)")
        self.whatsapp_status_label.setObjectName("whatsapp_status_label")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(70, 250, 351, 171))
        self.output_label.setAutoFillBackground(False)
        self.output_label.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(238, 238, 236)")
        self.output_label.setText("")
        self.output_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output_label.setWordWrap(True)
        self.output_label.setObjectName("output_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(243, 191, 255)")
        self.label_2.setObjectName("label_2")
        self.qt_status_label = QtWidgets.QLabel(self.centralwidget)
        self.qt_status_label.setGeometry(QtCore.QRect(370, 130, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.qt_status_label.setFont(font)
        self.qt_status_label.setStyleSheet("color: rgb(243, 191, 255)")
        self.qt_status_label.setObjectName("qt_status_label")
        self.qt_label = QtWidgets.QLabel(self.centralwidget)
        self.qt_label.setGeometry(QtCore.QRect(140, 130, 16, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.qt_label.setFont(font)
        self.qt_label.setStyleSheet("color: rgb(243, 191, 255)")
        self.qt_label.setObjectName("qt_label")
        Braintux.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Braintux)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 22))
        self.menubar.setObjectName("menubar")
        Braintux.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Braintux)
        self.statusbar.setObjectName("statusbar")
        Braintux.setStatusBar(self.statusbar)

        self.retranslateUi(Braintux)
        QtCore.QMetaObject.connectSlotsByName(Braintux)

    def retranslateUi(self, Braintux):
        _translate = QtCore.QCoreApplication.translate
        Braintux.setWindowTitle(_translate("Braintux", "Braintux"))
        self.title.setText(_translate("Braintux", "Braintux"))
        self.subtitle.setText(_translate("Braintux", "Braintux is made by modules, so use them."))
        self.terminal_label.setText(_translate("Braintux", "Terminal"))
        self.whatsapp_label.setText(_translate("Braintux", "Whatsapp"))
        self.terminal_start_button.setText(_translate("Braintux", "start"))
        self.terminal_stop_button.setText(_translate("Braintux", "stop"))
        self.whatsapp_stop_button.setText(_translate("Braintux", "stop"))
        self.whatsapp_start_button.setText(_translate("Braintux", "start"))
        self.qt_stop_button.setText(_translate("Braintux", "stop"))
        self.qt_start_button.setText(_translate("Braintux", "start"))
        self.label.setText(_translate("Braintux", "Status"))
        self.terminal_status_label.setText(_translate("Braintux", "Off"))
        self.whatsapp_status_label.setText(_translate("Braintux", "Off"))
        self.label_2.setText(_translate("Braintux", "Output"))
        self.qt_status_label.setText(_translate("Braintux", "Off"))
        self.qt_label.setText(_translate("Braintux", "Qt"))

def getFunction(command, module):

    def myfunc():
        subprocess.Popen("python3 {}/braintux-core.py {} {}".format(root, command, module), shell=True)
    
    return myfunc

def exitHandler():
    os._exit(0)

def statusUpdate():
    status = []

    for module in modules:
        p = subprocess.Popen("python3 {}/braintux-core.py ping {}".format(root, module), stdout=subprocess.PIPE, shell=True)
        output = p.communicate()[0].decode('utf-8')
        if output == "On\n":
            status.append("On")
        else:
            status.append("Off")

    ui.terminal_status_label.setText(status[1])
    ui.whatsapp_status_label.setText(status[2])

app = QtWidgets.QApplication([])
app.aboutToQuit.connect(exitHandler)
Braintux = QtWidgets.QMainWindow()
ui = Ui_Braintux()
ui.setupUi(Braintux)
ui.qt_start_button.clicked.connect(getFunction("start", "qt"))
ui.qt_stop_button.clicked.connect(getFunction("stop", "qt"))
ui.terminal_start_button.clicked.connect(getFunction("start", "terminal"))
ui.terminal_stop_button.clicked.connect(getFunction("stop", "terminal"))
ui.whatsapp_start_button.clicked.connect(getFunction("start", "whatsapp"))
ui.whatsapp_stop_button.clicked.connect(getFunction("stop", "whatsapp"))
ui.qt_status_label.setText("On")
statusUpdate()
Braintux.show()

threading.Thread(target=main).start()

app.exec_()