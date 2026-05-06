export default function CommitAnalysisTab({ data }) {
    return (
        <div>
            <h3>Commits Analysis</h3>
            { data.map((analysis, index) => (
                <div key={index}>
                    <p><strong>Message: </strong>{ analysis.message }</p>
                    <p><strong>SASD Detected: </strong>{ analysis.sasd_detected ? "Yes" : "No" }</p>
                    <p><strong>Details: </strong>{ analysis.details }</p>
                </div>
            ))}
        </div>
    );
}
