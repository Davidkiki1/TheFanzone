import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import TeamsPage from "./pages/TeamsPage";
import PlayersPage from "./pages/PlayersPage";
import PlayerDetailPage from "./pages/PlayerDetailPage";
import TeamDetailPage from "./pages/TeamDetailPage";
import FanFeedPage from "./pages/FanFeedPage"

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/teams" element={<TeamsPage />} />
        <Route path="/teams/:id" element={<TeamDetailPage />} />
        <Route path="/players" element={<PlayersPage />} />
        <Route path="/players/:id" element={<PlayerDetailPage />} />
        <Route path="/fanfeed" element={<FanFeedPage />} />
      </Routes>
    </Router>
  );
}

export default App;