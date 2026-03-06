import { Link } from "react-router-dom";
import "../styles/navbar.css";

function Navbar() {

  return (
    <nav className="navbar">

      <h2 className="logo">SkillSync AI</h2>

      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact">Contact</Link>
      </div>

    </nav>
  );
}

export default Navbar;