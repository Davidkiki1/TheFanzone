import React, { useEffect, useState } from "react";
import TeamCard from "../components/TeamCard";
import SearchBar from "../components/SearchBar";

function TeamsPage() {
  const [teams, setTeams] = useState([]);
  const [filteredTeams, setFilteredTeams] = useState([]);

  useEffect(() => {
    fetch("/teams")
      .then((res) => res.json())
      .then((data) => {
        setTeams(data);
        setFilteredTeams(data);
      });
  }, []);

  function handleSearch(term) {
    const results = teams.filter((team) =>
      team.name.toLowerCase().includes(term.toLowerCase())
    );
    setFilteredTeams(results);
  }

  return (
    <div>
      <h2>All Teams</h2>
      <SearchBar onSearch={handleSearch} />
      <div style={{ display: "flex", flexWrap: "wrap", gap: "1rem" }}>
        {filteredTeams.map((team) => (
          <TeamCard key={team.id} team={team} />
        ))}
      </div>
    </div>
  );
}

export default TeamsPage;
