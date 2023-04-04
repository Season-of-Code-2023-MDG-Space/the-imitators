// import React from "react";
// // import { ChartCanvas, CandlestickSeries } from "react-stockcharts";
// // import { XAxis, YAxis } from "react-stockcharts/lib/axes";
// // import { discontinuousTimeScaleProvider } from "react-stockcharts/lib/scale";
// // import { fitWidth } from "react-stockcharts/lib/helper";

// const CandlestickChart = ({ data, width, ratio }) => {
//   const xScaleProvider = discontinuousTimeScaleProvider.inputDateAccessor(
//     (d) => new Date(d.date)
//   );
//   const { data: chartData, xScale, yScale } = xScaleProvider(data);

//   return (
//     <ChartCanvas
//       width={width}
//       height={width / ratio}
//       ratio={ratio}
//       margin={{ left: 50, right: 50, top: 10, bottom: 30 }}
//       seriesName="HDFC"
//       data={chartData}
//       xScale={xScale}
//       yScale={yScale}
//       xAccessor={(d) => d.date}
//       displayXAccessor={xScaleProvider.displayDateAccessor}
//     >
//       <XAxis />
//       <YAxis />
//       <CandlestickSeries />
//     </ChartCanvas>
//   );
// };

// export default fitWidth(CandlestickChart);


import React from 'react'

function Candlestick() {
  return (
    <div>Candlestick</div>
  )
}

export default Candlestick