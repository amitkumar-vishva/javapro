// -----------------------------------------------------------------
//     Connect mongodb
// -----------------------------------------------------------------

// jab ham ko database connect karne ho tab ham ak (config) name ka folder banate hai,
// us ke andar (db.js) file banate hai us me database ko connect karte hai

import mongodb from "mongodb";

const connectDB = async () =>{
    try{
        await mongoose.connect(process.env.MONGODB_URL)
        console.log("DB Connected sucessfully....");
    }catch(err){
        console.log("DB Connection error ", err);
    }
}

export default connectDB;

// ab ham index.js me ja kar connectDB ko call kardege


import express from "express";
import dotenv from "dotenv"
dotenv.config()
import connectDB from "./config/db"


let app = express()
let port = process.env.PORT || 5000;

app.get("/", (req, res)=>{
    res.send("hello")
})


app.listen(port,()=>{
    connectDB() //calling
    console.log(`server is started at ${port}`);
})

//------> or


import express from "express";
import dotenv from "dotenv";
import connectDB from "./config/db.js";

dotenv.config();

const app = express();

const PORT = process.env.PORT || 5000;

// API route
app.get("/", (req, res) => {
  res.send("Hello MERN");
});

const startServer = async () => {
  try {
    // Pehle database connect hoga
    await connectDB();

    // Phir server start hoga
    app.listen(PORT, () => {
      console.log(`🚀 Server running on ${PORT}`);
    });

  } catch (error) {
    console.log(error);
  }
};

startServer();


//-----> or 


import express from "express";
import dotenv from "dotenv";
import connectDB from "./config/db.js";

dotenv.config();
const app = express();

// ================= TEST =================
app.get("/", (req, res) => {
  res.send("Testing Sucessfully Running 🚀");
});

// ================= DB =================
const uri = process.env.MONGO_URI;

if (!uri) {
  console.error("❌ MONGO_URI missing");
  process.exit(1);
}

// Agar database connected nahi hai to query ko hold mat karo, turant error do."
mongoose.set("bufferCommands", false);

// ================= START SERVER =================
const startServer = async () => {
  try {
    await mongoose.connect(uri);
    console.log("🔥 MongoDB connected");

    const PORT = process.env.PORT || 5000;

    app.listen(PORT, () => {
      console.log(`🚀 Server running on ${PORT}`);
    });

  } catch (err) {
    console.log("❌ DB error:", err);
    // Program error ki wajah se band hua.
    process.exit(1);
  }
};

startServer();

