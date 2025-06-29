import { createContext, useState, useContext, useEffect } from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  // Store the full user object instead of just the username
  const login = (userObj) => setUser(userObj);
  const logout = () => setUser(null);

  useEffect(() => {
    fetch("/auth/check_session")
      .then((res) => {
        if (res.ok) return res.json();
        throw new Error("Not logged in");
      })
      .then((data) => login(data)) // ✅ Store full user
      .catch(() => logout());
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
