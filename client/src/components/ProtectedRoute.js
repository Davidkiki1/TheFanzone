import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function ProtectedRoute({ children, devOnly = false }) {
  const { user } = useAuth();

  if (!user) {
    alert("You must be logged in to access this page.");
    return <Navigate to="/login" replace />;
  }

  if (devOnly && !user.is_admin) {
    alert("You must be a developer to access this page.");
    return <Navigate to="/" replace />;
  }

  return children;
}

export default ProtectedRoute;
