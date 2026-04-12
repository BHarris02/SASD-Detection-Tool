import Tabs from "@/components/ui/Tabs";
import CommitAnalysisTab from "./tabs/CommitAnalysisTab";
import IssueAnalysisTab from "./tabs/IssueAnalysisTabs";
import CodeAnalysisTab from "./tabs/CodeAnalysisTab";

export default function AnalysisTabs({ results }) {
    const tabs = [
        { label: "Commits Analysis", content: <CommitAnalysisTab data={ results.commit_analysis } /> },
        { label: "Issues Analysis", content: <IssueAnalysisTab data={ results.issue_analysis } /> },
        { label: "Code Analysis", content: <CodeAnalysisTab data={ results.code_analysis } /> }
    ];
    return <Tabs tabs={tabs} />;
}