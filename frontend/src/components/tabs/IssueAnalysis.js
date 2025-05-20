import React from "react";

const IssueAnalysis = ({ data }) => {
  return (
    <div className="issue-analysis">
      <h3>Issue Tracker Analysis</h3>
      {data.map((issue, index) => (
        <div key={index} className="issue-item">
          <p>
            <strong>Message:</strong> {issue.message}
          </p>
          <p>
            <strong>SASD Detected:</strong> {issue.sasd_detected ? "Yes" : "No"}
          </p>
          <p>
            <strong>Details:</strong> {issue.details}
          </p>
        </div>
      ))}
    </div>
  );
};

export default IssueAnalysis;
