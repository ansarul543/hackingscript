import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QMessageBox,QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer,QTime,Qt,QDate,QSize
from PyQt5 import uic,QtGui,QtCore,QtSql
import blocksmith
from keygen import *

print("Okkk")

nonce=0
while False:
    nonce+=1
    print(nonce)   
    kg = KeyGenerator()
    key = kg.generate_key()
    print(key)
    address = blocksmith.EthereumWallet.generate_address(key)
    print(address)
    if(address=="0xf977814e90da44bfa03b6295a0616a897441acec"):
        print("") #4,061,115.4546546 BNB
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break     
    elif(address=="0x73bceb1cd57c711feac4224d062b0f6ff338501e"):
        print("")#1,910,504.53010949 Ether
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break      
    elif(address=="0x9bf4001d307dfd62b26a2f1307ee0c0307632d59"):
        print("")#1,490,000.0180927 Ether
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break

    elif(address=="0x176f3dab24a159341c0509bb36b833e7fdd0a132"):
        print("")#291,046.56106656 Ether
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break
    elif(address=="0x8103683202aa8da10536036edef04cdd865c225e"):
        print("")# 275,000.02741999 Ether
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break    

    elif(address=="0xc90b04b27559d78ab95e56ea27119a38bcc66700"):
        print("")#81,880.39336024 BNB
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break
    elif(address=="0x21d45650db732ce5df77685d6021d7d5d1da807f"):
        print("")# 50,119.06563101 BNB
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break    

    elif(address=="0x4e7388199254abd454e8d51d8e2b70eb0af4d740"):
        print("")#44,135.45707496 BNB
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break
    elif(address=="0xd183f2bbf8b28d9fec8367cb06fe72b88778c86b"):
        print("")# 42,103.068079 BNB
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break     

    elif(address=="0x5bc7ee41a3668c58871c7416ab5b0ae119ece544"):
        print("")#39,735.99977471 BNB
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break
    elif(address=="0x0548f59fee79f8832c299e01dca5c76f034f558e"):
        print("")# 38,342.34308067 BNB
        print("")
        print("Privake : "+key)
        print("Address : "+address)
        print("Status : Success")
        print(nonce)
        break     

class MainWin(QWidget):
    def __init__(self,id='',lid='',type='',parent=None):
        super().__init__()
        uic.loadUi('./main.ui', self)
        self.setWindowTitle("Cryptocurrency Decrypt Tools")
        self.setWindowIcon(QtGui.QIcon("./icon.png"))


if __name__=="__main__":
    app = QApplication(sys.argv)
    wt=MainWin()
    wt.show()
    sys.exit(app.exec_())