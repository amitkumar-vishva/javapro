// import React from "react";
// import {Route, Routes} from "react-router-dom";
// import Home from './pages/Home'
// import About from './pages/About'
// import Server from './pages/Server'
// import Contact from './pages/Contact'
// const App = () =>{
//   return(
//     <div>
//       <Routes>
//         <Route path="/" element={<Home/>}/>
//         <Route path="/about" element={<About/>}/>
//         <Route path="/server" element={<Server/>}/>
//         <Route path="/contact" element={<Contact/>}/>
//       </Routes>
//     </div>
//   )
// }
// export default App;


import React from "react";
import { Routes, Route, Link } from "react-router-dom";

import Home from "./pages/Home";
import About from "./pages/About";
import Server from "./pages/Server";
import Contact from "./pages/Contact";

const App = () => {
  return (
    <div>
      {/* Navigation */}
      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/about">About</Link> |{" "}
        <Link to="/server">Server</Link> |{" "}
        <Link to="/contact">Contact</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/server" element={<Server />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </div>
  );
};

export default App;