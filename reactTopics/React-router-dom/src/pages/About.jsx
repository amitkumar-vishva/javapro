import React from "react";
import { useNavigate } from "react-router-dom";
const About = () => {
  const navigate = useNavigate()
  return (
    <div className="home-container">
      <h1>Welcome to About Page</h1>

      <div className="btns">
        <button onClick={()=>navigate('/')}>Home</button>
        <button onClick={()=>navigate('/server')}>Server</button>
        <button onClick={()=>navigate('/contact')}>Contact</button>
      </div>
    </div>
  );
};

export default About;