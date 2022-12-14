# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './views/buyTIcketWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_buyTicketWindow(object):
    def setupUi(self, buyTicketWindow):
        buyTicketWindow.setObjectName("buyTicketWindow")
        buyTicketWindow.resize(450, 560)
        buyTicketWindow.setStyleSheet("font-size: 20px;")
        self.centralwidget = QtWidgets.QWidget(buyTicketWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font-size: 36px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameTxt = QtWidgets.QLineEdit(self.frame_5)
        self.nameTxt.setStyleSheet("")
        self.nameTxt.setObjectName("nameTxt")
        self.horizontalLayout_2.addWidget(self.nameTxt)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bookFlightBtn = QtWidgets.QPushButton(self.frame_4)
        self.bookFlightBtn.setStyleSheet("background-color: rgb(48, 124, 124);\n"
"color: #ffffff;")
        self.bookFlightBtn.setObjectName("bookFlightBtn")
        self.horizontalLayout_4.addWidget(self.bookFlightBtn)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.finishBuyBtn = QtWidgets.QPushButton(self.frame_6)
        self.finishBuyBtn.setStyleSheet("background-color: rgb(16, 60, 60);\n"
"color: #ffffff;")
        self.finishBuyBtn.setObjectName("finishBuyBtn")
        self.horizontalLayout_5.addWidget(self.finishBuyBtn)
        self.verticalLayout.addWidget(self.frame_6)
        buyTicketWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(buyTicketWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 34))
        self.menubar.setObjectName("menubar")
        buyTicketWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(buyTicketWindow)
        self.statusbar.setObjectName("statusbar")
        buyTicketWindow.setStatusBar(self.statusbar)

        self.retranslateUi(buyTicketWindow)
        QtCore.QMetaObject.connectSlotsByName(buyTicketWindow)

    def retranslateUi(self, buyTicketWindow):
        _translate = QtCore.QCoreApplication.translate
        buyTicketWindow.setWindowTitle(_translate("buyTicketWindow", "MainWindow"))
        self.label.setText(_translate("buyTicketWindow", "Buy Tickets"))
        self.label_2.setText(_translate("buyTicketWindow", "Name"))
        self.label_3.setText(_translate("buyTicketWindow", "To proceed it is necessary to\n"
"scan your face"))
        self.bookFlightBtn.setText(_translate("buyTicketWindow", "Register Face"))
        self.finishBuyBtn.setText(_translate("buyTicketWindow", "Finish Buying"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    buyTicketWindow = QtWidgets.QMainWindow()
    ui = Ui_buyTicketWindow()
    ui.setupUi(buyTicketWindow)
    buyTicketWindow.show()
    sys.exit(app.exec_())
