import React from 'react'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import ReactDOM from 'react-dom/client'
import Login from './pages/Login.jsx'
import NotFoundPage from './pages/NotFoundPage.jsx'
import App from './App.jsx'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Login />,
    errorElement: <NotFoundPage />
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
