import React from "react";
const Apicalls = () =>{

    async function getData() {
    
       let response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
       console.log(response);
        
    }


  return(
    <div>
        <button onClick={getData}>Get Data</button>
    </div>
  )
}
export default Apicalls;