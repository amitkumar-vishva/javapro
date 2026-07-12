let num=Number(prompt("Enter the amount of bijli will : "));
let mul = 1;
if(num>0 && num<=100){
    mul=num*4;
    console.log("Your bijli will : " +mul);   
}
else if(num>=101 && num<=200){
    mul=num*6;
    console.log("Your bijli will : " +mul); 
}
else if(num>=201 && num<=400){
    mul=num*8;
    console.log("Your bijli will : " +mul); 
}
else if(num>=401){
    mul=num*13;
    console.log("Your bijli will : " +mul); 
}