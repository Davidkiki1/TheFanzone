import React from "react";
import { useAuth } from "../context/AuthContext";

function FanPost({ post, onEdit, onDelete }) {
  const { user } = useAuth();
  const isOwner = user?.id === post.user?.id;

  return (
    <div style={{ border: "1px solid #aaa", padding: "1rem", marginBottom: "1rem" }}>
      <h4>{post.user?.username || "Unknown User"}</h4>
      <p>{post.content}</p>
      <p style={{ fontSize: "0.8rem", color: "gray" }}>
        {new Date(post.timestamp).toLocaleString()}
      </p>
      {isOwner && (
        <div style={{ marginTop: "0.5rem" }}>
          <button onClick={() => onEdit(post)}>Edit</button>{" "}
          <button onClick={() => onDelete(post.id)}>Delete</button>
        </div>
      )}
    </div>
  );
}

export default FanPost;
