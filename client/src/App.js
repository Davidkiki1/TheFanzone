import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import SignupPage from "./pages/SignupPage";
import TeamsPage from "./pages/TeamsPage";
import PlayersPage from "./pages/PlayersPage";
import PlayerDetailPage from "./pages/PlayerDetailPage";
import TeamDetailPage from "./pages/TeamDetailPage";
import FanFeedPage from "./pages/FanFeedPage";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import DevLoginPage from "./pages/DevLoginPage"; // ✅ Added
import DevDashboardPage from "./pages/DevDashboardPage"; // ✅ Added
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route path="/teams" element={<TeamsPage />} />
        <Route path="/teams/:id" element={<TeamDetailPage />} />
        <Route path="/players" element={<PlayersPage />} />
        <Route path="/players/:id" element={<PlayerDetailPage />} />
        <Route
          path="/fanfeed"
          element={
            <ProtectedRoute>
              <FanFeedPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/dev"
          element={
            <ProtectedRoute devOnly={true}>
              <DevDashboardPage />
            </ProtectedRoute>
          }
        />
        <Route path="/dev-login" element={<DevLoginPage />} /> {/* ✅ Dev login route */}
      </Routes>
    </Router>
  );
}

export default App;
