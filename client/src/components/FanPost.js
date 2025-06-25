import React from "react";

function FanPost({ post }) {
  return (
    <div style={{ border: "1px solid #aaa", padding: "1rem", marginBottom: "1rem" }}>
      <h4>{post.user}</h4>
      <p>{post.content}</p>
      <p style={{ fontSize: "0.8rem", color: "gray" }}>{post.timestamp}</p>
    </div>
  );
}