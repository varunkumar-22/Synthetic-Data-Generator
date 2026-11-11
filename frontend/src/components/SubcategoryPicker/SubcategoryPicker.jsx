import "./SubcategoryPicker.css";

export default function SubcategoryPicker({ options, selected, onToggle }) {
  if (!options) {
    return <p className="muted">Select a template to see its subcategories.</p>;
  }

  return (
    <div className="chips">
      {options.map((sub) => (
        <button
          key={sub}
          type="button"
          className={selected.includes(sub) ? "chip chip-selected" : "chip"}
          onClick={() => onToggle(sub)}
        >
          {sub}
        </button>
      ))}
    </div>
  );
}
