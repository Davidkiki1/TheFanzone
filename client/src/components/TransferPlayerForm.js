import React, { useState, useEffect } from "react";

function TransferPlayerForm({ player, onClose }) {
  const [teams, setTeams] = useState([]);
  const [selectedTeamId, setSelectedTeamId] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5555/teams")
      .then((res) => res.json())
      .then(setTeams);
  }, []);

  function handleTransfer() {
    fetch(`http://localhost:5555/players/${player.id}/transfer`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ team_id: selectedTeamId }),
    })
      .then((res) => res.json())
      .then(() => {
        alert("Player transferred!");
        onClose();
      })
      .catch(() => alert("Transfer failed"));
  }

  return (
    <div>
      <h4>Transfer {player.name}</h4>
      <select onChange={(e) => setSelectedTeamId(e.target.value)} defaultValue="">
        <option value="" disabled>
          Select team
        </option>
        {teams.map((team) => (
          <option key={team.id} value={team.id}>
            {team.name}
          </option>
        ))}
      </select>
      <button onClick={handleTransfer} disabled={!selectedTeamId}>
        Confirm Transfer
      </button>
      <button onClick={onClose}>Cancel</button>
    </div>
  );
}

export default TransferPlayerForm;
