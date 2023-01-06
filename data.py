import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="11111111",
  database="addresslist"
)
mycursor = mydb.cursor()

filename = 'erc-usdc-coin.csv'
name = "ERC-USDC-Coin"
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        address = row[0]
        amount = row[1]
        try:
            if(float(amount)>=50):
                val = (address, amount,name)
                mycursor.execute("INSERT INTO address (address, amount,type) VALUES (%s, %s, %s)", val)
                mydb.commit()
                print("Inserted")
                #print(row[1])
        except Exception:
                print(row)
                #break
