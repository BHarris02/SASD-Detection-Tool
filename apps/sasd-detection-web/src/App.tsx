import { Toaster } from 'react-hot-toast';
import './App.css';
import Navbar from './components/layout/Navbar';
import AnalysisPanel from './components/sections/AnalysisPanel';
import RepoTree from './components/sections/RepoTree';
import useRepoTree from './hooks/useRepoTree';
import useFileSelection from './hooks/useFileSelection';

export default function App() {
  const { repoInput, setRepoInput, fileTree, isLoading, onLoadRepo } = useRepoTree();
  const { fileContent, onLoadFile } = useFileSelection();

  return (
    <>
    <Toaster />
    <header>
      <Navbar />
    </header>

    <main>
      <RepoTree
        repoInput={repoInput}
        onRepoInputChange={setRepoInput}
        fileTree={fileTree}
        isLoading={isLoading}
        onLoadRepo={() => onLoadRepo(repoInput)}
        onFileSelect={(path) => onLoadFile(repoInput, path)}
      />
      <AnalysisPanel fileContent={fileContent}/>
    </main>
    </>
  )
}
