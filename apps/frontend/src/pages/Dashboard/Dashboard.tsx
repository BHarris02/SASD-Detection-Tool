import LoadingSpinner from "@/components/ui/LoadingSpinner";
import RepoInput from "@/components/sections/RepoInput";
import { useState } from "react";
import RepoFileTree from "@/components/sections/RepoFileTree";
import Tab from "@/components/ui/Tab";
import FileViewer from "@/components/ui/FileViewer";
import BackendActions from "@/components/sections/BackendActions";
import Modal from "@/components/ui/Modal";

export default function Dashboard() {
    const [loading, setLoading] = useState(true);

    return (
        <div className="dashboard">
            <LoadingSpinner loading={loading} />

            <h1>Self-Admitted Security Debt Detection Tool: Web</h1>

            <RepoInput />
            <RepoFileTree />

            <div>
                <Tab />
                <FileViewer />
            </div>

            <BackendActions />
            <Modal />
        </div>
    )
}