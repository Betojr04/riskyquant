import React from "react";
import "../styles/navbar.css";

export const Navbar = () => {
  return (
    <nav className="nav-container">
      <div className="nav-logo">RiskyQuant</div>
      <div className="nav-links">
        <a href="/">Home</a>
        <a href="/random">Random</a>
      </div>
    </nav>
  );
};
