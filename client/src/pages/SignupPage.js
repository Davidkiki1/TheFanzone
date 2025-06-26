import React from "react";
import { useAuth } from "../context/AuthContext";
import SignupForm from "../components/SignupForm";

function SignupPage() {
  const { login } = useAuth();

  return (
    <div className="signup-container">
      <h2>Sign Up</h2>
      <SignupForm onSignup={login} />
    </div>
  );
}

export default SignupPage;