import { Link, NavLink } from "react-router-dom";
import "./Sidebar.css";

const NAV_ITEMS = [
  { to: "/generate", label: "Generate" },
  { to: "/templates", label: "Templates" },
  { to: "/docs", label: "Docs" },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <Link to="/" className="sidebar-brand">
        Synthetic Data
      </Link>
      <nav className="sidebar-nav">
        {NAV_ITEMS.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) => (isActive ? "sidebar-link sidebar-link-active" : "sidebar-link")}
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
