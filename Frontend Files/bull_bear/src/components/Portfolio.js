import React, {useState, useEffect}from "react";
import Navbar from "./NavBar";
import axios from 'axios';
import "../styles/Portfolio.css";
import { Link } from 'react-router-dom';

function Portfolio() {

    
    const [stocks, setStocks] = useState([]);
    const [price, setPrice] = useState([]);
    const [userdata, setUserdata] = useState([]);

    useEffect(()=>{
        async function getportfolio(){
            try {
                const userdata = await axios.get('http://localhost:8000/portfoliodata/')
                console.log(userdata.data)
                setUserdata(userdata.data)
                
            } catch (error) {
                console.log(error)
            }
        } getportfolio();

        async function getstock(){
            try {
                const stocks = await axios.get('http://localhost:8000/stockcard/')
                console.log(stocks.data)
                setStocks(stocks.data)
                
            } catch (error) {
                console.log(error)
            }
        } getstock();

        async function getprice(){
            try {
                const price = await axios.get('http://localhost:8000/watchlist/')
                console.log(price.data)
                setPrice(price.data)
                
            } catch (error) {
                console.log(error)
            }
        } getprice();
    
        
    },[])

    var balance = 0;
    let q =0
    stocks.map((stock,i)=>{
        balance = balance+ parseFloat(stock.q) * parseFloat(stock.price)
        q = q + parseFloat(stock.q)

    })

    

    var profit=0;
    
    for (let index = 0; index < stocks.length; index++) {
        for (let i =0; i<price.length;i++){
            if (stocks[index].name == price[i].name) {
                profit = profit+(parseFloat(stocks[index].q)* parseFloat(price[i].cprice))
            }
        }
        
    }

    let numberClass = '';

  if (profit > 0) {
    numberClass = 'green';
  } else if (profit < 0) {
    numberClass = 'red';
  }
    

    return(
        <>
        <div className="Portfolio">
            <Navbar/>
        </div>
        <div className="portfolio">
            {
                userdata.map((user,i)=>{ return(
                    
                    <ul className="userheading">
                        <h1>{user.name}'s Portfolio</h1>
                        <p>Username: {user.username}</p>
                        <p>Age: {user.age}</p>
                        <p className={numberClass}>Profit: Rs. {profit-balance}</p>
                        <p>Invested Price: Rs. {profit}</p>
                        <p>Balance: Rs. {user.balance - balance}</p>
                        <p>Stocks Quantity Holding:{q} </p>
                    </ul>
                )
                })
            }
            
            {/* <h2>Stocks</h2>
            <ul>
                {stocks.map(stock => (
                <li key={stock.symbol}>
                    <p>{stock.name} ({stock.symbol})</p>
                    <p>Quantity: {stock.quantity}</p>
                </li>
                ))} */}
            {/* </ul> */}

            <Link to="http://localhost:3000/stockdetails" className="portfolio-button-link">
      <button>Check your Owned Stock Details here...</button>
      </Link>
    </div>
    
        </>
    );
}

export default Portfolio;