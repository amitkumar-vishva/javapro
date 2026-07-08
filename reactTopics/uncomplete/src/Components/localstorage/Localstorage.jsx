import React from "react";
const Localstorage = () =>{

    // object store karene ke liye
    const user = {
        name:'suman',
        age:21,
        city:'delhi'
    };
    localStorage.setItem('user',JSON.stringify(user))

    // object se data lene ke liye
    let result = JSON.parse(localStorage.getItem('user'))
    console.log(result);
    console.log(result.name);
     
  return(
   <div>Local-Storage</div>
  )
}
export default Localstorage;