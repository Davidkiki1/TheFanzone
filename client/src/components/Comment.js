import React from "react";

function Comment({ comment }) {
  return (
    <div style={{ marginBottom: "0.5rem", padding: "0.5rem", borderBottom: "1px solid #ddd" }}>
      <p><strong>{comment.user?.username || "Unknown User"}:</strong> {comment.content}</p>
    </div>
  );
}

export default Comment;
