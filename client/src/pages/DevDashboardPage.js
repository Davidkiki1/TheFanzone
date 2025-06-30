// src/pages/DevDashboardPage.js
import React from "react";
import { useAuth } from "../context/AuthContext";
import TeamManager from "../components/TeamManager";       // ✅ Main team interface
import PlayerManager from "../components/PlayerManager";   // ✅ Player editor/transfer

function DevDashboardPage() {
  const { user } = useAuth();

  if (!user?.is_admin) return <p style={{ color: "red" }}>Access denied.</p>;

  return (
    <div style={{ padding: "1rem" }}>
      <h2>Developer Dashboard</h2>
      <p>Here you can add/edit teams, update player stats, and transfer players.</p>

      <hr />

      <TeamManager />

      <hr />

      <PlayerManager />
    </div>
  );
}

export default DevDashboardPage;
