import { useFormik } from "formik";
import * as Yup from "yup";
import { useAuth } from "../context/AuthContext";

function DevLoginPage() {
  const { login } = useAuth();

  const formik = useFormik({
    initialValues: { username: "", password: "" },
    validationSchema: Yup.object({
      username: Yup.string().required("Username is required"),
      password: Yup.string().required("Password is required"),
    }),
    onSubmit: (values, { setSubmitting, resetForm }) => {
      fetch("http://localhost:5555/auth/dev_login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(values),
      })
        .then((res) => {
          if (!res.ok) throw new Error("Dev login failed");
          return res.json();
        })
        .then((userData) => {
          if (!userData.is_dev) throw new Error("Not authorized as dev");
          login(userData);
          alert("Dev login successful!");
          resetForm();
        })
        .catch(() => {
          alert("Login failed or not authorized as dev.");
        })
        .finally(() => setSubmitting(false));
    },
  });

  return (
    <form onSubmit={formik.handleSubmit} style={{ maxWidth: "400px", margin: "3rem auto" }}>
      <h2 style={{ textAlign: "center", marginBottom: "1rem", color: "var(--color-accent)" }}>Developer Login</h2>
      <input
        name="username"
        type="text"
        onChange={formik.handleChange}
        value={formik.values.username}
        placeholder="Dev Username"
      />
      <input
        name="password"
        type="password"
        onChange={formik.handleChange}
        value={formik.values.password}
        placeholder="Password"
      />
      <button type="submit" disabled={formik.isSubmitting}>
        {formik.isSubmitting ? "Logging in..." : "Dev Login"}
      </button>
    </form>
  );
}

export default DevLoginPage;
