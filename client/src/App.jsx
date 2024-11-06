import { useState } from "react";
import reactLogo from "./assets/react.svg";
import LoginPage from "./pages/LoginPage";
import viteLogo from "/vite.svg";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import RegisterPage from "./pages/RegisterPage";
import Dashboard from "./pages/Dashboard";
import Landing from "./components/Landing/Landing";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/landing" element={<Landing />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
