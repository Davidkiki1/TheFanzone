import React from "react";
import { NavLink } from "react-router-dom";

function NavBar() {
  const linkStyle = {
    margin: "0 10px",
    textDecoration: "none",
    fontWeight: "bold",
  };

  return (
    <nav>
      <NavLink to="/teams" style={linkStyle}>Teams</NavLink>
      <NavLink to="/players" style={linkStyle}>Players</NavLink>
      <NavLink to="/fanfeed" style={linkStyle}>Fan Feed</NavLink>
    </nav>
  );
}

export default NavBar;