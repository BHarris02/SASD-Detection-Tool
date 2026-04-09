import { useAppContext } from "@/context/AppContext"
import { useState } from "react";

export default function useWorkspace() {
    // state
    // FileViewer
    const { fileViewerContent } = useAppContext();
    const [selectedCode, setSelectedCode] = useState<string>("");

    // handlers

    return {
        // FileViewer
        fileViewerContent,
        setSelectedCode
    }
}