// Defination : - Promise ek object hai jo batata hai ki koi asynchronous operation future me complete hoga ya fail hoga,
// aur complete hone par uska result kya hoga.
// let result = new Promise((resolve, reject) => {
//     console.log("Babbar.........");
   
    
// });


// -----------------------------------------------------------------------
// ye code Asynchronous code ka example hai
// -----------------------------------------------------------------------
// function Myname(){
//     console.log("Hello ji kese ho sare");   
// }

// setTimeout(Myname, 2000);

// -----------------------------------------------------------------------
// me es asynchronous code ko promise ke andar rakhta hu
// -----------------------------------------------------------------------
// let result = new Promise((resolve, reject) => {
//     function Myname(){
//     console.log("Hello ji kese ho sare");   
//     }
//     setTimeout(Myname, 2000);

// });

// -----------------------------------------------------------------------
// yha par me state check kar raha hu
// -----------------------------------------------------------------------
// let result = new Promise((resolve, reject) => {
//     let success = true;
//     if(success){
//         resolve("Promise fullfill")
//     }
//     else{
//         reject("Promise Rejected")
//     }
// });

// result.then((message)=>{
//     console.log("then ka message is " + message);
// }).catch((error)=>{
//     console.log("Error " + error);
// }).finally(()=>{
//     console.log("this is finally ke lliye");
// })

// -----------------------------------------------------------------------
// multiple promise manage karna
// -----------------------------------------------------------------------
// let result01 = new Promise((resolve, reject)=>{
//     setTimeout(resolve, 1000, "First");
// })

// let result02 = new Promise((resolve, reject)=>{
//     setTimeout(resolve, 1000, "second");
// })

// let result03 = new Promise((resolve, reject)=>{
//     setTimeout(reject, 1000, "third");
// })

// Promise.all([result01, result02, result03])
// .then((value)=>{
//     console.log(value); 
// }).catch((error)=>{
//     console.log("error is comming : " + error);
    
// })


// ---------------------------------------------------------------------
//     Topic - Async-await
// ---------------------------------------------------------------------
// Async : - async keyword kisi function ko asynchronous function bana deta hai.
// async function hamesha Promise return karta hai.

// Await :- await keyword sirf async function ke andar use hota hai. Ye Promise ke resolve hone ka wait karta hai aur resolved value return karta hai.


// Fetch Api :- Fetch API JavaScript ka built-in feature hai jo server se data (resources) 
// lane ke liye use hota hai. Ye purane XMLHttpRequest se zyada powerful aur use karne me aasan hai.

// Example :- 

// async function getData() {
//     setTimeout(()=>{
//         console.log("Hello ji kese ho sare.................");
        
//     }, 2000)
// }

// getData()

// Example :-

async function getData() {
    let response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    let data = await response.json();
    console.log(data);
}
getData()


// data ko kese lete hai or kis formate me lete hai

// prepare url / api endpoint -> sync
// await // fetch data -> network call -> async
// process data -> sync


// parse json -> async