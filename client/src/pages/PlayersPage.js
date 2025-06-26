import React, { useEffect, useState } from "react";
import PlayerCard from "../components/PlayerCard";
import SearchBar from "../components/SearchBar";

function PlayersPage() {
  const [players, setPlayers] = useState([]);
  const [filteredPlayers, setFilteredPlayers] = useState([]);

  useEffect(() => {
    fetch("/players")
      .then((res) => res.json())
      .then((data) => {
        setPlayers(data);
        setFilteredPlayers(data);
      });
  }, []);

  function handleSearch(term) {
    const results = players.filter((player) =>
      player.name.toLowerCase().includes(term.toLowerCase())
    );
    setFilteredPlayers(results);
  }

  return (
    <div>
      <h2>All Players</h2>
      <SearchBar onSearch={handleSearch} />
      <div style={{ display: "flex", flexWrap: "wrap", gap: "1rem" }}>
        {filteredPlayers.map((player) => (
          <PlayerCard key={player.id} player={player} />
        ))}
      </div>
    </div>
  );
}

export default PlayersPage;
