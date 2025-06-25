import React, { useEffect, useState } from "react";
import FanPost from "../components/FanPost";
import FanPostForm from "../components/FanPostForm";

function FanFeedPage() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("/fanposts")
      .then((res) => res.json())
      .then(setPosts);
  }, []);

  function handleAddPost(newPost) {
    setPosts([newPost, ...posts]);
  }

  return (
    <div>
      <h2>Fan Feed</h2>
      <FanPostForm onAddPost={handleAddPost} />
      {posts.map((post) => <FanPost key={post.id} post={post} />)}
    </div>
  );
}

export default FanFeedPage;
