import React, { useEffect, useState } from "react";
import TeamForm from "./EditTeamForm";

function TeamManager() {
  const [teams, setTeams] = useState([]);
  const [editingTeam, setEditingTeam] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5555/teams")
      .then((res) => res.json())
      .then(setTeams);
  }, []);

  function handleDelete(id) {
    if (!window.confirm("Delete this team?")) return;
    fetch(`http://localhost:5555/teams/${id}`, {
      method: "DELETE",
      credentials: "include",
    })
      .then((res) => {
        if (res.ok) setTeams((prev) => prev.filter((t) => t.id !== id));
        else throw new Error("Delete failed");
      })
      .catch((err) => alert("Failed to delete team"));
  }

  function handleUpdate(team) {
    setEditingTeam(team);
  }

  return (
    <div>
      <h3>Manage Teams</h3>
      <TeamForm team={editingTeam} onSuccess={() => setEditingTeam(null)} />
      <ul>
        {teams.map((team) => (
          <li key={team.id}>
            {team.name} - {team.country}
            <button onClick={() => handleUpdate(team)}>Edit</button>
            <button onClick={() => handleDelete(team.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TeamManager;