import React from "react";
import { useFormik } from "formik";

function FanPostForm({ onAddPost }) {
  const formik = useFormik({
    initialValues: { content: "" },
    validate: (values) => {
      const errors = {};
      if (!values.content) errors.content = "Post cannot be empty";
      return errors;
    },
    onSubmit: (values, { resetForm }) => {
      fetch("/fanposts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(values),
      })
        .then((res) => res.json())
        .then((newPost) => {
          onAddPost(newPost);
          resetForm();
        });
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <textarea
        name="content"
        value={formik.values.content}
        onChange={formik.handleChange}
        placeholder="Share your thoughts..."
        style={{ width: "100%", height: "80px" }}
      />
      {formik.errors.content && <p style={{ color: "red" }}>{formik.errors.content}</p>}
      <button type="submit">Post</button>
    </form>
  );
}

export default FanPostForm;
