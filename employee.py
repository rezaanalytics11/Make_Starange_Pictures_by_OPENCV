import sqlite3
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
import test
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
import numpy as np
import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget,
  QPushButton, QVBoxLayout, QHBoxLayout,QGridLayout,QLineEdit)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.new_label0 = QLabel(self)
        self.new_label1 = QLabel(self)
        self.new_label2 = QLabel(self)
        self.new_label3 = QLabel(self)
        self.new_label4 = QLabel(self)
        hbox1 = QHBoxLayout()

        # hbox1.addWidget(self.new_label0)
        # hbox1.addWidget(self.new_label1)
        # hbox1.addWidget(self.new_label2)
        # hbox1.addWidget(self.new_label3)
        # hbox1.addWidget(self.new_label4)


        self.label1 = QLabel('First Name', self)
        hbox0 = QHBoxLayout()
        hbox0.addWidget(self.label1)
        self.name = QLineEdit(self)
        hbox0.addWidget(self.name)

        self.label2 = QLabel('Last Name', self)
        hbox0.addWidget(self.label2)
        self.last_name = QLineEdit(self)
        hbox0.addWidget(self.last_name)

        self.label3 = QLabel('Fathers\' Name', self)
        hbox0.addWidget(self.label3)
        self.fathers_name= QLineEdit(self)
        hbox0.addWidget(self.fathers_name)

        self.label4 = QLabel('Dtae of Birth', self)
        hbox0.addWidget(self.label4)
        self.birth_date= QLineEdit(self)
        hbox0.addWidget(self.birth_date)

        self.label5 = QLabel('photo url', self)
        hbox0.addWidget(self.label5)
        self.url= QLineEdit(self)
        hbox0.addWidget(self.url)

        self.label6 = QLabel('', self)
        self.label6.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human2.jpg"))
        hbox0.addWidget(self.label6)


        self.label7 = QLabel('', self)
        hbox1.addWidget(self.label7)

        #Empty Label
        self.label8 = QLabel('', self)
        hbox1.addWidget(self.label8)

        self.label9 = QLabel('', self)
        hbox1.addWidget(self.label9)

        self.label10 = QLabel('', self)
        hbox1.addWidget(self.label10)

        hbox2 = QHBoxLayout()
        self.label11 = QLabel('', self)
        hbox2.addWidget(self.label11)

        self.label12 = QLabel('', self)
        hbox2.addWidget(self.label12)

        self.label13 = QLabel('', self)
        hbox2.addWidget(self.label13)

        self.label14 = QLabel('', self)
        hbox2.addWidget(self.label14)

        Button = QPushButton('+')
        hbox0.addWidget(Button)
        Button.clicked.connect(self.addnewtasktodatabase)

        # delete_button = QPushButton('-')
        # hbox1.addWidget(delete_button)
        # delete_button.clicked.connect(self.delete)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.setAlignment(Qt.AlignHCenter)
        vbox.setAlignment(Qt.AlignVCenter)
        self.setLayout(vbox)

        #self.setGeometry(400, 400, 300, 150)
        self.setWindowTitle('Box layout example, QHBoxLayout, QVBoxLayout')
        self.show()

    def addnewtasktodatabase(self):

        a=self.name.text()
        b=self.last_name.text()
        c=self.birth_date.text()
        d=self.fathers_name.text()
        e=self.url.text()

        con = sqlite3.connect(r'C:\Users\Ariya Rayaneh\Desktop\employee.db')
        my_cursor = con.cursor()
        my_cursor.execute(f"INSERT INTO employee (name,last_name,father_name,birth_date,url) VALUES('{a}','{b}','{c}','{d}','{e}') ")
        con.commit()

        self.name.setText('')
        self.last_name.setText('')
        self.birth_date.setText('')
        self.fathers_name.setText('')
        self.url.setText('')

        self.readFromDatabase()

    # def delete(self):
    #
    #     con = sqlite3.connect(r'C:\Users\Ariya Rayaneh\Desktop\employee.db')
    #     my_cursor = con.cursor()
    #
    #     print(self.results)


    def readFromDatabase(self):
        con = sqlite3.connect(r'C:\Users\Ariya Rayaneh\Desktop\employee.db')
        my_cursor = con.cursor()
        my_cursor.execute("SELECT * FROM employee")
        self.results=my_cursor.fetchall()
        print(self.results)

        for i in range(len(self.results)):

            self.new_label0.setText(self.results[i][0])
            self.new_label1.setText(self.results[i][1])
            self.new_label2.setText(self.results[i][2])
            self.new_label3.setText(self.results[i][3])
            self.new_label4.setText(self.results[i][4])

        self.draw()



    def draw(self):


     img = cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\human2.jpg")
     #img = cv2.blur(img, (10, 10))
     img1 = cv2.flip(img, 90)
     img2 = cv2.bitwise_or(img1, img)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output.jpg", img2)
     self.label7.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output.jpg"))

     img2 = cv2.bitwise_and(img1, img)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output1.jpg", img2)
     self.label8.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output1.jpg"))

     # img2 = cv2.blur(img,(20,20))
     # cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output2.jpg", img2)
     # self.label9.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output2.jpg"))

     img2 = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
     img2 = cv2.flip(img2, -90)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output3.jpg", img2)
     self.label9.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output3.jpg"))

     img2 = cv2.bitwise_xor(img1, img)
     img2 = cv2.flip(img2, 90)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output4.jpg", img2)
     self.label10.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output4.jpg"))

     img2 = cv2.bitwise_not(img1, img)
     img2 = cv2.flip(img2, 90)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output5.jpg", img2)
     self.label11.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output5.jpg"))

     img2 =cv2.cvtColor(img2,cv2.COLOR_RGB2HSV)
     img2 = cv2.flip(img2, 90)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output6.jpg", img2)
     self.label12.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output6.jpg"))

     img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2HLS)
     img2 = cv2.flip(img2, 90)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output7.jpg", img2)
     self.label13.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output7.jpg"))

     img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
     img2 = cv2.flip(img2, -90)
     cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\human20_output8.jpg", img2)
     self.label14.setPixmap(QPixmap(r"C:\Users\Ariya Rayaneh\Desktop\human20_output8.jpg"))

if __name__ == '__main__':
 app = QApplication(sys.argv)
 ex = Example()
 sys.exit(app.exec_())


