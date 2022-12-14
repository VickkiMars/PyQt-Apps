# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Victor\PyQt_Apps\Image Converter\PyQt-Apps\Voice_Password_App\Signup_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 409)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.widget_2.setMinimumSize(QtCore.QSize(500, 400))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(23)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setGeometry(QtCore.QRect(50, 50, 391, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(110, 0, 20, 61))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.widget_2)
        self.line_6.setGeometry(QtCore.QRect(360, 0, 20, 61))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 60, 331, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.firstname.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid black;\n"
"color:black;\n"
"padding-bottom: 7px")
        self.firstname.setText("")
        self.firstname.setObjectName("firstname")
        self.verticalLayout.addWidget(self.firstname)
        self.surname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.surname.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid black;\n"
"color:black;\n"
"padding-bottom: 7px")
        self.surname.setText("")
        self.surname.setObjectName("surname")
        self.verticalLayout.addWidget(self.surname)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid black;\n"
"color:black;\n"
"padding-bottom: 7px")
        self.username.setText("")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid black;\n"
"color:black;\n"
"padding-bottom: 7px")
        self.email.setText("")
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.nextButton = QtWidgets.QPushButton(self.widget_2)
        self.nextButton.setGeometry(QtCore.QRect(140, 290, 191, 41))
        self.nextButton.setStyleSheet("QPushButton {border-radius: 14px;\n"
"color: white;\n"
"background-color: rgb(0, 0, 13);\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 0, 25); \n"
"color: rgb(0, 153, 255);\n"
"font-weight: bold;\n"
"}\n"
"")
        self.nextButton.setObjectName("nextButton")
        self.loginButton = QtWidgets.QPushButton(self.widget_2)
        self.loginButton.setGeometry(QtCore.QRect(140, 340, 201, 28))
        self.loginButton.setStyleSheet("QPushButton {\n"
"background-color:rgb(242, 242, 242);\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}\n"
"")
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Signup"))
        self.firstname.setPlaceholderText(_translate("Form", "First Name"))
        self.surname.setPlaceholderText(_translate("Form", "Surname"))
        self.username.setPlaceholderText(_translate("Form", "Username"))
        self.email.setPlaceholderText(_translate("Form", "Email"))
        self.nextButton.setText(_translate("Form", "Next ???"))
        self.loginButton.setText(_translate("Form", "Already have an account? Login"))
