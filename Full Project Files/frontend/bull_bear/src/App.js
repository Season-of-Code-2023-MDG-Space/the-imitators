import React from 'react';
// import './App.css';
import axios from 'axios'

import NavBar from './components/NavBar';
import Carousel from './components/Carousel';
import Footer from './components/Footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import {Routes, Route} from "react-router-dom";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";
import Watchlist from "./components/Watchlist";
import Portfolio from "./components/Portfolio";
import News from "./components/News";
import Searchbar from "./components/Searchbar";
import Navigationbar from './components/NavigationBar';
import Prediction from './components/Prediction';
import StockDetails from './components/StockDetails';
import BuyButton from './components/Buy';

function App() {
    return (
        <div className="App">
            <Routes>
                <Route exact path ="/" element={<> <Navigationbar/> <Carousel /> <Footer /> </>}  />
                <Route exact path ="/signup" element={<Signup/>} />
                <Route exact path ="/login" element={<Login/>} />
                <Route exact path="/dashboard" element={<Dashboard/>} />
                <Route exact path ="/dashboard/watchlist" element={<Watchlist/>} />
                <Route exact path ="/dashboard/portfolio" element={<Portfolio/>} />
                <Route exact path ="/dashboard/news" element={<News/>} />
                <Route exact path ="/search/:ticker" element={<Searchbar/> } />
                <Route exact path ="/prediction" element = {<Prediction/>} />
                <Route exact path ="/stockdetails" element = {<StockDetails/>} />
                <Route exact path ="/buy" element={<BuyButton/>} />
            </Routes>
        </div>
    );
}

export default App;
