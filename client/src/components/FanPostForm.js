import React from "react";
import { useFormik } from "formik";

function FanPostForm({ onAddPost, user }) {
  const formik = useFormik({
    initialValues: { content: "" },
    validate: (values) => {
      const errors = {};
      if (!values.content) errors.content = "Post cannot be empty";
      return errors;
    },
    onSubmit: (values, { resetForm }) => {
      if (!user) {
        alert("You must be logged in to post.");
        return;
      }

      fetch("/fanposts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // important for sessions
        body: JSON.stringify({
          content: values.content,
        }),
      })
        .then((res) => res.json())
        .then((newPost) => {
          onAddPost(newPost);
          resetForm();
        });
    },
  });

  if (!user) {
    return <p style={{ color: "red" }}>Please log in to share a post.</p>;
  }

  return (
    <form onSubmit={formik.handleSubmit}>
      <textarea
        name="content"
        value={formik.values.content}
        onChange={formik.handleChange}
        placeholder="Share your thoughts..."
        style={{ width: "100%", height: "80px" }}
      />
      {formik.errors.content && (
        <p style={{ color: "red" }}>{formik.errors.content}</p>
      )}
      <button type="submit">Post</button>
    </form>
  );
}

export default FanPostForm;
