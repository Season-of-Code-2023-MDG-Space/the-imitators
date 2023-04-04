import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFacebook, faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';
import "../styles/Footer.css";

function Footer() {
    return (
        <footer className="footer">
            <div className="container">
                <div className="row">
                    <div className="col-lg-3 col-md-6">
                        <h3>About Us</h3>
                        <p> At Bulls and Bears Company, we're passionate about helping you achieve your financial goals.
                            Our expert team offers cutting-edge trading technology, personalized advice, and unbeatable
                            customer service to help you succeed in the stock market.</p>
                    </div>
                    <div className="col-lg-3 col-md-6">
                        <h3>Contact Us</h3>
                        <ul className="list-unstyled">
                            <li><a href="#">Address</a></li>
                            <li><a href="#">Phone</a></li>
                            <li><a href="#">Email</a></li>
                        </ul>
                    </div>
                    <div className="col-lg-3 col-md-6">
                        <h3>Follow Us</h3>
                        <ul className="list-unstyled">
                            <li><a href="#"><FontAwesomeIcon icon={faFacebook} /></a></li>
                            <li><a href="#"><FontAwesomeIcon icon={faTwitter} /></a></li>
                            <li><a href="#"><FontAwesomeIcon icon={faInstagram} /></a></li>
                        </ul>
                    </div>
                    <div className="col-lg-3 col-md-6">
                        <h3>Copyright</h3>
                        <p>&copy; 2023 Bulls and Bears Company. All Rights Reserved.</p>
                    </div>
                </div>
            </div>
        </footer>
    );
}

export default Footer;
