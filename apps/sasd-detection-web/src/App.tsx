import './App.css';
import Navbar from './components/layout/Navbar';
import RepoTree from './components/sections/RepoTree';

export default function App() {
  return (
    <>
    <header>
      <Navbar />
    </header>

    <main>
      <RepoTree />
    </main>
    </>
  )
}
