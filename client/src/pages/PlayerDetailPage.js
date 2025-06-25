import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import PlayerStats from "../components/PlayerStats";
import Comment from "../components/Comment";

function PlayerDetailPage() {
  const { id } = useParams();
  const [player, setPlayer] = useState(null);
  const [comments, setComments] = useState([]);

  useEffect(() => {
    fetch(`/players/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setPlayer(data.player);
        setComments(data.comments);
      });
  }, [id]);

  if (!player) return <p>Loading player...</p>;

  return (
    <div>
      <PlayerStats player={player} />
      <h3>Comments</h3>
      {comments.map((c) => <Comment key={c.id} comment={c} />)}
    </div>
  );
}

export default PlayerDetailPage;
