import { createContext, useState, useContext, useEffect } from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = (userObj) => setUser(userObj);

  const logout = () => {
    fetch("http://localhost:5555/auth/logout", {
      method: "POST",
      credentials: "include", // ✅ send session cookie to backend
    }).finally(() => setUser(null)); // Clear local state no matter what
  };

  // 🔁 Run once on app load: check session
  useEffect(() => {
    fetch("http://localhost:5555/auth/check_session", {
      credentials: "include", // ✅ include cookie so Flask can see session
    })
      .then((res) => {
        if (res.ok) return res.json();
        throw new Error("Not logged in");
      })
      .then((userData) => login(userData)) // ✅ store full user object
      .catch(() => logout()); // Clear session if invalid
  }, []);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
