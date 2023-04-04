import React , {useState, useEffect} from 'react'
import axios from 'axios';

import logo from "../images/Bullbear logo.png"
import "../styles/Searchbar.css"
import Candlestick from './Candlestick';



// import HistoricalData from "/Users/lordvoldemort/django_react/second_attempt/data/historicaldata.csv"
// import {Line} from 'react-chartjs-2'
// import { LineController, LinearScale, CategoryScale, CandlestickController, Chart } from 'chart.js';

// Chart.register(LineController, LinearScale, CategoryScale, CandlestickController);


function Searchbar() {

  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("/data.json");
      const data = await response.json();
      setData(data);
    };

    fetchData();
  }, []);

  
  function showTickerData(event){
        axios.get('http://127.0.0.1:8000/ticker/')
        .then((res)=>{
            console.log(res.data)
            this.setState({Ticker:res.data})
        })
  } showTickerData();

  function handleSignUpClick() {
    window.location.href = '/signup';
  }

  function handleLoginClick() {
    window.location.href = '/login';
  }

  const [searchText, setSearchText] = useState('');

  const handleInputChange = (e) => {
    setSearchText(e.target.value);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    
    // Perform search or other action here
            if({searchText}){
                let formfield= new FormData()
                formfield.append('ticker_name', searchText)
                axios.post('http://127.0.0.1:8000/ticker/', formfield)
                .then((response)=>{
                    console.log(`Search submitted: ${searchText}`);
                    console.log(response.data);
                })
                .catch((error)=>{
                    console.log(error)
                })
            
        }
  };

  return (
    <>
    <div className='navbar'>
      <div className="navbar-left">
        <div className="navbar-logo">
          <img src={logo} alt="Company Logo"/>
        </div>
        <a href="/" class="navbar-title">Bulls and Bears</a>
      </div>
      <div className="navbar-right">
        <button class="navbar-button" onClick={handleSignUpClick}>Sign Up</button>
        <button class="navbar-button" onClick={handleLoginClick}>Sign In</button>
      </div>
    </div>
    <div className='history'>
    <h3 className='heading'>Check the Historical Data Analysis here</h3>
    <div className='formticker'>
    <form className="search-bar" onSubmit={handleFormSubmit}>
      <input type="text" value={searchText} onChange={handleInputChange} placeholder="Search..." />
      <button type="submit">Search</button>
    </form>
    </div>
    <div className='graph'>
    {/* <h1>{searchText} Candlestick Chart</h1>
      {data.length > 0 ? (
        <Candlestick data={data} width={800} ratio={2} />
      ) : (
        <p>Loading chart data...</p>
      )} */}
    </div>
    </div>
    </>
  )
}

export default Searchbar