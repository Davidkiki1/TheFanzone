import React, { useState } from "react";

function EditPlayerForm({ player, onClose }) {
  const [formData, setFormData] = useState({ ...player });

  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch(`http://localhost:5555/players/${player.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify(formData),
    })
      .then((res) => res.json())
      .then(() => {
        alert("Player updated!");
        onClose();
      })
      .catch(() => alert("Failed to update player"));
  }

  return (
    <form onSubmit={handleSubmit}>
      <h4>Edit Player: {player.name}</h4>
      <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" /><br />
      <input name="position" value={formData.position} onChange={handleChange} placeholder="Position" /><br />
      <input name="goals" value={formData.goals} onChange={handleChange} placeholder="Goals" /><br />
      <input name="assists" value={formData.assists} onChange={handleChange} placeholder="Assists" /><br />
      <input name="appearances" value={formData.appearances} onChange={handleChange} placeholder="Appearances" /><br />
      <button type="submit">Save</button>
      <button type="button" onClick={onClose}>Cancel</button>
    </form>
  );
}

export default EditPlayerForm;