import React from "react";
import { useNavigate } from "react-router-dom";
const Server = () => {
  const navigate = useNavigate()
  return (
    <div className="home-container">
      <h1>Welcome to Server Page</h1>

      <div className="btns">
        <button onClick={()=>navigate('/')}>Home</button>
        <button onClick={()=>navigate('/about')}>About</button>
        <button onClick={()=>navigate('/contact')}>Contact</button>
      </div>
    </div>
  );
};

export default Server;