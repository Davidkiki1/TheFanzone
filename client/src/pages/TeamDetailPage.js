import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import PlayerCard from "../components/PlayerCard";
import Comment from "../components/Comment";

function TeamDetailPage() {
  const { id } = useParams();
  const [team, setTeam] = useState(null);
  const [players, setPlayers] = useState([]);
  const [comments, setComments] = useState([]);

  useEffect(() => {
    fetch(`/teams/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setTeam(data.team);
        setPlayers(data.players);
        setComments(data.comments);
      });
  }, [id]);

  if (!team) return <p>Loading team...</p>;

  return (
    <div>
      <h2>{team.name}</h2>
      <p>{team.country}</p>

      <h3>Players</h3>
      <div style={{ display: "flex", flexWrap: "wrap", gap: "1rem" }}>
        {players.map((player) => <PlayerCard key={player.id} player={player} />)}
      </div>

      <h3>Comments</h3>
      {comments.map((comment) => <Comment key={comment.id} comment={comment} />)}
    </div>
  );
}

export default TeamDetailPage;