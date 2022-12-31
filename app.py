import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QMessageBox,QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer,QTime,Qt,QDate,QSize
from PyQt5 import uic,QtGui,QtCore,QtSql
import blocksmith
from keygen import *
from addressgen import CryptoWallet
import pymongo

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
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.myclient['addressbook']
        self.addresstable = self.db["addresstable"]


    def HakingStart(self):
        inputadd = self.inputaddress.text()
        fromn = 11000000000000000000000000000000000000000000000000000000000000000000000401131
        endnum = 99999999999999999999999999999999999999999999999999999999999999999999999999999
        nonce =0
        decimal = 11000000000000000000000000000000000000000000000000000000000000000000000401131
        lastdecimal = self.addresstable.find().sort("_id", -1).limit(1)
        for x in lastdecimal:
            fromn = int(x["decimal"])
            decimal = int(x["decimal"])
            #print(x["decimal"])
        if (inputadd !=""):
            for i in range(fromn,endnum):
                nonce+=1
                decimal+=1
                key = f'{int(decimal):x}'
                newadd = CryptoWallet.generate_address(key)
                publickey = CryptoWallet.publickeyval(key)
                
                print("Private Key : ",key)
                print("Nonce : ",nonce)
                print("Decimal : ",decimal)
                print("New Address : ",newadd.lower())
                print("Input Address ",inputadd.lower())
                
                print("................................New Line.............................")
                self.privatekey.setText(key)
                self.publickey.setText(publickey.decode("utf-8"))
                self.address.setText(newadd)
                self.status.setText("False")

                data = {"decimal":str(decimal),"private_key":key.lower(),"address":newadd.lower(),"status":"Failed"}
                data1 = {"decimal":str(decimal),"private_key":key.lower(),"address":newadd.lower(),"status":"Success"}
                ent = self.addresstable.find_one({"decimal":str(decimal)})
                
                if(inputadd.lower()==newadd.lower()):
                    self.privatekey.setText(key)
                    self.publickey.setText(publickey.decode("utf-8"))
                    self.address.setText(newadd)
                    self.status.setText("True")
                    self.addresstable.insert_one(data1)
                    break
                else:
                    if ent==None:
                        self.addresstable.insert_one(data)  
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