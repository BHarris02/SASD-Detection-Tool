import { useState } from "react";
import useAsyncAction from "./useAsyncAction";
import { parseOwnerRepo } from "@/utils/parseOwnerRepo";
import { fetchFileContent } from "@/api/fetchFileContent";

export default function useFileSelection() {
    const [filePath, setFilePath] = useState<string | null>(null);
    const [fileContent, setFileContent] = useState<string | null>(null);
    const [loadedRepo, setLoadedRepo] = useState<string | null>(null);
    const { isLoading, run } = useAsyncAction();

    async function onLoadFile(ownerRepo: string, path: string) {
        if (path === filePath && ownerRepo === loadedRepo) {
            return;
        }

        await run(async () => {
            const { owner, repo } = parseOwnerRepo(ownerRepo);
            setFileContent(await fetchFileContent(owner, repo, path));
            setFilePath(path);
            setLoadedRepo(ownerRepo);
        }, "Failed to fetch file");
    }

    return {
        fileContent,
        isLoading,
        onLoadFile
    }
}
