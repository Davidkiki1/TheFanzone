import React, { useEffect, useState } from "react";
import EditPlayerForm from "./EditPlayerForm";
import TransferPlayerForm from "./TransferPlayerForm";

function PlayerManager() {
  const [players, setPlayers] = useState([]);
  const [editingPlayer, setEditingPlayer] = useState(null);
  const [transferPlayer, setTransferPlayer] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5555/players")
      .then((res) => res.json())
      .then(setPlayers);
  }, []);

  return (
    <div>
      <h3>Manage Players</h3>
      {editingPlayer && <EditPlayerForm player={editingPlayer} onClose={() => setEditingPlayer(null)} />}
      {transferPlayer && <TransferPlayerForm player={transferPlayer} onClose={() => setTransferPlayer(null)} />}
      <ul>
        {players.map((p) => (
          <li key={p.id}>
            {p.name} ({p.position})
            <button onClick={() => setEditingPlayer(p)}>Edit</button>
            <button onClick={() => setTransferPlayer(p)}>Transfer</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PlayerManager;