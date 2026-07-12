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

// let arr = [];
// // let i=0;
// // let j = 0;
// let size = Number(prompt("Enter the size of array elemets  : "));

// for(let i=0;i<size;i++){
//     arr[i]=Number(prompt("Enter the elemets of arrays  : "));
// }

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

// let i=0;
// let j = size - 1;
// while(i!=j){
//     let temp=arr[i];
//     arr[i]=arr[j];
//     arr[j]=temp;
//     i++;
//     j--;
// }
// console.log(arr);



// -------------------------------------------------------------------
//        Revers array
// -------------------------------------------------------------------

// let arr = [];
// let size = Number(prompt("Enter the size of arraya : "));
// for(let i=0;i<size;i++){
//     arr[i]=Number(prompt("Enter the element of array : "));
// }
// for(let i=size-1;i>=0;i--){
//     console.log(arr[i]);   
// }

// second method

// let arr = []
// let size = prompt("Enter the size of array : ")
// for(let i=0;i<size;i++){
//     arr[i]=Number(prompt("Enter the elements of array : "))
// }

// for(let i=size;i>=0;i--){
//     console.log(arr[i]);
    
// }

// -------------------------------------------------------------------
//        change the last postion
// -------------------------------------------------------------------
// output - [1,2,3,4,5] to [2,3,4,5,1]

// let arr = [1,2,3,4,5]
// let first = arr.shift()
// arr.push(first)
// console.log(arr);

// or

// let arr = [1, 2, 3, 4, 5]; // ak array ban liya hai
// let first = arr[0];	// index zero ke element ko first me store kar diya hai
// for (let i = 0; i < arr.length - 1; i++) {
//     arr[i] = arr[i + 1];	// index arr[0] par index 1 ki value aa jaye
// }
// arr[arr.length - 1] = first;
// console.log(arr);


// -------------------------------------------------------------------
//        change the last postion
// -------------------------------------------------------------------

let arr = [1,2,3,4,5]
let result = arr.shift()
let result02=arr.pop()
arr.push(result)
arr.unshift(result02)
console.log(arr);









