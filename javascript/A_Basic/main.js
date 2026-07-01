// let a = 10;
// let b = 20;
// let c = 30;
// console.log(`Sum of given ${a} and ${b} : `  +a+b+c);
// Math.floor ki help se ham point ke baad ki value ko hata sakte hai
// Math.round ye 5 se niche point ki value hogi to usi value ko dega 5 se uper koi value
// hogi to ak bad kar dega,exampl:-
// console.log(Math.round(4.9));  output :- 5
//console.log(Math.round(4.3));   output :- 4
//Math.ceil ka matlab hai ki tum ak point ki value laga do ham us ko khud uper kar degei,
//exmaple :- console.log(math.ceil(10.1));  output:- 11

// ---------------------------------------------------------
//              Topic - Type coercion
// ---------------------------------------------------------
// javaScript engine by default "1" ko 1 me convert kar dega console.log(1-1)
// console.log("1"-1);


// ---------------------------------------------------------
//              Topic - taking input from the user
// ---------------------------------------------------------

// dynamically value user dalta hai 
// Static value developer set karta hai 
// prompt() -> ye ak function hota hai or jo bhi data ye leta hai bo by defalut string leta hai

// abhi ye bydefalut string hai
// Example:-
// let age = prompt("Enter the age : ");
// console.log(typeof(age));

// ab es ko number me convert karte hai
// Example:-
// let age = prompt("Enter the age : ");
// age = Number(age)
// console.log(age);

// agar ham console me Number("ali") likh kar enter mare to ouput NaN hoga

// ---------------------------------------------------------
//              Topic - type castng
// ---------------------------------------------------------
// ak data type ko dusre data type me change karna type castng khate hai, es ke pass me do type ki casting hoti hai

// i -> implicit :- js apne app data type change karta hai
//Example :-      
            //let result = "10" + 5;// yha par js ne 5 ko automatically string bana diya
            //console.log(result); // output:-  "105"

//Example :- 
            //let result = "10" - 5; // js me 10 ko no me change kar diya
            //console.log(result); // output- 5

// ii-> Explicit :- programmer khud data type change karta hai
// Example:-
        // let str = "25";
        // let num = Number(str);
        // console.log(num);      // 25
        // console.log(typeof num); // number

// Example:-       Number → String

            // let num = 100;
            // let str = String(num);
            // console.log(str);       // "100"
            // console.log(typeof str); // string

// ---------------------------------------------------------
//              swap two number
// ---------------------------------------------------------
// method - 01

// let a=10;
// let b=20;
// let temp=0;

// temp=a;
// a=b;
// b=temp;

// console.log("A : " +a);
// console.log("B : " +b);

// method - 02

// let a=10;
// let b=20;

// a = a+b; //-> a=10+20 = 30, a=30
// b = a-b; //-> b = 30-20 = 10, b=10
// a = a-b; //-> a = 30-10 = 20, a=20

// console.log("a :  " +a);
// console.log("b : " +b);

// method - 03
// let a=10;
// let b=20;

// [a,b] = [b,a]
// console.log(a,b);















