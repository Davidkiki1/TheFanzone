import React from "react";
import { NavLink } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function NavBar() {
  const { user, logout } = useAuth();

  const linkStyle = {
    margin: "0 10px",
    textDecoration: "none",
    fontWeight: "bold",
    color: "#f4f4f4",
  };

  const accentLink = {
    ...linkStyle,
    color: "var(--color-accent)",
  };

  return (
    <nav style={{ 
      display: "flex", 
      justifyContent: "space-between", 
      alignItems: "center", 
      padding: "10px 20px", 
      background: "rgba(15, 22, 30, 0.8)", 
      backdropFilter: "blur(10px)", 
      borderRadius: "12px" 
    }}>
      <div>
        <NavLink to="/" style={linkStyle}>Home</NavLink>
        <NavLink to="/teams" style={linkStyle}>Teams</NavLink>
        <NavLink to="/players" style={linkStyle}>Players</NavLink>
        <NavLink to="/fanfeed" style={linkStyle}>Fan Feed</NavLink>

        {user?.is_dev && (
          <NavLink to="/dev" style={accentLink}>Dev Dashboard</NavLink>
        )}

        {!user && (
          <>
            <NavLink to="/signup" style={linkStyle}>Sign Up</NavLink>
            <NavLink to="/dev-login" style={accentLink}>Dev Login</NavLink>
          </>
        )}
      </div>

      <div>
        {user ? (
          <>
            <span style={{ fontWeight: "bold", color: "#00ff94" }}>
              Welcome, {user.username}!
            </span>
            <button 
              onClick={logout} 
              style={{
                marginLeft: "10px",
                padding: "6px 12px",
                border: "none",
                borderRadius: "6px",
                background: "linear-gradient(to right, var(--color-primary), var(--color-secondary))",
                color: "#0a192f",
                fontWeight: "bold",
                cursor: "pointer",
                boxShadow: "0 4px 10px rgba(0, 255, 148, 0.3)"
              }}
            >
              Logout
            </button>
          </>
        ) : (
          <NavLink to="/login" style={linkStyle}>Login</NavLink>
        )}
      </div>
    </nav>
  );
}

export default NavBar;
