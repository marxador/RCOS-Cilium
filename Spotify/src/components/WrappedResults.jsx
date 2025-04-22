import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

const WrappedResults = ({ data }) => {
  if (!data) return <p>Loading...</p>;

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4">
        Your Wrapped for {data.month}/{data.year}
      </h2>
      <ul className="mb-6">
        {data.top_tracks.map((track, idx) => (
          <li key={idx}>
            {track.name} — {track.artist}
          </li>
        ))}
      </ul>
      <BarChart width={500} height={300} data={data.top_tracks}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="popularity" fill="#82ca9d" />
      </BarChart>
    </div>
  );
};

export default WrappedResults;
