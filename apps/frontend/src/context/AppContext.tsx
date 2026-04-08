import { createContext, useContext, useState } from "react";

interface AppContextType {
    fileViewerContent: string;
    setFileViewerContent: (content: string) => void;
}

const AppContext = createContext<AppContextType | null>(null);

export function AppContextProvider({ children }: { children: React.ReactNode }) {
    const [fileViewerContent, setFileViewerContent] = useState<string>("");

    return (
        <AppContext.Provider value={{ fileViewerContent, setFileViewerContent }}>
            { children }
        </AppContext.Provider>
    );
}

export function useApp() {
    const context = useContext(AppContext);
    if (!context)
        throw new Error("useApp must be used within an AppContextProvider");
    return context;
}