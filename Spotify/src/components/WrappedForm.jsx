import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import axios from "axios";

const WrappedForm = ({ token, setWrappedData }) => {
  const [month, setMonth] = useState("");
  const [year, setYear] = useState("");
  const navigate = useNavigate();
  const location = useLocation();

  const urlToken = new URLSearchParams(location.search).get("token");

  const accessToken = token || urlToken;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post("http://localhost:5000/wrapped", {
      token: accessToken,
      month,
      year,
    });
    setWrappedData(response.data);
    navigate("/results");
  };

  return (
    <form onSubmit={handleSubmit} className="p-6 space-y-4">
      <h2 className="text-xl font-bold">Choose a Month and Year</h2>
      <input
        type="number"
        min="1"
        max="12"
        placeholder="Month (1-12)"
        value={month}
        onChange={(e) => setMonth(e.target.value)}
        className="border p-2 rounded w-full"
      />
      <input
        type="number"
        placeholder="Year (e.g., 2024)"
        value={year}
        onChange={(e) => setYear(e.target.value)}
        className="border p-2 rounded w-full"
      />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
        Get My Wrapped
      </button>
    </form>
  );
};

export default WrappedForm;
