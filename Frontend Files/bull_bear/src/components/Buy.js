import { useState, useEffect } from 'react';
import '../styles/Buy.css';
import axios from 'axios';



function BuyButton(props) {
  const [quantity, setQuantity] = useState(1);
  // const [id, setId] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [message, setMessage] = useState('');
  

  const handleBuy = () => {
    // Handle buy logic with quantity
    let formfield = new FormData()
    formfield.append("username",props.username)
    formfield.append("name",props.ticker)
    formfield.append("q",quantity)
    formfield.append("price",props.price)
    axios.post('http://localhost:8000/buy/',formfield)
    .then((res)=>{
      console.log(`Buying ${quantity} items of ${props.ticker}.`);
      
      
      
    })
    
     // Hide message after 3 seconds
    // Hide the modal
    setShowModal(false);
    setMessage('Button clicked!');
      setTimeout(() => {
      setMessage('');
    }, 3000);
  };

  const handleQuantityChange = (event) => {
    setQuantity(parseInt(event.target.value));
  };

  return (
    <div>
      <button className="buy-button" onClick={() => setShowModal(true)}>
        Buy
      </button>
      {showModal && (
        <div className="modal">
          <div className="modal-content">
            <div className="modal-header">
              <h2>How many items do you want to buy?</h2>
              <button onClick={() => setShowModal(false)}>X</button>
            </div>
            <div className="modal-body">
              <label htmlFor="quantity">Quantity:</label>
              <input type="text"
              value = {props.ticker}
               />
              <input
                type="number"
                id="quantity"
                value={quantity}
                onChange={handleQuantityChange}
              />
            </div>
            <div className="modal-footer">
              <button className="buy-button" onClick={handleBuy}>
                Buy {quantity}
              </button>
              <button onClick={() => setShowModal(false)}>Cancel</button>
              {message && <p className="flash-message">{message}</p>}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default BuyButton;
