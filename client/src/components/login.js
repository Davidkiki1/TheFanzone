import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

function LoginForm({ onLogin }) {
  const formik = useFormik({
    initialValues: {
      username: "",
      password: "",
    },
    validationSchema: Yup.object({
      username: Yup.string().required("Username is required"),
      password: Yup.string().required("Password is required"),
    }),
    onSubmit: (values, { setSubmitting, resetForm }) => {
      fetch("http://localhost:5555/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include", // ✅ Enables session cookie
        body: JSON.stringify(values),
      })
        .then((r) => {
          if (!r.ok) throw new Error("Login failed");
          return r.json();
        })
        .then(() => {
          // ✅ Now verify the session and get full user data
          return fetch("http://localhost:5555/auth/check_session", {
            method: "GET",
            credentials: "include", // ✅ Required for session
          });
        })
        .then((r) => {
          if (!r.ok) throw new Error("Session check failed");
          return r.json();
        })
        .then((userData) => {
          if (onLogin) onLogin(userData);
          alert("Login successful!");
          resetForm();
        })
        .catch(() => {
          alert("Login failed. Check your username and password.");
        })
        .finally(() => setSubmitting(false));
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <input
        name="username"
        type="text"
        placeholder="Username"
        onChange={formik.handleChange}
        value={formik.values.username}
      />
      {formik.errors.username && formik.touched.username && (
        <div className="error">{formik.errors.username}</div>
      )}

      <input
        name="password"
        type="password"
        placeholder="Password"
        onChange={formik.handleChange}
        value={formik.values.password}
      />
      {formik.errors.password && formik.touched.password && (
        <div className="error">{formik.errors.password}</div>
      )}

      <button type="submit" disabled={formik.isSubmitting}>
        {formik.isSubmitting ? "Logging in..." : "Login"}
      </button>
    </form>
  );
}

export default LoginForm;
