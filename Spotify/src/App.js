import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import WrappedForm from "./components/WrappedForm";
import WrappedResults from "./components/WrappedResults";

function App() {
  const [token, setToken] = useState(null);
  const [wrappedData, setWrappedData] = useState(null);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login setToken={setToken} />} />
        <Route path="/form" element={<WrappedForm token={token} setWrappedData={setWrappedData} />} />
        <Route path="/results" element={<WrappedResults data={wrappedData} />} />
      </Routes>
    </Router>
  );
}

export default App;
