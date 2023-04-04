import React, {useState, useEffect}from "react";
import "../styles/Watchlist.css";
import Navbar from "./NavBar";
import axios from 'axios';
import { Link } from 'react-router-dom';
import BuyButton from "./Buy";



function Watchlist() {

    const [name, setSearchTerm] = useState('');
    const [stockdata, setStockdata] = useState([]);
    const [isloading, setIsLoading] = useState(false);
    const [logindata, setLoginData] = useState([]);

  useEffect(()=>{
    async function getlogin() {
      try {
        const logindata = await axios.get('http://localhost:8000/login/')
        console.log(logindata.data[logindata.data.length -1])
        setLoginData(logindata.data[logindata.data.length -1])
      } catch (error) {
        console.log(error)
        
      }
    } getlogin();
  },[])

    useEffect(()=>{
        async function getallstock(){
            try {
                setIsLoading(true);
                const stockdata = await axios.get('http://localhost:8000/watchlist/')
                console.log(stockdata.data)
                setStockdata(stockdata.data)
            } catch (error) {
                console.log(error)
            } finally {
                setIsLoading(false);
            }
        } getallstock();
        if(!stockdata){
            return(<p>Prices are shown in their respective country's currency.</p>)
        }
        const interval = setInterval(()=>{
            getallstock();
        },12000);
        return()=> clearInterval(interval);
    },[])
    

    function handleInputChange(event) {
        setSearchTerm(event.target.value);
      }
    
      function handleSearch(event) {
        event.preventDefault();
        let formfield = new FormData()
        formfield.append('name',name)
        // TODO: Perform search using searchTerm
        axios.post('http://localhost:8000/watchlist/',formfield)
        console.log(`Performing search for "${name}"...`);
      }

      

    return(
        <>
        <div className="bground">
        <div className="watchlist">
            <Navbar/>
        </div>
        
        <div className="entryticker">
      <form onSubmit={handleSearch}>
        <input type="text" placeholder="Search..." value={name} onChange={handleInputChange} />
        <button type="submit">Search</button>
      </form>
    </div>
    <div className="watchlist">

        {
        stockdata.map((stock,i)=>{
            return(
                <h3>{stock.name} Price:{stock.cprice} <BuyButton username = {logindata.username} ticker={stock.name} price= {stock.cprice} /></h3> 
            )
        })

         }
        
    
    </div>
    <div>
    <Link to="http://127.0.0.1:8050" className="button-link">
      <button>Check your Real Time Data Analysis of Stocks here...</button>
      </Link>
      <Link to="/prediction" className="button-link">
      <button>Check our price predictions of Stocks here...</button>
    </Link>
    </div>

    </div>
        </>
    );
}

export default Watchlist;