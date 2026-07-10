// server ko ham localhost:3000 par run karte hai

// import http from 'http'

// const post = 3000

// const server = http.createServer((req,res)=>{
//     res.end("This is my first server...........")
// })

// server.listen(post,()=>{
//     console.log("Server is started.........");
    
// })


// ------------------------------------------------
//     Routing in server
// ------------------------------------------------

import http from 'http'

const Port = 3000

const server = http.createServer((req, res)=>{
    if(req.url == "/"){
        res.end("Welcome to home page............")
    }
    else if(req.url == "/about"){
        res.end("Welcome to About Page............")
    }
    else if(req.url == "/contact"){
        res.end("Welcome to contact Page............")
    }
    else{
        res.end("404 Not Found")
    }
})

server.listen(Port,()=>{
    console.log("Server is started.............");
    
})

