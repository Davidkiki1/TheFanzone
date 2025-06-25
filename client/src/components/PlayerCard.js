import React from "react";
import { Link } from "react-router-dom";

function PlayerCard({ player }) {
  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem", borderRadius: "8px", width: "200px" }}>
      <h3>{player.name}</h3>
      <p>Position: {player.position}</p>
      <p>Goals: {player.goals}</p>
      <Link to={`/players/${player.id}`}>View Stats</Link>
    </div>
  );
}

export default PlayerCard;