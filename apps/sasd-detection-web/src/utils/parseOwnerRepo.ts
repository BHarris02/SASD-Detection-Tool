export function parseOwnerRepo(ownerRepo: string): {owner: string, repo: string} {
    const parts = ownerRepo.trim().split("/").filter(Boolean);

    if (parts.length !== 2) {
        throw new Error("Repository must be in the format: 'owner/repository'");
    }

    const [owner, repo] = parts;
    return { owner, repo };
}
