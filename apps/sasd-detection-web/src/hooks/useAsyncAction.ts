import { useState } from "react";
import toast from "react-hot-toast";

export default function useAsyncAction() {
    const [isLoading, setIsLoading] = useState(false);

    async function run(action: () => Promise<void>, fallbackMessage: string) {
        setIsLoading(true);
        try {
            await action();
        }
        catch (err) {
            const message = err instanceof Error ? err.message : fallbackMessage;
            toast.error(message);
        }
        finally {
            setIsLoading(false);
        }
    }

    return { isLoading, run };
}
