// -------------------------------------------------------------------------
//     Http method 
// -------------------------------------------------------------------------

// GET =>  Server se data fetch karvana ho to es ka use karte hai (fronend par data get http method ki help se dekhta hai)
// POST => Server par data send karna ho 
// PATCH => Server par data already hai us ko update karna ho 
// DELETE => Server par data hai us ko delete karna hai

// ham yha par note create kar rahe hai (ye ak array of object note hai)

// Rule yaad rakho
// POST → req.body
// PUT → req.body
// PATCH → req.body
// GET → req.query ya req.params (body normally use nahi hoti)
// DELETE → Kabhi req.params, kabhi req.body (API design par depend karta hai)

// -------------------------------------------------------------------------
//     express.json() Middleware 
// -------------------------------------------------------------------------

// ->app.use(express.json()) Express ka ek middleware hai jo request ke andar
// aaye hue JSON data ko read karne ke liye use hota hai.Kyuki Express ko pata nahi hai ki JSON data ko kaise read karna hai.

//Syntax:

// app.use(express.json());

//Use:

// Jab client (Postman, frontend, mobile app) JSON format me data bhejta hai, tab `express.json()` us data ko parse karta hai.

// ### Example:

// ```javascript
// const express = require("express");

// const app = express();

// app.use(express.json());

// app.post("/notes", (req, res) => {
//     console.log(req.body);

//     res.status(201).json({
//         message: "Note created successfully"
//     });
// });
// ```

// ### Request Body:

// ```json
// {
//     "title": "Node.js",
//     "description": "Learn Express"
// }
// ```

// ### Output:

// ```javascript
// {
//     title: "Node.js",
//     description: "Learn Express"
// }
// ```

// ### Working Flow:

// Client JSON Data
// ↓
// `express.json()` middleware
// ↓
// `req.body`
// ↓
// Route Handler

// ### Important Points:

// * `express.json()` JSON data ko parse karta hai.
// * Iske bina `req.body` undefined aa sakta hai.
// * Isko routes se pehle likhte hain.
// * Mostly POST, PUT, PATCH requests ke saath use hota hai.




// ye me dunga 
// const note = {
//     title : "My first note",
//     description : "This is my first note"
// }

// or muje ye melega bo ak array of boject milega

// const notes = [
//     {
//         title : "My first note",
//         description : "This is my first note"
//     },
//     {
//         title : "My second note",
//         description : "This is my second note"
//     }

// ]


import express from "express";



const app = express();
// middleware
app.use(express.json())
const Port = 8000;

const notes = []

// data fronend se sever par aa raha tha
app.post('/notes',(req, res) => {
    notes.push(req.body);

    res.status(201).json({
        message: "notes created sucessfully"
    }) 
})

// data server se frontend par ja raha hai
app.get('/notes',(req, res) => {
    res.status(200).json({
        message: "notes fetch sucessfully",
        notes:notes
    })
})

// delete karne ke liye
app.delete('/notes/:id', (req, res) => {
    const index = req.params.id
    delete notes[index]

    res.status(200).json({
        message: "Note deleted successfully"
    });
});


app.listen(Port, ()=>{
    console.log("Server is started ............");
    
})

