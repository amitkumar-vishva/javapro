// -----------------------------------------------------------
//     what is Express?
// -----------------------------------------------------------

// Express js ak node js ka popular Framework hai

// Express js ka package install karne ke liye ye command run karo

        // ============================================
        // =           npm install express            =
        // ============================================


// import express from 'express'

// const app = express()
// const Port = 8000

// app.get('/',(req,res)=>{
//         res.send("This is my first server with the help of express.js ....")
// })

// app.listen(Port,()=>{
//         console.log("Express server is started .........");
        
// })

// ----------------------------------------------------------------
//         Routing in Express.js
// ----------------------------------------------------------------

import express from "express";
const app = express()

const Port = 8000;

app.get('/',(req,res)=>{
        res.json({name:"hello",class:"12"})
})

app.get('/about',(req,res)=>{
        res.send("About")
})

app.get('/contact',(req,res)=>{
        res.send("Contact")
})

app.listen(Port,()=>{
        console.log("server is statred............");
        
})