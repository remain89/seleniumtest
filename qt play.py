import sys
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5 import uic
form_class = uic.loadUiType("untitled.ui")[0]
import keponefunction
from selenium import webdriver

class MyWindow(QDialog, form_class):

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)
        self.pushButton_3.clicked.connect(self.btn3_clicked)
        self.pushButton_4.clicked.connect(self.btn4_clicked)

    def btn_clicked(self) :
      number=self.textEdit.toPlainText()
      chromedriver = 'C:\chromedriver.exe'
      driver = webdriver.Chrome(chromedriver)
      driver.get('http://59.3.93.125:8085/aimir/login')
      keponefunction.Login(driver)

      keponefunction.LPDownload(driver,number)
      driver.quit()  # 창 종료


    def btn2_clicked(self) :
       number=self.textEdit.toPlainText()
       chromedriver = 'C:\chromedriver.exe'
       driver = webdriver.Chrome(chromedriver)
       driver.get('http://59.3.93.125:8085/aimir/login')
       keponefunction.Login(driver)

       keponefunction.LPCheck(driver,number)
       driver.quit() # 창 종료

    def btn3_clicked(self) :
        number = self.textEdit.toPlainText()
        chromedriver = 'C:\chromedriver.exe'
        driver = webdriver.Chrome(chromedriver)
        driver.get('http://59.3.93.125:8085/aimir/login')
        keponefunction.Login(driver)

        keponefunction.GMMPTest(driver,number)

    def btn4_clicked(self) :
        number = self.textEdit.toPlainText()
        mnumber = self.textEdit_2.toPlainText()
        chromedriver = 'C:\chromedriver.exe'
        driver = webdriver.Chrome(chromedriver)
        driver.get('http://59.3.93.125:8085/aimir/login')
        keponefunction.Login(driver)

        keponefunction.SELP(driver,number,mnumber)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   myWindow = MyWindow()
   myWindow.show()
   app.exec_()