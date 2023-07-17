from tkinter import filedialog#il permet d ouvrir et stoker un fichier et stocker le chemin
from PyQt5.uic import loadUi#contient le code qui represente l'interface graphique gérer par QTPY
from PyQt5 import QtWidgets#classe permettent de créer uen fenetre afin de fixer sa taille
from PyQt5.QtWidgets import QDialog #classe se base des boites de dialogue
import tkinter as Tk
import sys#il ajoute le chemin spécifique 

import pyttsx3#bibliothèque de synthése vocale
from tkinter import filedialog
from tkinter import *
from PyQt5 import QtCore,QtGui,QtWidgets#permet l interaction avec les boutons
from PyQt5.QtWidgets import QMessageBox,QApplication
import re#il permet la representation des expresssions regulieres.



sys.path.append('C:\desktop\pics')



class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()

        loadUi("OBJECT.ui", self)
        self.confirm.clicked.connect(self.confirmfunction)
        self.confirm2.clicked.connect(self.helpfunction)
        self.ok.clicked.connect(self.contact)


    def helpfunction(self):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("""si vous trouvez des problemes ,veuillez nous contactez:"
                     ******************
                     *hanae.hanim01@gmail.com
                     *laazizahmed72@gmail.com
                     *baknzizsaad@gmail.com
                     *kartbouni18@gmail.com
                     *****************""")
        msg.setWindowTitle("Contact")
        msg.exec_()

    def contact(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("""         

            --------------------------------------------------------------------
            Pour choisir une image clicker sur le button CHOISIR ET DETECTER
            Aprés vous serez obligés  de selectionner l'objet désiré à detectez
           
            ------------------*******************------------------
                         ---       Encore perdue?      ---
            clickez sur le boutton "contact" pour nous contactez
                    """)
        msg.setWindowTitle("contact")
        msg.exec_()













    def detectfunction(self):
        return self.detection.currentText()#il nous permet de lire le contenu stocker placé dans le combo box




    def confirmfunction(self):

        a=self.detectfunction()
        print(a)

        if a == 'BUILDING':

            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 130)
            engine.setProperty('Volume', 4.0)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            def speak(text):
                engine.say(text)
                engine.runAndWait()


            
            app = Tk()
            app.filename = filedialog.askopenfilename()#on a stocké le chemin de l'image importé
            app.destroy()#apres le choix de l'image on quitte l'interface tkinter
            img = cv2.imread(app.filename)#permet de convertir l'image en  MATRICE
            if app.filename !='':
                height, width = img.shape[:2]
            print(app.filename)

            while app.filename =='':#GESTION D'ERREUR - fichier image vide
                speak("you didn't choose an image")
                app = Tk()#relancement de la fenetre
                app.filename = filedialog.askopenfilename()
                app.destroy()
                img = cv2.imread(app.filename)
                if app.filename !='':
                    height, width = img.shape[:2]
                    break




            file = open("building.txt", "r+")#ouvrir le fichier pour la lecture et l'ecriture
            l = file.readlines()#lecture des lignes
            data = []# liste pour stocker les donnees ultierement
            c = []
            for i in range(len(l)):
                data.append(l[i].split(","))#eliminer les virgules entre les listes
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if j == len(data[0]) - 1 and "\n" in data[i][j]:
                        data[i][j] = data[i][j].rstrip(data[i][j][-1])#permet de supprimer le dernier element ( dans notre cas \n)
                        data[i][j] = int(data[i][j])#la suppression de \n qui noua a permet d'integere int                                  
                    else:
                        data[i][j] = int(data[i][j])
            for i in range(len(data)):
                if "/" + str(data[i][0]) + "." in app.filename:#il nous permet d'identifier l'image
                    image1 = cv2.rectangle(img, (data[i][1], data[i][2]), (data[i][3], data[i][4]), (150, 0, 0), 4)#dessiner un rectangle autour de l'objet qu'on veut detecter
                    image1 = cv2.putText(img, 'building', (data[i][1] + 10, data[i][2] + 100),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 4)#style d'ecriture
                    image1 = cv2.putText(img, "height : "+str((data[i][4]-data[i][2])/100)+"m", (int((width/3)),100),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    image1 = cv2.putText(img, "width : "+str((data[i][3]-data[i][1])/100)+"m", (int((width/3)),200),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    c.append([data[i][1], data[i][2], data[i][3], data[i][4]])#il pose les points (extrimités des diagonales de la sous matrice)permettant de calculer la largeur et la longueur
            if len(c) > 0:#verifier si l'objet se trouve dans l'image
                image = cv2.resize(image1, (1900, 1000))
                cv2.imshow("image", image)#afficher l'image avec la detection de l'objet désiré
                print("the approximate height : ", (c[0][3] - c[0][1]) / 100, "m")#calcul de la longueur en metres
                speak("the approximate height of the building: " + str((c[0][3] - c[0][1]) / 100) + "meter")
                print("the approximate weight : ", (c[0][2] - c[0][0]) / 100, "m")
                speak("the approximate weight of the building: " + str((c[0][2] - c[0][0]) / 100) + "meter")
                image1 = cv2.putText(img, "the approximate weight : "+str(c[0][2] - c[0][0] / 100)+ "m", (data[i][1] + 10, data[i][2] + 100),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 4)
                cv2.waitKey(0)
            else:
                print("there is no building in the picture")
                speak("there is no building in the picture")

        elif a == 'LIGHTING POLE':


            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 130)
            engine.setProperty('Volume', 5.0)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            def speak(text):
                engine.say(text)
                engine.runAndWait()


            app = Tk()
            app.filename = filedialog.askopenfilename()
            app.destroy()
            img = cv2.imread(app.filename)
            if app.filename !='':
                height, width = img.shape[:2]
            print(app.filename)
            while app.filename =='':
                speak("you didn't choose an image")
                app = Tk()
                app.filename = filedialog.askopenfilename()
                app.destroy()
                img = cv2.imread(app.filename)
                if app.filename !='':
                    height, width = img.shape[:2]
                    break
            file = open("lighting_poles_data.txt", "r+")
            l = file.readlines()
            data = []
            c = []
            for i in range(len(l)):
                data.append(l[i].split(","))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if j == len(data[0]) - 1 and "\n" in data[i][j]:
                        data[i][j] = data[i][j].rstrip(data[i][j][-1])
                        data[i][j] = int(data[i][j])
                    else:
                        data[i][j] = int(data[i][j])
            for i in range(len(data)):
                if "/" + str(data[i][0]) + "." in app.filename:
                    image1 = cv2.rectangle(img, (data[i][1], data[i][2]), (data[i][3], data[i][4]), (0, 255, 0), 4)
                    image1 = cv2.putText(img, 'light pole', (data[i][1] + 10, data[i][2] + 100),
                                             cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 4)
                    image1 = cv2.putText(img, "height : "+str((data[i][4]-data[i][2])/100)+"m", (int((width/3)),100),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    image1 = cv2.putText(img, "width : "+str((data[i][3]-data[i][1])/100)+"m", (int((width/3)),200),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    c.append([data[i][1], data[i][2], data[i][3], data[i][4]])
            if len(c) > 0:
                image = cv2.resize(image1, (1900, 1000))
                cv2.imshow("image", image)
                print("the approximate height : ", (c[0][3] - c[0][1]) / 100, "m")
                speak("the approximate height of the light pole is : " + str((c[0][3] - c[0][1]) / 100) + "meter")
                print("the approximate weight ", (c[0][2] - c[0][0]) / 100, "m")
                speak("the approximate weight of the light pole is : " + str((c[0][2] - c[0][0]) / 100) + "meter")
                if len(c) < 2:
                    print("there is only one light pole !!")
                    speak("there is only one light pole !!")
                else:
                    print("the distance between two light poles is :", (c[1][0] - c[0][0]) / 100, "m")
                    speak("the distance between two light poles is :" + str((c[1][0] - c[0][0]) / 100) + "meter")
                cv2.waitKey(0)
            else:
                print("there is no light pole in the picture")
                speak("there is no light pole in the picture")

        elif a =="ROAD":

            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 130)
            engine.setProperty('Volume', 4.0)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)

            def speak(text):
                engine.say(text)
                engine.runAndWait()

            app = Tk()
            app.filename = filedialog.askopenfilename()
            app.destroy()
            img = cv2.imread(app.filename)
            if app.filename !='':
                height, width = img.shape[:2]
            while app.filename =='':
                speak("you didn't choose an image")
                app = Tk()
                app.filename = filedialog.askopenfilename()
                app.destroy()
                img = cv2.imread(app.filename)
                if app.filename !='':
                    height, width = img.shape[:2]
                    break
            file = open("roads.txt", "r+")
            l = file.readlines()
            data = []
            c = []
            for i in range(len(l)):
                data.append(l[i].split(","))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if j == len(data[0]) - 1 and "\n" in data[i][j]:
                        data[i][j] = data[i][j].rstrip(data[i][j][-1])
                        data[i][j] = int(data[i][j])
                    else:
                        data[i][j] = int(data[i][j])
            for i in range(len(data)):
                if "/" + str(data[i][0]) + "." in app.filename:
                    image1 = cv2.rectangle(img, (data[i][1], data[i][2]), (data[i][3], data[i][4]), (150, 0, 0), 4)
                    image1 = cv2.putText(img, 'road', (data[i][1], data[i][2]), cv2.FONT_HERSHEY_PLAIN, 2,
                                             (0, 0, 255), 4)
                    image1 = cv2.putText(img, "height : "+str((data[i][4]-data[i][2])/100)+"m", (int((width/3)),100),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    image1 = cv2.putText(img, "width : "+str((data[i][3]-data[i][1])/100)+"m", (int((width/3)),200),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    c.append([data[i][1], data[i][2], data[i][3], data[i][4]])
            if len(c) > 0:
                image = cv2.resize(image1, (1900, 1000))
                cv2.imshow("image", image)
                print("the approximate height : ", (c[0][3] - c[0][1]) / 100, "m")
                speak("the approximate height of the road is: " + str((c[0][3] - c[0][1]) / 100) + "meter")
                print("the approximate weight : ", (c[0][2] - c[0][0]) / 100, "m")
                speak("the approximate weight of the road is: " + str((c[0][2] - c[0][0]) / 100) + "meter")
                cv2.waitKey(0)
            else:
                print("there is no road in the picture")
                speak("there is no road in the picture")
        elif a =='GRASS':
            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 130)
            engine.setProperty('Volume', 4.0)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            def speak(text):
                engine.say(text)
                engine.runAndWait()

            app = Tk()
            app.filename = filedialog.askopenfilename()
            app.destroy()
            img = cv2.imread(app.filename)
            if app.filename !='':
                height, width = img.shape[:2]
            while app.filename =='':
                speak("you didn't choose an image")
                app = Tk()
                app.filename = filedialog.askopenfilename()
                app.destroy()
                img = cv2.imread(app.filename)
                if app.filename !='':
                    height, width = img.shape[:2]
                    break

            file = open("green_space.txt", "r+")
            l = file.readlines()
            data = []
            c = []
            for i in range(len(l)):
                data.append(l[i].split(","))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if j == len(data[0]) - 1 and "\n" in data[i][j]:
                        data[i][j] = data[i][j].rstrip(data[i][j][-1])
                        data[i][j] = int(data[i][j])
                    else:
                        data[i][j] = int(data[i][j])
            for i in range(len(data)):
                if "/" + str(data[i][0]) + "." in app.filename:
                    image1 = cv2.rectangle(img, (data[i][1], data[i][2]), (data[i][3], data[i][4]), (150, 0, 0), 4)
                    image1 = cv2.putText(img, 'Green space', (data[i][1], data[i][2]), cv2.FONT_HERSHEY_PLAIN, 2,
                                             (0, 0, 255), 4)
                    image1 = cv2.putText(img, "height : "+str((data[i][4]-data[i][2])/100)+"m", (int((width/3)),100),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    image1 = cv2.putText(img, "width : "+str((data[i][3]-data[i][1])/100)+"m", (int((width/3)),200),
                                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
                    c.append([data[i][1], data[i][2], data[i][3], data[i][4]])
            if len(c) > 0:
                image = cv2.resize(image1, (1900, 1000))
                cv2.imshow("image", image)

                cv2.waitKey(0)
            else:
                print("there is no green space in the picture")
                speak("there is no green space in the picture")






app = QApplication(sys.argv)
Mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Mainwindow)
widget.setWindowTitle("OBJECT DETECTOR")
widget.setFixedWidth(1374)
widget.setFixedHeight(622)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")
