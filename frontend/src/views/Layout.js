import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// store imports
import InjectContext from "../store/appContext";
// componenet imports
import ScrollToTop from "../components/scrollToTop";
import { Navbar } from "../components/Navbar";
import { Footer } from "../components/Footer";
import { Home } from "./Home";
import { Random } from "../components/Random";

const Layout = () => {
  return (
    <div>
      <BrowserRouter>
        <ScrollToTop>
          <Navbar />
          <Routes>
            <Route element={<Home />} path="/" />
            <Route element={<Random />} path="/random" />
          </Routes>
          <Footer />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default InjectContext(Layout);
