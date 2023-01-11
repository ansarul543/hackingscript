import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QMessageBox,QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer,QTime,Qt,QDate,QSize
from PyQt5 import uic,QtGui,QtCore,QtSql
import blocksmith
from keygen import *
from addressgen import CryptoWallet
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="11111111",
  database="addresslist"
)
mycursor = mydb.cursor(buffered=True)

class MainWin(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        uic.loadUi('./main.ui', self)
        self.setWindowTitle("Cryptocurrency Decrypt Tools")
        self.setWindowIcon(QtGui.QIcon("./icon.png"))
        self.newaddressbtn.clicked.connect(self.NewAddress)
        self.signbtn.clicked.connect(self.SignAddress)
        self.hackstartbtn.clicked.connect(self.HakingStart)
        self.reset1.clicked.connect(self.ResetNew)
        self.reset.clicked.connect(self.ResetHack)


    def HakingStart(self):
        inputadd = self.inputaddress.text()
        fromn = 69241019954724465951685232763738906485115382608678138745599000903879915057901
        endnum = 97961055421793202728119147264747681425359989749448018624932072528561029839314
        nonce =0
        #decimal = 69241019954724465951685232763738906485115382608678138745599000903879915057901
        
        for i in range(fromn,endnum):
                nonce+=1
                #decimal+=1
                decimal = random.randint(fromn, endnum)
                key = f'{int(decimal):x}'
                newadd = CryptoWallet.generate_address(key)#"0x748934b822a52903bdf8cda7d32a4943463e0403"
                #publickey = CryptoWallet.publickeyval(key)
                
                print("Private Key : ",key)
                print("Nonce : ",nonce)
                print("Decimal : ",decimal)
                print("New Address : ",newadd.lower())
                print("Input Address ",inputadd.lower())
                
                print("................................New Line.............................")
                self.privatekey.setText(key)
                #self.publickey.setText(publickey.decode("utf-8"))
                self.address.setText(newadd)
                self.status.setText("False")
                mycursor.execute("SELECT * FROM address WHERE address = %s", (newadd, ))
                myresult = mycursor.fetchone()
                if(myresult!=None):
                    self.privatekey.setText(key)
                    self.address.setText(newadd)
                    self.status.setText("True")
                    self.publickey.setText(CryptoWallet.publickeyval(key).decode("utf-8"))
                    print(".....................................Matching ..............................")
                    break
                else:
                    print(myresult)

  
        else:
            QMessageBox.warning(None, ("Error"), 
            ("Input address is required"),
             QMessageBox.Ok)

    def SignAddress(self):
        privatekey1 = self.privatekey1.text()
        try:
            address = CryptoWallet.generate_address(privatekey1)
            checksum = CryptoWallet.checksum_address(address)
            public = CryptoWallet.publickeyval(privatekey1).decode()
            self.publickey1.setText(public)
            self.address1.setText(checksum)
            self.status1.setText("True")         
        except:
            #print("Invalid Private Key")
            self.status1.setText("False") 
            QMessageBox.warning(None, ("Error"), 
            ("Invalid Private Key Try Again"),
             QMessageBox.Ok)

    def NewAddress(self):
        kg = KeyGenerator()
        kg.seed_input('')
        key = kg.generate_key()
        address = CryptoWallet.generate_address(key)
        checksum = CryptoWallet.checksum_address(address)
        public = CryptoWallet.publickeyval(key).decode()
        print("Private Key :")
        print(key)
        print(int(key, base=16))
        print("")
        print("Public Key :")
        print(public)
        print(int(public, base=16))
        print("")
        print("Address :")
        print(address)
        print(int(address, base=16))
        print("")
        print("...............................Line Break...............................")

        """print([{"privateKey":key,
                 "publickey":public,
                 "address":address,
                 "check_sum":checksum
                 }])"""
        self.privatekey1.setText(key)
        self.publickey1.setText(public)
        self.address1.setText(checksum)
        self.status1.setText("True")

    def ResetHack(self):
        self.privatekey.setText("")
        self.publickey.setText("")
        self.address.setText("")
        self.status.setText("")
        self.inputaddress.setText("")
    def ResetNew(self):
        self.privatekey1.setText("")
        self.publickey1.setText("")
        self.address1.setText("")
        self.status1.setText("")



if __name__=="__main__":
    app = QApplication(sys.argv)
    wt=MainWin()
    wt.show()
    sys.exit(app.exec_())