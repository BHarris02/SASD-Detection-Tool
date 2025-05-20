import React from "react";

const CommitAnalysis = ({ data }) => {

  return (
    <div className="commit-analysis">
      <h3>Commit Message Analysis</h3>
      {data.map((commit, index) => (
        <div key={index} className="commit-item">
          <p>
            <strong>Message:</strong> {commit.message}
          </p>
          <p>
            <strong>SASD Detected:</strong> {commit.sasd_detected ? "Yes" : "No"}
          </p>
          <p>
            <strong>Details:</strong> {commit.details}
          </p>
        </div>
      ))}
    </div>
  );
};

export default CommitAnalysis;
