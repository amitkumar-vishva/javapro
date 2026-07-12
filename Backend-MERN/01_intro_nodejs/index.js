// ---------------------------------------------------------------
//     npm init kya hai?
// ---------------------------------------------------------------

// -> npm init ka use Node.js project ko initialize karne ke liye hota hai. 
// Ye command project ke liye ek package.json file banati hai.

// ---------------------------------------------------------------
//     package.json kya hoti hai?
// ---------------------------------------------------------------

// -> Ye project ki information aur settings store karti hai, jaise:

// Project ka naam
// Version
// Description
// Author
// License
// Dependencies (kaun-kaun se packages install hain)
// Scripts (jaise npm start, npm test)

// ---------------------------------------------------------------
//     npm init ka use kyun karte hain?
// ---------------------------------------------------------------

// -> Jab aap naya Node.js project start karte ho, tab:

// Project ki basic information save hoti hai.
// Baad me install hone wale packages dependencies me automatically add ho jate hain.
// Scripts define kar sakte ho.
// Project ko dusre developers ke saath share karna aasaan ho jata hai.

// ---------------------------------------------------------------
//     packege.json (formate)
// ---------------------------------------------------------------

// {
//   "name": "my-app",
//   "version": "1.0.0",
//   "description": "",
//   "main": "index.js",
//   "scripts": {
//     "start": "node index.js"
//   },
//   "author": "",
//   "license": "ISC"
// }

// ---------------------------------------------------------------
//     npm init -y ka use?
// ---------------------------------------------------------------

// -> npm init -y ka matlab hai default settings ke saath turant package.json file bana dena, 
// bina aapse koi question poochhe

// -> To npm automatically ek package.json file bana deta hai.

// ---------------------------------------------------------------
//     Scripts
// ---------------------------------------------------------------

// -> Agar ham project ko apne man ke accoding run karna chate hai jese (npm run dev) to ham ko script me update karna hoga

// -> scripts package.json ka ek section hota hai jisme aap commands ko shortcut naam de sakte ho. Baad me unhe npm run ya npm se aasani se chala sakte ho.

// {
//   "scripts": {
//     "start": "node index.js",
//     "dev": "nodemon index.js",
//     "test": "echo \"No tests\""
//   }
// }


// ---------------------------------------------------------------
//     import/export
// ---------------------------------------------------------------

// -> Agar ham backend me import export use karna chate hai to ham ko package.json file me 
// (type ko module) karna hoga


// ---------------------------------------------------------------
//     node module
// ---------------------------------------------------------------

// agar kisi karna barsh (node module) folder delete ho jaye to (npm install) ye command run kar do bo sab 
// kuch recover ho jayega

// ---------------------------------------------------------------
//     nodemon
// ---------------------------------------------------------------

// -> nodemon ko development ke time use kiya jata hai taaki code me change karte hi server automatically restart ho jaye.
// install karne ke liye command  (npm i nodemon)

// how to use nodemon

// "dev":"node index.js" ----> convert -----> "dev":"nodemon index.js" --> then run --> npm run dev

// ---------------------------------------------------------------
//     .env
// ---------------------------------------------------------------

// .env file ka use secret aur configuration values store karne ke liye hota hai, jaise:
// es ko install karne ke liye ---->    npm install dotenv


// PORT=5000
// MONGO_URI=mongodb://localhost:27017/mydatabase
// JWT_SECRET=mySuperSecretKey
// NODE_ENV=development
// CLOUDINARY_API_KEY=your_api_key
// CLOUDINARY_API_SECRET=your_api_secret


//--> jis file me es ko use karna ho    import dotenv from "dotenv";
                                      //dotenv.config();    ye dono import karna hai es ki help se ham ko (process.env)
// ye milta hai.