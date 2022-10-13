"""
Voice Password Authenticator. (with low-level authentication).
A GUI that incorporates speech recognition in its authentication process.
"""
import os
import sys
import time
from PyQt5 import QtCore
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import speech_recognition as sr
from validate_email import validate_email

password_list = []

credentials = [] # A List to hold credentials from the signup page. To be used after recording the password.
r = sr.Recognizer()

class signupWindow(QWidget):
    """
    A Class representing the Signup Window.
    
    Methods
    -------
    create_auth(): 
        Appends the email, firsname, surname and username to the credentials list.
        
    open_recording():
        Displays the recording .
        
    login():
        Displays the login page.
    """
    def __init__(self, parent=None):
        """
        Constructs all the necessary attributes for the signupWindow object.
        """
        super(signupWindow, self).__init__()
        loadUi("Signup_widget.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)          #Creates a frameless Window
        self.nextButton.clicked.connect(self.create_auth)           #Creates an event(create_auth()) when clicked(nextButton)
        self.loginButton.clicked.connect(self.login)                #Creates an event(login()) when clicked(loginButton)

    def create_auth(self):
        """
        Appends (Writes) the variables specified to the credentials list.
        
        Variables
        ---------
        
        email:
            represents the string given by the user as the email in the GUI
            
        first_name:
            represents the string given by the user as the First Name in the GUI
            
        surname:
            represents the string given by the user as the Surname in the GUI
            
        username:
            represents the string given by the user as the username in the GUI
            
        """
        email = self.email.text()
        first_name = self.firstname.text()
        surname = self.surname.text()
        username = self.username.text()
        credentials.append(email)
        credentials.append(first_name)
        credentials.append(surname)
        credentials.append(username)

        msg = QMessageBox()
        if validate_email(email) is True:
            self.open_recording()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Invalid Email!')
            msg.exec_()

    def open_recording(self):
        """
        Opens the Recording window.
        """
        widget.setCurrentIndex(widget.currentIndex()+2)

    def login(self):
        """
        Opens the login window.
        """
        try:
            widget.setCurrentIndex(widget.currentIndex()+1)
        except Exception as e :
            print(e)
            
class recordingWindow(QDialog):
    """
    A Class representing the recording window.
    
    Methods
    -------
    listen():
        Gets user input from the devices' main audio source.
        
    stop_listening():
        Matches the user input against certain parameters and writes the input gotten from the 'listen()' method to a file.
        
    continue_auth():
        Writes the credentials to a file.

    open_success():
        Displays the Success Window.

        """
    def __init__(self, parent=None):
        super(recordingWindow, self).__init__()
        loadUi("Recording.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.startRecordingButton.clicked.connect(self.listen)
        self.stopRecordingButton.clicked.connect(self.stop_listening)
        self.setWindowTitle(" Password Recording ")

    def listen(self):
        with sr.Microphone() as source:
            try:
                self.listening_label.setText("Please Wait")
                print(1)
                r.adjust_for_ambient_noise(source, duration=1)
                print(2)
                self.listening_label.setText("Listening")
                print(3)
                audio = r.listen(source)
                print(4)
                global text
                print(5)
                text = r.recognize_google(audio)
                print(6)
                password_list.append(str(text))
                print(text)
                
            except Exception as e:
                print(str(Exception), e)
                self.listening_label.setFont(QFont('Cambria', 7))
                self.listening_label.setText("We're having trouble connecting to the internet 🌐")
                

    def stop_listening(self):
        try:
            if len(password_list[0]) <= 7:
                self.listening_label.setText("Your password was not up to 8 letters, please try again!")
                time.sleep(1)
                self.listening_label.setText("")
                widget.setCurrentIndex(widget.currentIndex())
            else:
                text = password_list[0]
                self.password.setText(text)
                credentials.append(text)
                print(1)
                self.continue_auth()
                print(4)
        except NameError:
            print("Dead")
            self.listening_label.setFont(QFont('Cambria', 10))
            self.listening_label.setText("I didn't get that 💔. Please try again!")
            time.sleep(2)

    def continue_auth(self):
        print('Doing------------------------------------------------------------')
        email = credentials[0]
        password = credentials[-1]
        username = credentials[3]
        msg = QMessageBox()
        try:
            msg.setIcon(QMessageBox.Information)
            msg.setText('Loading... Please Wait')
            msg.exec_()
            f = open("C:/Users/Public/221101.txt", "w")
            if f != " ":
                details = ";" + email +":"+ username + ":" + password
                f.write(details)
                self.open_success()
            else:
                f.write(email+ ":" +username+ ":" + password)
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Successfully created!! Exit!')
                msg.exec_()
                f.close()
                print('Closed')
                self.open_success()
        except Exception:
            self.listening_label.setText("An Error Occured. Please try again! ")

    def open_success(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class loginPage(QDialog):
    """
    A Class representing the login window.
    
    Methods
    -------
    verify_password():
        Matches the user's input against the password in the file.

    open_success():
        Displays the success window.
        
    """
    def __init__(self, parent=None):
        super(loginPage, self).__init__()
        loadUi("Login.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle(" Login ")
        self.nextButton.clicked.connect(self.verify_password)
        # if self.rememberMe.isChecked() == True:
        #     self.never_login()

    # def never_login(self):
    #     with open('C:/Users/Public/bootstrap.txt', 'w') as f:
    #         f.write('True')
    #         f.close()

    def verify_password(self):
        """
        Matches the users input against the password in the file, opens the success window if successful, displays an error message if not.
        """
        email = self.email.text()
        username = self.username.text()
        password = self.password.text()
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        txt = Path('C:/Users/Public/221101.txt').read_text()
        num = ";"
        if num in txt:
            txt = txt.split(num)
            details = email +":"+username+":"+password
            if details in txt:
                self.open_success()
            else:
                msg = QMessageBox()   
                msg.setText("Invalid Login Credentials")
                msg.exec_()
        else:
            num = ":"
            text=txt.split(num)
            if text[0] == email and text[1] == username and text[2] == password:
                self.open_success()
            else:
                msg = QMessageBox()
                msg.setText("Invalid Login Credentials")
                msg.exec_()

    def open_success(self):
        """
        Opens the success Window.
        """
        widget.setCurrentIndex(widget.currentIndex()+2)
        
class success(QDialog):
    def __init__(self, parent=None):
        super(success, self).__init__()
        loadUi("Success.ui", self)
        self.setWindowTitle(" Success ")

app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
signup_window = signupWindow()
signup_window.setWindowTitle('Signup')
login_page = loginPage()
login_page.setWindowTitle('Login')
recording = recordingWindow()
successes = success()
successes.setWindowTitle('Success')

widget.addWidget(signup_window)
widget.addWidget(login_page)
widget.addWidget(recording)
widget.addWidget(successes)
widget.setFixedHeight(400)
widget.setFixedWidth(500)
widget.show()
sys.exit(app.exec())