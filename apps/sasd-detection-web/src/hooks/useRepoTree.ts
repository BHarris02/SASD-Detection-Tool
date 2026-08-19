import { fetchRepoTree } from "@/api/fetchRepoTree";
import type { RepoNode } from "@/types/repo";
import { parseOwnerRepo } from "@/utils/parseOwnerRepo";
import { useState } from "react";
import useAsyncAction from "./useAsyncAction";

export default function useRepoTree() {
    const [repoInput, setRepoInput] = useState("");
    const [fileTree, setFileTree] = useState<RepoNode[] | null>(null);
    const { isLoading, run } = useAsyncAction();

    async function onLoadRepo(ownerRepo: string) {
        await run(async () => {
            const { owner, repo } = parseOwnerRepo(ownerRepo);
            setFileTree(await fetchRepoTree(owner, repo));
        }, "Failed to load repository");
    }

    return {
        repoInput,
        setRepoInput,
        fileTree,
        isLoading,
        onLoadRepo
    }
}
