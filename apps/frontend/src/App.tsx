import './App.css'
import Dashboard from '@/pages/Dashboard';
import Navbar from './components/layout/Navbar';
import { AppContextProvider } from './context/AppContext';

function App() {
  return (
    <AppContextProvider>
      <Navbar />
      <Dashboard />
    </AppContextProvider>
  )
}

export default App
