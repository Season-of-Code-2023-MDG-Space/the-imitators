import React, { useRef } from 'react'
import Navbar from "./NavBar";
import "../styles/Dashboard.css";
function Dashboard() {
  
  return (
    <>
    <div className="Dashboard">
            <Navbar/>
    </div>

    <div className='info'>
      <div className='headings'>
      <div className='dashboard-about'>
      <h3>Dashboard: It is to know the global stock prices</h3>
      </div>
      <div className='watchlist-about'>
      <h3>Watchlist: It is to know about the price changes for your own list</h3>
      </div>
      <div className='portfolio-about'>
      <h3>Portfolio: It is to know about your holdings. It is the place to buy and sell stocks virtually.</h3>
      </div>
      </div>
    </div>
    
    </>
    

  )
}

export default Dashboard