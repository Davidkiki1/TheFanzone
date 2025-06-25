import React, { useEffect, useState } from "react";
import TeamCard from "../components/TeamCard";

function TeamsPage() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch("/teams")
      .then((res) => res.json())
      .then(setTeams);
  }, []);

  return (
    <div>
      <h2>All Teams</h2>
      <div style={{ display: "flex", flexWrap: "wrap", gap: "1rem" }}>
        {teams.map((team) => (
          <TeamCard key={team.id} team={team} />
        ))}
      </div>
    </div>
  );
}

export default TeamsPage;