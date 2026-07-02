import React from "react";
import './CompanyCard.css'
const CompanyCard = ({companuName,image,name,id,role,department,email}) =>{
    return(
        <>
            <div className="container">
                <div className="card">
                    <div className="top-logo"><h1>{companuName}</h1></div>
                    <img src={image} alt="images" />
                    <p>Name : {name}</p>
                    <p>ID : {id}</p>
                    <p>Role : {role}</p>
                    <p>Department : {department} </p>
                    <p>Email : {email}</p>
                </div>
            </div>
        </>
    )
}
export default CompanyCard;