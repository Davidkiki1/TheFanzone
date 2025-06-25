import React from "react";

function PlayerStats({ player }) {
  return (
    <div>
      <h2>{player.name}</h2>
      <p>Position: {player.position}</p>
      <p>Goals: {player.goals}</p>
      <p>Assists: {player.assists}</p>
      <p>Appearances: {player.appearances}</p>
    </div>
  );
}

export default PlayerStats;
