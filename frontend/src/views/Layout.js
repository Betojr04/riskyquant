import React from "react";
import { BrowserRouter as Routes, Route } from "react-router-dom";
import ScrollToTop from "../components/scrollToTop";
import injectContext from "../store/appContext";

// imports
import { Navbar } from "../components/Navbar";
import { Footer } from "../components/Footer";
import { Home } from "./Home";

const Layout = () => {
  return (
    <div>
      <BrowserRouter>
        <ScrollToTop>
          <Navbar />
          <Routes>
            <Route element={<Home />} path="/" />
          </Routes>
          <Footer />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
