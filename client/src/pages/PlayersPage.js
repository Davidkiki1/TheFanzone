import React, { useEffect, useState } from "react";
import PlayerCard from "../components/PlayerCard";

function PlayersPage() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    fetch("/players")
      .then((res) => res.json())
      .then(setPlayers);
  }, []);

  return (
    <div>
      <h2>All Players</h2>
      <div style={{ display: "flex", flexWrap: "wrap", gap: "1rem" }}>
        {players.map((player) => (
          <PlayerCard key={player.id} player={player} />
        ))}
      </div>
    </div>
  );
}

export default PlayersPage;
