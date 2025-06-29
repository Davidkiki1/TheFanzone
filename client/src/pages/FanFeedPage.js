import React, { useEffect, useState } from "react";
import FanPost from "../components/FanPost";
import FanPostForm from "../components/FanPostForm";
import { useAuth } from "../context/AuthContext";

function FanFeedPage() {
  const [posts, setPosts] = useState([]);
  const { user } = useAuth();

  useEffect(() => {
    fetch("http://localhost:5555/fanposts/", { credentials: "include" })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch fan posts");
        return res.json();
      })
      .then(setPosts)
      .catch((err) => {
        console.error(err);
        alert("Unable to load fan posts.");
      });
  }, []);

  function handleAddPost(newPost) {
    setPosts((prev) => [newPost, ...prev]);
  }

  function handleEdit(post) {
    const newContent = prompt("Edit your post:", post.content);
    if (!newContent || newContent.trim() === post.content.trim()) return;

    fetch(`http://localhost:5555/fanposts/${post.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ content: newContent.trim() }),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to update post");
        return res.json();
      })
      .then((updatedPost) => {
        setPosts((prev) =>
          prev.map((p) => (p.id === updatedPost.id ? updatedPost : p))
        );
      })
      .catch((err) => {
        console.error(err);
        alert("Failed to update post");
      });
  }

  function handleDelete(postId) {
    if (!window.confirm("Are you sure you want to delete this post?")) return;

    fetch(`http://localhost:5555/fanposts/${postId}`, {
      method: "DELETE",
      credentials: "include",
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to delete post");
        return res.json();
      })
      .then(() => {
        setPosts((prev) => prev.filter((p) => p.id !== postId));
      })
      .catch((err) => {
        console.error(err);
        alert("Failed to delete post");
      });
  }

  return (
    <div>
      <h2>Fan Feed</h2>
      {user ? (
        <FanPostForm onAddPost={handleAddPost} />
      ) : (
        <p style={{ color: "red" }}>Please log in to share a post.</p>
      )}
      {posts.map((post) => (
        <FanPost
          key={post.id}
          post={post}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      ))}
    </div>
  );
}

export default FanFeedPage;
