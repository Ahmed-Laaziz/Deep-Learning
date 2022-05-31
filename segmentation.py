from PyQt5 import QtCore, QtGui, QtWidgets

import cv2

import numpy as np
from tkinter import filedialog
from tkinter import *
from matplotlib import pyplot as pltd
import random
from PyQt5.QtWidgets import QMessageBox,QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1194, 700)
        MainWindow.setFixedSize(1194,700)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 1191, 111))
        self.label.setStyleSheet("background-color: rgb(150, 149, 159);\n"
            "color:rgb(255, 255, 255);font-size: 40pt\n"
"")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.insert)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 230, 401, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(150, 149, 159);\n"
"color: rgb(255, 255, 255);\n"
"font-size:13pt")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.clicked.connect(self.help)
        self.pushButton_3.setGeometry(QtCore.QRect(1040, 540, 101, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(150, 149, 159);\n"
"background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font-size:13pt")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.clicked.connect(self.contact)
        self.pushButton_4.setGeometry(QtCore.QRect(1040, 600, 101, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(150, 149, 159);\n"
"background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);\n"
"font-size:13pt")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 180, 16, 471))
        self.line.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 180, 20, 461))
        self.line_2.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(340, 180, 20, 461))
        self.line_3.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(290, 180, 16, 461))
        self.line_4.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(190, 180, 20, 461))
        self.line_5.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(240, 180, 16, 461))
        self.line_6.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(140, 180, 16, 461))
        self.line_8.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(1150, 180, 16, 471))
        self.line_10.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(1100, 180, 20, 351))
        self.line_11.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(1050, 180, 20, 351))
        self.line_12.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(990, 180, 20, 461))
        self.line_14.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(940, 180, 20, 471))
        self.line_15.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(840, 180, 16, 471))
        self.line_16.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(790, 180, 16, 471))
        self.line_17.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(890, 180, 16, 471))
        self.line_18.setStyleSheet("background-color: rgb(150, 149, 159);")
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1194, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
  
    def help(self):
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Question)
         msg.setText("""
     «Choisir l'image à Analyser» va te permettre de choisir
   une image qui va être convertie en image grise pour être 
   analyser et traîter. La sortie sera l'image grise et l'image 
   avec des contours.
 __________________________________________________________
 
                        Encore Perdue? 
 Clickez sur le boutton "Contact" pour nous contacter.
 _________________________________________________________""")
         msg.setWindowTitle("Aide")
         msg.exec_()
    def contact(self):
         msg = QMessageBox()
         msg.setIcon(QMessageBox. Information)
         msg.setText("""Veuillez nous SVP pour plus d'information:
                        ***********************************
                        * hanae.hanim01@gmail.com  
                        * laazizahmed72@gmail.com  
                        * baknzizesaad@gmail.com  
                        * kartbouni18@gmail.com   
                        ***********************************""")
         msg.setWindowTitle("Contact")
         msg.exec_()
         
    def insert(self):
        app = Tk()
        app.filename =  filedialog.askopenfilename()
        app.destroy()
        img = cv2.imread(app.filename)
        imgResize = cv2.resize(img, (1900,1000))
        #img_gray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
        imgCanny = cv2.Canny(imgResize, 400, 400)
        
        class HomogeneousBgDetector():
            def _init_(self):
                pass

            def detect_objects(self, frame):
                # Convert Image to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                kernel = np.ones((5, 5), np.uint8)

                #imgCanny = cv2.Canny(frame, 500, 400)
                #imgDilation = cv2.dilate(imgCanny, kernel, iterations=3)
                #imgEroded = cv2.erode(imgDilation, kernel, iterations=3)

                # Create a Mask with adaptive threshold
                mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

                # Find contours
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                cv2.imshow("mask", mask)
                objects_contours = []

                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > 2000:
                        #cnt = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
                        objects_contours.append(cnt)

                return objects_contours
        detector = HomogeneousBgDetector()
        contours = detector.detect_objects(imgResize)

        # Draw objects boundaries
        for cnt in contours:
            # Get rect
            rect = cv2.minAreaRect(cnt)
            (x, y), (w, h), angle = rect

            # Get Width and Height of the Objects by applying the Ratio pixel to cm


            # Display rectangle
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            l = [0, 255]
            #cv2.circle(imgResize, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(imgResize, [cnt], True, (random.choice(l),random.choice(l), random.choice(l)), 2)
            cv2.putText(imgResize, "Width {} m".format(round(w/10, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
            cv2.putText(imgResize, "Height {} m".format(round(h/10, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
        #print((cnt))






        cv2.imshow("Image", imgResize)
        cv2.waitKey(0)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                Détection d'objet"))
        self.pushButton_2.setText(_translate("MainWindow", "Choisir l'image à Analyser"))
        self.pushButton_3.setText(_translate("MainWindow", "Aide"))
        self.pushButton_4.setText(_translate("MainWindow", "Contact"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    


