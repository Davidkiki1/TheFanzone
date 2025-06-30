import React, { useState, useEffect } from "react";

function TeamForm({ team = {}, onSuccess }) {
  const [name, setName] = useState("");
  const [country, setCountry] = useState("");
  const [logoUrl, setLogoUrl] = useState("");
  const [yearCreated, setYearCreated] = useState("");
  const [trophies, setTrophies] = useState("");

  useEffect(() => {
    if (team) {
      setName(team.name || "");
      setCountry(team.country || "");
      setLogoUrl(team.logo_url || "");
      setYearCreated(team.year_created || "");
      setTrophies(team.trophies || "");
    }
  }, [team]);

  function handleSubmit(e) {
    e.preventDefault();
    const method = team?.id ? "PATCH" : "POST";
    const url = team?.id
      ? `http://localhost:5555/teams/${team.id}`
      : "http://localhost:5555/teams";

    fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ name, country, logo_url: logoUrl, year_created: yearCreated, trophies }),
    })
      .then((res) => res.json())
      .then(() => {
        alert("Team saved!");
        onSuccess?.();
      })
      .catch(() => alert("Failed to save team"));
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" required /><br />
      <input value={country} onChange={(e) => setCountry(e.target.value)} placeholder="Country" required /><br />
      <input value={logoUrl} onChange={(e) => setLogoUrl(e.target.value)} placeholder="Logo URL" /><br />
      <input value={yearCreated} onChange={(e) => setYearCreated(e.target.value)} placeholder="Year Created" /><br />
      <input value={trophies} onChange={(e) => setTrophies(e.target.value)} placeholder="Trophies" /><br />
      <button type="submit">{team?.id ? "Update Team" : "Add Team"}</button>
    </form>
  );
}

export default TeamForm;