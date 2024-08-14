import { Routes, Route } from "react-router-dom"
import Home from "./pages/userside/home"
import Category from "./pages/userside/category"
import Product from "./pages/userside/product"
import About from "./pages/userside/about"
import Contact from "./pages/userside/contact"
import Login from "./pages/userside/login"
import Register from "./pages/userside/regiser"
import ErrorPage from "./pages/userside/error"
import Single from "./pages/userside/Single"
import MainPage from "./pages/mainPage";
import AssociatedProduct from "./pages/userside/AssociatedProduct"

function App() {

  return (
    <>
      <Routes>
        <Route path="" element={<MainPage />} >
        <Route index element={<Home />} />
        <Route path="category" element={<Category />} />
        <Route path="product" element={<Product />} />
        <Route path="about" element={<About />} />
        <Route path="contact" element={<Contact />} />
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="single/:id" element={<Single />} />
        <Route path="category/:id" element={<AssociatedProduct />} />
        <Route path="*" element={<ErrorPage />} />
        </Route>
      </Routes>
    </>
  )
}

export default App
