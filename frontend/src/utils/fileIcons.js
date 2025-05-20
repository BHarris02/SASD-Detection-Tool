import { FaFolder, FaFileAlt } from "react-icons/fa";
import { SiJavascript, SiPython, SiJson } from "react-icons/si";

export const getFileIcon = (filename) => {
    if (!filename || typeof filename !== "string") {
        return <FaFileAlt />;
    }
    if (filename.endsWith(".js")) return <SiJavascript style={{ color: "#f1e5a" }} />;
    if (filename.endsWith(".py")) return <SiPython style={{ color: "#3572a5" }} />;
    if (filename.endsWith(".json")) return <SiJson style={{ color: "#cbcb41" }} />;
    return <FaFileAlt />;
};

export const folderIcon = <FaFolder style={{ color: "#4caf50" }} />;
