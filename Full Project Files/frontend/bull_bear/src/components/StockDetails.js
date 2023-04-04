import React, {useState, useEffect} from 'react';
import NavBar from './NavBar';
import "../styles/StockDetails.css";
import axios from 'axios';

function StockDetails() {

  const [stocks,setStocks] = useState([])


  
  useEffect(()=>{
    async function getstock() {
      try {
        const stocks = await axios.get('http://localhost:8000/stockcard/')
        console.log(stocks.data)
        setStocks(stocks.data)
      } catch (error) {
        console.log(error)
        
      }
    } getstock();
  },[])





  return (
    <>
    <div className='nav'>
        <NavBar/>
    </div>
    <div className="card-container">
      
      {stocks.map((stock) => (
        <div className="card" key={stock.name}>
          <div className="card-content">
            <h2>{stock.name}</h2>
            <p>Purchased Price: {stock.price}</p>
            <p>Holdings: {stock.q}</p>
          </div>
        </div>
      ))}
    </div>
    </>
  )
}

export default StockDetails