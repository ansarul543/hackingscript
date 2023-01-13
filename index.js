var mysql = require('mysql');
var MongoClient = require('mongodb').MongoClient;
var converter = require('hex2dec');
//https://www.npmjs.com/package/hex2dec
var ethers = require('ethers')

var url = "mongodb://localhost:27017/"
const client = new MongoClient(url);
const db = client.db("addressbook");
var addresscollect = db.collection("addresstable")

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "11111111",
    database: "addresslist",
    timezone: 'utc'
});
con.connect(function (err) {
    if (err) {
        throw err
    }
})

Number.MAX_SAFE_INTEGER+6924101995472446595168523276373890648511538260867813874559900090387991535772600

var sqldata = []

let number = "69241019954724465951685232763738906485115382608678138745599000903879915357726";
//console.log(number.toLocaleString('fullwide', {useGrouping:false}))
//console.log(number.toString())
//var privateKey = converter.decToHex(number, { prefix: false });
//console.log(privateKey)


var minv = "18012827153960864754624460067314899934289787607017033346142888690430615982161"
var maxv = "79241019954724465951685232763738906485115382608678138745599000903879915057901"
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return BigInt(Math.floor(Math.random()* (max - min + 1))  + min);
}
//console.log(getRandomInt(minv, maxv))

async function getData() {
    await con.query("SELECT * FROM address", async (err, result, fields) => {
        if (err) {
            throw err
        } else {
            var val = await Object.values(JSON.parse(JSON.stringify(result)));
            for (var i = 0; i < val.length; i++) {
                await sqldata.push(val[i])
            }
            nonce = 0;
            var num = BigInt("68012827153960868850514310250827697934122923227184115023474753406989251790688")
            for (i = 0; i < 10000000; i++) {
                nonce += 1;
                num +=1n
                var number1 = getRandomInt(minv, maxv).toLocaleString('fullwide', {useGrouping:false});
                //number1 = num.toLocaleString('fullwide', {useGrouping:false});
                var privateKey1 = converter.decToHex(number1, { prefix: false });
                //console.log(privateKey1)
                var wallet = new ethers.Wallet(privateKey1);
                var address = wallet.address.toLowerCase()
                //console.log("Address: " + address)
                countv=0;
                var ck = sqldata.filter(rs => {
                    //countv+=1
                    if (address == rs.address.toLowerCase()) {
                        return rs;
                    }
                })
                if (ck.length > 0) {
                    console.log("")
                    console.log("")
                    console.log(".....................................Welcome...................................................")
                    console.log("")
                    console.log("")
                    console.log("Address : ",address)
                    console.log("Private Key : ",privateKey1)
                    console.log("Decimal Key : ",number1)
                    console.log("")
                    console.log("")
                    console.log(".................Address Macthed Successfully..................Enjoy..............Now...........")
                    
                    break
                } else {
                    console.log("Nonce : ", nonce)
                    //console.log("Address Count : ",countv)
                    console.log("Address : ", address)
                    console.log("Key : ",privateKey1)
                    console.log("Decimal Key : ",number1)
                    console.log("")
                    console.log("............................Line Break............................")
                    console.log("")
                }
            }
        }
    })


}




getData()