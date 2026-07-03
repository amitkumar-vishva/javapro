import React from "react";
import { useEffect } from "react";
import { useState } from "react";
const Usestate = () =>{

    const [count, setCount] = useState(0)

    const increment = () =>{
        setCount(count+1)
    }
    useEffect(()=>{
        console.log("useEffect hooks es runing.......");
        
    })
    return(
        <div>
            <div>{count}</div>
            <button onClick={()=>setCount(count-1)}>decrement</button>
            <button onClick={increment}>Increment</button>
        </div>
    )
}
export default Usestate;