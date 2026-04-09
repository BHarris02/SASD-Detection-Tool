import { createContext, useContext, useState } from "react";

interface AppContextType {
    fileViewerContent: string;
    setFileViewerContent: (content: string) => void;
    repoUrl: string;
    setRepoUrl: (url: string) => void;
    selectedFilePath: string | null;
    setSelectedFilePath: (filePath: string) => void;
}

const AppContext = createContext<AppContextType | null>(null);

export function AppContextProvider({ children }: { children: React.ReactNode }) {
    const [fileViewerContent, setFileViewerContent] = useState<string>("");
    const [repoUrl, setRepoUrl] = useState<string>("");
    const [selectedFilePath, setSelectedFilePath] = useState<string | null>(null);

    return (
        <AppContext.Provider value={{
            fileViewerContent,
            setFileViewerContent,
            repoUrl,
            setRepoUrl,
            selectedFilePath,
            setSelectedFilePath
        }}>
            { children }
        </AppContext.Provider>
    );
}

export function useAppContext() {
    const context = useContext(AppContext);
    if (!context)
        throw new Error("useApp must be used within an AppContextProvider");
    return context;
}