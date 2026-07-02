import React from "react";
import './Card.css'
const Card = () =>{
  return(
    <div className="container">
      <div className="top">
        <img src="https://picsum.photos/300/200" alt="image" />
        <button>save</button>
      </div>

      <div className="center">
        <h4>Amazon</h4>
        <h3>Senior UI/UX Designer</h3>
        <div className="btn">
          <button>Part Time</button>
          <button>Senior Level</button>
        </div>
      </div>

      <div className="bottom">
        <div className="rate">
          <h1>$120/hr</h1>
          <p>Mumbi, India</p>
        </div>
        <div className="btn">
          <button>Apply Now</button>
        </div>
      </div>
    </div>
  )
}
export default Card;




































// import React from "react";
// import './Card.css'

// function Card({image,name,discription}) {

//   return (
//     <div className="container">
//             <div className="card">
//                 <img src={image} alt="profile"/>
//                 <h2>{name}</h2>
//                 <p>{discription}</p>
//                 <button>View Profile</button>
//             </div>
//     </div>
//   );
// }

// export default Card;