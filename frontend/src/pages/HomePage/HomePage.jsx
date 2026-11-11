import { Link } from "react-router-dom";
import "./HomePage.css";

export default function HomePage() {
  return (
    <section className="home">
      <img src="/logo.png" alt="" className="home-logo" />
      <h1 className="home-title">Synthetic Data Generator</h1>
      <p>
        Generate fake datasets for testing, demos and prototyping.</p>
        <p>Pick a pre-defined template, choose the subcategories you need, and export the result as CSV or JSON.</p>
      <Link to="/generate" className="btn btn-primary home-cta">
        Get started
      </Link>
    </section>
  );
}
