# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Victor\PyQt_Apps\Image Converter\PyQt-Apps\Voice_Password_App\Success.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 408)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 120, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(49)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("COLOR: RGB(0,0,26);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 250, 271, 71))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SUCCESS👍😁"))
        self.label_2.setText(_translate("Form", "Contact: +2349032751819                              E-mail: victorumoreng@gmail.com                  Website: www.kodehauz.com"))
