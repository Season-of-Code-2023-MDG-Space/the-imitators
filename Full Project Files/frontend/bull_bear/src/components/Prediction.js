import React, {useState,useEffect} from 'react';
import NavBar from './NavBar'
import axios from 'axios';

function Prediction() {

  const [name, setSearchTerm] = useState('');
  const [stockdata, setStockdata] = useState([])

  useEffect(()=>{
      async function getallstock(){
          try {
              const stockdata = await axios.get('http://localhost:8000/prediction/')
              console.log(stockdata.data)
              setStockdata(stockdata.data)
          } catch (error) {
              console.log(error)
          }
      } getallstock();
      const interval = setInterval(()=>{
          getallstock();
      },300000);
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
      axios.post('http://localhost:8000/prediction/',formfield)
      console.log(`Performing search for "${name}"...`);
    }


  return (
    <>
    <div><NavBar/></div>
    <div className="entryticker">
      <form onSubmit={handleSearch}>
        <input type="text" placeholder="Search..." value={name} onChange={handleInputChange} />
        <button type="submit">Search</button>
      </form>
    </div>
    </>

  )
}

export default Prediction