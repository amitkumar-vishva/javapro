import React from "react";
import { useNavigate } from "react-router-dom";
const Contact = () => {
  const navigate = useNavigate()
  return (
    <div className="home-container">
      <h1>Welcome to Contact Page</h1>

      <div className="btns">
        <button onClick={()=>navigate('/')}>Home</button>
        <button onClick={()=>navigate('/server')}>Server</button>
        <button onClick={()=>navigate('/about')}>About</button>
      </div>
    </div>
  );
};

export default Contact;