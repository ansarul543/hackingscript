import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QMessageBox,QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer,QTime,Qt,QDate,QSize
from PyQt5 import uic,QtGui,QtCore,QtSql

class MainWin(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        uic.loadUi('./cal.ui', self)
        self.setWindowTitle("Calculator")
        self.quoated=""
        self.plus.clicked.connect(self.plusB)
        self.minus.clicked.connect(self.minusB)
        self.mul.clicked.connect(self.mulB)
        self.divide.clicked.connect(self.divideB)
        self.equal.clicked.connect(self.equalB)
    
    def equalB(self):
        base = self.base.text()
        quote = self.quote.text()
        #d = int("F83a27eDEFe74E6A1aA936f18D0c03f8CA4Fa91A", base=16) // hexadicimal to decimal
        #print(d)
        #hex(int(888)) // Decimal to hexadecimal f'{int(totalmul):x}'
        if base=="":
            QMessageBox.warning(None, ("Error"), 
            ("Base Number empty"),
             QMessageBox.Ok)
        elif quote=="":
            QMessageBox.warning(None, ("Error"), 
            ("Quote Number empty"),
             QMessageBox.Ok)             
        elif self.quoated=="":
            QMessageBox.warning(None, ("Error"), 
            ("Symbol is empty"),
             QMessageBox.Ok) 
        else:
            if self.quoated=="+":
                totaladd = float(base)+float(quote)
                self.output.setText(f'{totaladd:.8f}')
                self.symbol.setText("Output +")
                #print(f'{totaladd:.8f}')
            if self.quoated=="-":
                totalsub = float(base)-float(quote)
                self.output.setText(f'{totalsub:.8f}')
                self.symbol.setText("Output -")
                #print(f'{totalsub:.8f}')
            if self.quoated=="*":
                totalmul = float(base)*float(quote)
                self.output.setText(f'{totalmul:.8f}')
                self.symbol.setText("Output *")
                print("Address :")
                print(base)
                print(f'{int(base):x}'.upper()) #.lower()
                print("Public Key :")
                print(f'{totalmul:.0f}')
                print(f'{int(totalmul):x}')
                print("Private Key :")
                getprivate = totalmul/100000000000000000000000000000000000000000000000000000000000000000000000000000
                print(f'{getprivate:.0f}')
                print(f'{int(getprivate):x}')
                #print(f'{totalmul:.8f}')
                print("..............................Line Break..............................")
            if self.quoated=="/":
                totaldiv = float(base)/float(quote)
                self.output.setText(f'{totaldiv:.8f}')
                self.symbol.setText("Output /")


    def plusB(self):
        self.quoated="+"    
    def minusB(self):
        self.quoated="-"  
    def mulB(self):
        self.quoated="*"      
    def divideB(self):
        self.quoated="/"  

if __name__=="__main__":
    app = QApplication(sys.argv)
    wt=MainWin()
    wt.show()
    sys.exit(app.exec_())