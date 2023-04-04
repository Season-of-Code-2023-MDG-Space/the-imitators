import React, {useState,useEffect}from "react";
import NavBar from "./NavBar";
import axios from 'axios';
import "../styles/news.css"


function News() {

    const [stockName, setStockName] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    let formfield = new FormData()
    formfield.append("name",stockName)
    formfield.append("sdate",startDate)
    formfield.append("edate",endDate)
    axios.post('http://localhost:8000/news/',formfield)
    .then((res)=>{
        console.log(`Stock name: ${stockName}, Start date: ${startDate}, End date: ${endDate}`);
    })
    
  };



    return(
        <>
        <div className="news">
            <NavBar/>
        </div>
        <form onSubmit={handleSubmit}>
      <label htmlFor="stock-name-input">Stock Name:</label>
      <input type="text" id="stock-name-input" value={stockName} onChange={(e) => setStockName(e.target.value)} />

      <label htmlFor="start-date-input">Start Date:</label>
      <input type="date" id="start-date-input" value={startDate} onChange={(e) => setStartDate(e.target.value)} />

      <label htmlFor="end-date-input">End Date:</label>
      <input type="date" id="end-date-input" value={endDate} onChange={(e) => setEndDate(e.target.value)} />

      <button type="submit">Submit</button>
    </form>
      </>
    );
}

export default News;