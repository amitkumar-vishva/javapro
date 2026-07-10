import React from "react";
import { useNavigate } from "react-router-dom";
const Home = () => {
  const navigate = useNavigate()
  return (
    <div className="home-container">
      <h1>Welcome to Home Page</h1>

      <div className="btns">
        <button onClick={()=>navigate('/about')}>About</button>
        <button onClick={()=>navigate('/server')}>Server</button>
        <button onClick={()=>navigate('/contact')}>Contact</button>
      </div>
    </div>
  );
};

export default Home;