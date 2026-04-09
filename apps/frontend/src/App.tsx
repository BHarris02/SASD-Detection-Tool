import './App.css'
import Dashboard from '@/pages/Dashboard';
import Navbar from './components/layout/Navbar';
import { AppContextProvider, useAppContext } from './context/AppContext';
import Modal from './components/ui/Modal';

function AppContent() {
  const { error, setError } = useAppContext();

  return (
    <>
      <Navbar />
      <Dashboard />
      <Modal
        show={!!error}
        onClose={() => setError(null)}
        title="Error"
      >
        <p>{ error }</p>
      </Modal>
    </>
  );
}

export default function App() {
  return (
    <AppContextProvider>
      <AppContent />
    </AppContextProvider>
  )
}
