"""
PyQt Native App to convert images using python's base64 module
"""
import os
import sys
import base64
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

image_format = []
file_list = []

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Converter.ui", self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.select_image.clicked.connect(self.select_file)
        global radio_1, radio_2, radio_3, radio_4, radio_5, radio_6


        self.radio_png.toggled.connect(lambda:self.btnstate(self.radio_png))


        self.radio_jpg.toggled.connect(lambda:self.btnstate(self.radio_jpg))

        self.radio_gif.toggled.connect(lambda:self.btnstate(self.radio_gif))

        self.radio_tiff.toggled.connect(lambda:self.btnstate(self.tiff))

        self.radio_pdf.toggled.connect(lambda:self.btnstate(self.pdf))

        self.radio_webp.toggled.connect(lambda:self.btnstate(self.webp))

        self.radio_bmp.toggled.connect(lambda:self.btnstate(self.bmp))
        
        self.convert.clicked.connect(self.process_file)

    def btnstate(self, b):
        if len(image_format) == 0:
            image_format.append(b.text())
        else:
            image_format[0] == b.text()
            
    def select_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 
            'c:\\',"Image files (*.jpg *.png)")
        x = file_name[0].split('/').pop(-1)


        
        fp1 = file_name[0] #File path with file name
        fp2 = file_name[0].replace(x, '') #File path without file name


        file_list.append(fp1)
        file_list.append(fp2)

        print("Done with selecting file")


    def process_file(self):
        print("Starting processing")

        #Open image file
        file = open(file_list[0], 'rb')

        #Convert file to base64
        b64_of_file = base64.b64encode(file.read())

        #get output file name e.g sample
        output_file_name = self.output_file_name.text()

        #get file format
        file_format = image_format[0]

        #Full file name e.g sample.jpg
        ffn = file_list[1]+output_file_name+'.'+file_format.lower()
        print(ffn)
        file2 = open(ffn, 'wb')
        file2.write(base64.b64decode(b64_of_file))
        
        file.close()
        file2.close()

        self.file.setText(f"File saved at: {file_list[1]}")


app = QApplication(sys.argv)
window = Converter()
window.show()
sys.exit(app.exec())



    
            
        
                
