import csv
import mysql.connector
import pymongo
import json

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
db = myclient['addressbook']
addresstable = db["addresstable"]

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="11111111",
  database="addresslist"
)
mycursor = mydb.cursor(buffered=True)
name = "BNB"

"""
filename = 'erc-usdc-coin.csv'
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
"""
"""
f = open("bnb.txt",mode="r")
address=[]
for line in f:
    address.append(line[0:42].lower())
      #print(line)
f.close() 
for ars in address:
  #print(ars)
  mycursor.execute("SELECT * FROM address WHERE address = %s", (ars, ))
  myresult = mycursor.fetchone()
  if (myresult==None):
      val = (ars, "",name)
      mycursor.execute("INSERT INTO address (address, amount,type) VALUES (%s, %s, %s)", val)
      mydb.commit()
      print("Inserted")

"""
print("MySql Address Querying...")
sqldata = []
mycursor.execute("SELECT * FROM address")
alldata = mycursor.fetchall()
sqldata=alldata

print("Mongodb Address Querying...")
data = []
doc = addresstable.find().sort("_id",-1).limit(1000000)
ab =0
try:
  for m in doc:
    data.append(m)
    #ab+=1
    #print(ab)
    #print(m["address"])
except:
  print("Mongodb error")

print("Searching...")

def filterData(address):
  for x in alldata:
    if(x[1].lower()==address.lower()):
      return True
    else:
      False  

for d in data:
    ab+=1
    if(filterData(d["address"])==True):
        break
    else:  
      addresstable.delete_one({"address": d["address"]})  
    print("Nonce : ",ab)
     

"""
print(len(data))

for d in data:
  print(d["address"])
  mycursor.execute("SELECT * FROM address WHERE address = %s", (m["address"], ))
  myresult = mycursor.fetchone()
  if (myresult!=None):
    print(m)
    print(myresult)
    break
  else:
    addresstable.delete_one({"address": m["address"]})
    
mycursor.execute("SELECT * FROM address")
alldata = mycursor.fetchall()
nv=0
for x in alldata:
  #print(x[1])
  nv +=1
  print(nv)
  mydoc = addresstable.find_one({ "address": x[1].lower() }) 
  if (mydoc!=None):
    print(mydoc) 
    break
  """