import "./PageHeader.css";

export default function PageHeader({ title, subtitle }) {
  return (
    <header className="page-header">
      <h1 className="page-title">{title}</h1>
      {subtitle && <p className="page-subtitle">{subtitle}</p>}
    </header>
  );
}
