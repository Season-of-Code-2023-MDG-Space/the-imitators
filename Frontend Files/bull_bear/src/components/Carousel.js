import Carousel from 'react-bootstrap/Carousel';
import Carousel1 from "../images/Carousel1.jpg";
import Carousel2 from "../images/Carousel2.jpg";
import Carousel3 from "../images/Carousel3.jpg";
import "../styles/Carousel.css";

function CarouselFadeExample() {
    return (
        <Carousel fade>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={Carousel1}
                    alt="First slide"
                />
                <Carousel.Caption>
                    <p className="firstp">A tool for transferring money from the impatient to the patient.</p>
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={Carousel2}
                    alt="Second slide"
                />

                <Carousel.Caption>
                    <p className="secondp">Be Bullish on the Future and Bearish on the Past !</p>
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={Carousel3}
                    alt="Third slide"
                />

                <Carousel.Caption>
                    <p className="thirdp">
                        Risk hai toh Ishq hai !
                    </p>
                </Carousel.Caption>
            </Carousel.Item>
        </Carousel>
    );
}

export default CarouselFadeExample;