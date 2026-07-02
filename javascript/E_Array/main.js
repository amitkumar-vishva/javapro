// -------------------------------------------------------------------
//         Aary me 5 elements stor ko fir print karo
// -------------------------------------------------------------------
// let arr = new Array(5);
// for(let i=0;i<arr.length;i++){
//     arr[i]=Number(prompt("Enter the elemets : "));
// }
// // console.log(typeof(arr));
// // console.log(arr);


// -------------------------------------------------------------------
//         taking input size from the user
// -------------------------------------------------------------------

// let arr = [];
// let size = Number(prompt("Enter the size of array : "))
// for(let i=0;i<size;i++){
//     arr[i] = Number(prompt("Enter the array elements : "));
// }
// console.log(arr);

// -------------------------------------------------------------------
//         sum of the array elemets
// -------------------------------------------------------------------

// let arr = [];
// let sum=0;
// let size = Number(prompt("Enter the size of array : "))
// for(let i=0;i<size;i++){
//     arr[i] = Number(prompt("Enter the array elements : "));
//     sum+=arr[i];
// }
// console.log(sum);

// -------------------------------------------------------------------
//         find the largest number
// -------------------------------------------------------------------

// let arr = [];
// let size = Number(prompt("Enter the size of array : "))
// for(let i=0;i<size;i++){
//     arr[i] = Number(prompt("Enter the array elements : "));
// }
// let max = arr[0];
// for(let i=0;i<size;i++){
//     if(arr[i]>max){
//         max=arr[i];
//     }
// }
// console.log(max);


// -------------------------------------------------------------------
//         find the second largest number
// -------------------------------------------------------------------

// let arr = [];
// let size = Number(prompt("Enter the size of array : "))
// for(let i=0;i<size;i++){
//     // Array ke andar element ko input le raha hu
//     arr[i] = Number(prompt("Enter the array elements : "));
// }

// let Firstmax = arr[0];
// let Secondmax = arr[0];
// for(let i=0;i<size;i++){
//     if(arr[i]>Firstmax){
//         Firstmax=arr[i];
//     }
//     else if(arr[i]>Secondmax){
//         Secondmax=arr[i];
//     }
// }
// console.log("First largest no : " +Firstmax);
// console.log("Second largest no : " +Secondmax);

// -------------------------------------------------------------------
//         find the second largest number
// -------------------------------------------------------------------

let arr = [];
// let i=0;
// let j = 0;
let size = Number(prompt("Enter the size of array elemets  : "));

for(let i=0;i<size;i++){
    arr[i]=Number(prompt("Enter the elemets of arrays  : "));
}

// arr.reverse();
// console.log(arr);

// optional

// for(let i=size-1;i>=0;i--){
//     console.log(arr[i]);    
// }

// optional
// for(let i=size-1;i>=0;i--){
//     temp[j] = arr[i];
//     j++;
// }
// console.log(temp);

// optional

let i=0;
let j = size - 1;
while(i!=j){
    let temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
    i++;
    j--;
}
console.log(arr);




