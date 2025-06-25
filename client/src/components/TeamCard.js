import React from "react";
import { Link } from "react-router-dom";

function TeamCard({ team }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem", borderRadius: "8px", width: "200px" }}>
      <img src={team.logo_url} alt={team.name} style={{ width: "100%", height: "100px", objectFit: "contain" }} />
      <h3>{team.name}</h3>
      <p>{team.country}</p>
      <Link to={`/teams/${team.id}`}>View Details</Link>
    </div>
  );
}

export default TeamCard;