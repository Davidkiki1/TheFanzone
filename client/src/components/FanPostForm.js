import React from "react";
import { useFormik } from "formik";
import { useAuth } from "../context/AuthContext";

function FanPostForm({ onAddPost }) {
  const { user } = useAuth();

  const formik = useFormik({
    initialValues: { content: "" },
    validate: (values) => {
      const errors = {};
      if (!values.content.trim()) {
        errors.content = "Post cannot be empty";
      }
      return errors;
    },
    onSubmit: (values, { resetForm, setSubmitting }) => {
      const trimmedContent = values.content.trim();

      if (!trimmedContent) {
        alert("Post cannot be empty.");
        setSubmitting(false);
        return;
      }

      fetch("http://localhost:5555/fanposts/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        credentials: "include", // ✅ important for session auth
        body: JSON.stringify({
          content: trimmedContent  // ✅ matches backend
        }),
      })
        .then(async (res) => {
          if (!res.ok) {
            const err = await res.json().catch(() => ({}));
            throw new Error(err.error || "Failed to post");
          }
          return res.json();
        })
        .then((newPost) => {
          onAddPost(newPost);
          resetForm();
        })
        .catch((err) => {
          console.error("Fan post error:", err);
          alert(err.message || "Something went wrong.");
        })
        .finally(() => setSubmitting(false));
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
      <button type="submit" disabled={formik.isSubmitting}>
        {formik.isSubmitting ? "Posting..." : "Post"}
      </button>
    </form>
  );
}

export default FanPostForm;
