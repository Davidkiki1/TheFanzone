import React from "react";
import { NavLink } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function NavBar() {
  const { user, logout } = useAuth();

  const linkStyle = {
    margin: "0 10px",
    textDecoration: "none",
    fontWeight: "bold",
  };

  return (
    <nav style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "10px 20px" }}>
      <div>
        <img src="/Fanzone.png" alt="Fanzone logo" style={{ height: "40px" }} />
        <NavLink to="/" style={linkStyle}>Home</NavLink>
        <NavLink to="/teams" style={linkStyle}>Teams</NavLink>
        <NavLink to="/players" style={linkStyle}>Players</NavLink>
        <NavLink to="/fanfeed" style={linkStyle}>Fan Feed</NavLink>
        {!user && <NavLink to="/signup" style={linkStyle}>Sign Up</NavLink>}
      </div>

      <div>
        {user ? (
          <>
            <span style={{ fontWeight: "bold" }}>Welcome, {user.username}!</span>
            <button onClick={logout} style={{ marginLeft: "10px" }}>Logout</button>
          </>
        ) : (
          <NavLink to="/login" style={linkStyle}>Login</NavLink>
        )}
      </div>
    </nav>
  );
}

export default NavBar;
