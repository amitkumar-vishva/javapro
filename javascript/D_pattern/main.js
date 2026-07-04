// es ka use ham print karne ke liye karte hai bo bhi cmd me
// process.stdout.write("hello");
// process.stdout.write("world");
// npm i prompt-sync


// ye string leta hai number me convert karne ke liye toString kar use karte hai
// ye line common hai
let prompt = require('prompt-sync')();

// let a = prompt("Enter the number : ");
// process.stdout.write((a).toString());

// ----------------------------------------------------------------
//         Star - 01
// ----------------------------------------------------------------
// let n = prompt("Enter the number : ");
// for(let i=0;i<n;i++){
//    for(let j=0;j<n;j++){
//     process.stdout.write("* ")
//    }
//    process.stdout.write("\n")
// }


// output:-
// * * * * * 
// * * * * * 
// * * * * * 
// * * * * * 
// * * * * * 

// ----------------------------------------------------------------
//         Star - 02
// ----------------------------------------------------------------

// let n=prompt("Enter the number : ");
// for(let i=1;i<=n;i++){
//     for(let j=1;j<=i;j++){
//         process.stdout.write("* ");
//     }
//     process.stdout.write("\n");
// }

// output:-
// * 
// * * 
// * * * 
// * * * * 

// ----------------------------------------------------------------
//         Star - 03
// ----------------------------------------------------------------

// let n=prompt("Enter the elemetns : ");
// for(let i=1;i<=n;i++){
//     for(let j=1;j<=n-i;j++){
//         process.stdout.write("* ");
//     }
//     process.stdout.write("\n");
// }

// or
// let n=prompt("Enter the elemetns : ");
// for(let i=1;i<=n;i++){
//     for(let j=n;j>=i;j--){
//         process.stdout.write("* ");
//     }
//     process.stdout.write("\n");
// }

// output:-
// * * * * * 
// * * * * 
// * * * 
// * * 
// * 

// ----------------------------------------------------------------
//         Star - 04
// ----------------------------------------------------------------

// let n=prompt("Enter the elemetns : ");
// for(let i=1;i<=n;i++){
//     for(let j=1;j<=i;j++){
//         process.stdout.write("* ");
//     }
//     process.stdout.write("\n");
// }
// for(let i=1;i<=n;i++){
//     for(let j=1;j<=n-i;j++){
//         process.stdout.write("* ");
//     }
//     process.stdout.write("\n");
// }

// output:-
// * 
// * * 
// * * * 
// * * * * 
// * * * * * 
// * * * * 
// * * * 
// * * 
// * 

// ----------------------------------------------------------------
//         Star - 05
// ----------------------------------------------------------------

// let n=prompt("Enter the elemetns : ");
// for(let i=1;i<=n;i++){
//     for(let j=n;j>=i;j--){
//         process.stdout.write("   ");
//     }
//     for(let k=1;k<=i;k++){
//         process.stdout.write("*  ");
//     }
//     process.stdout.write("\n");
// }

// output:-
//                *  
//             *  *  
//          *  *  *  
//       *  *  *  *  
//    *  *  *  *  *

// ----------------------------------------------------------------
//         Star - 06
// ----------------------------------------------------------------

// let n=prompt("Enter the elemetns : ");
// for(let i=1;i<=n;i++){
//     for(let j=1;j<=i;j++){
//         process.stdout.write("  ");
//     }
    
//     for(let k=n;k>=i;k--){
//         process.stdout.write("* ");
//     } 
//     process.stdout.write("\n");
// }

// output :-
// * * * * * 
//   * * * * 
//     * * * 
//       * *  
//         *
// ----------------------------------------------------------------
//         Star - 07
// ----------------------------------------------------------------

// let n=prompt("Enter the elemetns : ");
// for(let i=1;i<=n-i+1;i++){
//     for(let j=n;j>=i;j--){
//         process.stdout.write("  ");
//     }
//     for(let k=1;k<=i;k++){
//         process.stdout.write("* ");
//     }
//     process.stdout.write("\n");
// }
// for(let i=1;i<=n;i++){
//     for(let j=1;j<=i;j++){
//         process.stdout.write("  ");
//     }
    
//     for(let k=n;k>=i;k--){
//         process.stdout.write("* ");
//     } 
//     process.stdout.write("\n");
// }

// output:-
//       * 
//     * * 
//   * * * 
//     * * 
//       * 

// ----------------------------------------------------------------
//         Star - 08
// ----------------------------------------------------------------

// let n=prompt("Enter the elemetns : ");
// for(let i=1;i<=n;i++){
//     for(let j=n;j>=i;j--){
//         process.stdout.write("   ");
//     }
//     for(let k=1;k<=i;k++){
//         process.stdout.write("   *  ");
//     }
//     process.stdout.write("\n");
// }


// output:-
//                   *  
//                *     *  
//             *     *     *  
//          *     *     *     *  
//       *     *     *     *     *  




