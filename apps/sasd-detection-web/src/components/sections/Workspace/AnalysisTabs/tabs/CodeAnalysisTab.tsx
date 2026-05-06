export default function CodeAnalysisTab({ data }) {
    return (
        <div>
            <h3>Code Comments Analysis</h3>
            <div>
                { data.map((file, index) => (
                    <button
                        key={index}
                        onClick={null}
                    >
                        { file.file_path }
                    </button>
                ))}
            </div>
        </div>
    );
}
