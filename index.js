var mysql = require('mysql');
var MongoClient = require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/"
const client = new MongoClient(url);
const db = client.db("addressbook");
var addresscollect = db.collection("addresstable")
addresscollect.find({address:"0x8ee6099e5e44a7e316bf0ed7fb36410effa116c"}).toArray(async function(err, result){
    if(result>0){
        console.log(result)
    }else{
        console.log("....")
    }
})

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


con.query("SELECT * FROM address", (err, result, fields) => {
    if (err) {
        throw err
    } else {
        var val = Object.values(JSON.parse(JSON.stringify(result)));
        for (var i = 0; i < val.length; i++) {
            console.log(val[i])
            if (val[i]["id"] == 10) {
              break;
            }
        }
    }
})


console.log("Endline ...........")