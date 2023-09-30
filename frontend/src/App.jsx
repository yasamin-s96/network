import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './index.css'
import Register from './pages/Register'
import ForgotPassword from './pages/ForgotPassword'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFoundPage from './pages/NotFoundPage'
import Profile from './pages/Profile'

function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/forgot-password' element={<ForgotPassword />} />
          <Route path='/page-not-found' element={<NotFoundPage />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
          <Route path='/profile' element={<Login />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
