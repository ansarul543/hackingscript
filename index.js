var mysql = require('mysql');
var MongoClient = require('mongodb').MongoClient;

var url = "mongodb://localhost:27017/"
const client = new MongoClient(url);
const db = client.db("addressbook");
var addresscollect = db.collection("addresstable")
var mongodata =[]
var sqldata=[]
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

async function getData(){
    await addresscollect.find({}).sort({"_id":-1}).limit(1000000).toArray(async function(err, result){
        if(result.length>0){
            //console.log(result)
            result.map(rmd=>{
                mongodata.push(rmd)
            })
            await con.query("SELECT * FROM address", async(err, result, fields) => {
                if (err) {
                    throw err
                } else {
                    var val =await Object.values(JSON.parse(JSON.stringify(result)));
                    for (var i = 0; i < val.length; i++) {
                        await sqldata.push(val[i])
                    }
                    nonce =0;
                    for(i=0;i<mongodata.length;i++){
                        nonce+=1;
                        countv=0;
                        address = mongodata[i]["address"]
                        var myquery = { address: address };
                        var ck = sqldata.filter(rs=>{
                            //countv+=1
                            if(mongodata[i]["address"]==rs.address){
                                return rs;
                            }
                        })
                        if(ck.length>0){
                            break
                        }else{
                            await db.collection("addresstable").deleteOne(myquery, function(err, obj) {
                                if (err){
                                    console.log(err)
                                }else{
                                    console.log(address+" deleted ");
                                }
                                db.close();
                              });
                              console.log("Nonce : ",nonce)
                              //console.log("Address Count : ",countv)
                              console.log("Address : ", address)

                        }
                        
                        //console.log(mongodata[i]["address"])
                    }
                }
            })
            //console.log(mongodata)
        }else{
            console.log("....")
        }
    })
    
    
    
    console.log("Endline ...........")
}

getData()