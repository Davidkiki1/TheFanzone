import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

function SignupForm({ onSignup }) {
  const formik = useFormik({
    initialValues: {
      username: "",
      password: "",
    },
    validationSchema: Yup.object({
      username: Yup.string()
        .min(3, "Username must be at least 3 characters")
        .required("Username is required"),
      password: Yup.string()
        .min(6, "Password must be at least 6 characters")
        .required("Password is required"),
    }),
    onSubmit: (values, { resetForm, setSubmitting }) => {
      fetch("http://localhost:5555/auth/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(values),
      })
        .then((r) => {
          if (!r.ok) throw new Error("Signup failed");
          return r.json();
        })
        .then((data) => {
          if (onSignup) onSignup(data.username);
          alert("Signup successful!");
          resetForm();
        })
        .catch(() => {
          alert("Signup failed. Username might already exist.");
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
        {formik.isSubmitting ? "Signing up..." : "Sign Up"}
      </button>
    </form>
  );
}

export default SignupForm;