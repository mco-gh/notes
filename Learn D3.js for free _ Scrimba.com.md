Learn D3.js for free | Scrimba.com

# Learn D3.js for free

### Become a data visualization wiz in less than an hour

<html>  <head>  <link  rel="stylesheet"  href="index.css">  </head>  <body>  <h1>index.html</h1>  <script  src="index.pack.js">**</script>  </body></html>

1[Introduction to D3.js](https://scrimba.com/p/pb4WsX/c2bB4hN)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 1:53 • 4 days ago

<html>  <head>  <link  rel="stylesheet"  href="index.css">  <title>Learn D3.js</title>  </head>  <body>  <h1>First heading</h1>  <script  src="https://d3js.org/d3.v4.min.js">**</script>  <script  src="index.js">**</script>  </body></html>

2[Selection and Manipulation](https://scrimba.com/p/pb4WsX/cPyLwfm)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 3:33 • 4 days ago
// javascriptvar dataset = [1, 2, 3, 4, 5];
d3.select('body')
.selectAll('p')
.data(dataset)
.enter()

.append('p') // appends paragraph for each data element .text('D3 is awesome!!'); //.text(function(d) { return d; });

3[Data Loading and Binding](https://scrimba.com/p/pb4WsX/cGZNpU7)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 2:05 • 4 days ago

 // javascriptvar dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];var svgWidth = 500, svgHeight = 300, barPadding = 5;var barWidth = (svgWidth / dataset.length);var svg = d3.select('svg')

.attr("width", svgWidth)
.attr("height", svgHeight); var barChart = svg.selectAll("rect")
.data(dataset)
.enter()

4[Creating a simple bar chart](https://scrimba.com/p/pb4WsX/ckV6eHM)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 3:29 • 4 days ago

 // javascriptvar dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];var svgWidth = 500, svgHeight = 300, barPadding = 5;var barWidth = svgWidth / dataset.length;var svg = d3.select('svg')

.attr("width", svgWidth)
.attr("height", svgHeight); var barChart = svg.selectAll("rect")
.data(dataset)
.enter()
.append("rect")
.attr("y", function(d) {

5[Creating labels](https://scrimba.com/p/pb4WsX/cN8NmSm)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 2:04 • 4 days ago

 // javascriptvar dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];var svgWidth = 500, svgHeight = 400, barPadding = 5;var xScale = d3.scaleLinear()

.domain([0, dataset.length])
.range([0, svgWidth]); var yScale = d3.scaleLinear()
.domain([0, d3.max(dataset)])
.range([svgHeight, 0]);var svg = d3.select('svg')

6[Scales](https://scrimba.com/p/pb4WsX/c4WLes8)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 1:51 • 4 days ago

 // javascript  var data= [80, 100, 56, 120, 180, 30, 40, 120, 160];var svgWidth = 500, svgHeight = 300;var svg = d3.select('svg')

.attr("width", svgWidth)
.attr("height", svgHeight);var xScale = d3.scaleLinear()
.domain([0, d3.max(data)])
.range([0, svgWidth]);

7[Axes](https://scrimba.com/p/pb4WsX/c6rwbhr)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 2:20 • 4 days ago
 // javascriptvar svgWidth = 600, svgHeight = 500;var svg = d3.select("svg")
.attr("width", svgWidth)
.attr("height", svgHeight)
.attr("class", "svg-container"); var line = svg.append("line")
.attr("x1", 100)
.attr("x2", 500)
.attr("y1", 50)
.attr("y2", 50)
.attr("stroke", "red")

8[Creating SVG elements](https://scrimba.com/p/pb4WsX/crk4MhJ)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 2:49 • 4 days ago
// javascriptvar data = [

{"platform": "Android", "percentage": 40.11}, {"platform": "Windows", "percentage": 36.69},

{"platform": "iOS", "percentage": 13.06}

];var svgWidth = 500, svgHeight = 300, radius = Math.min(svgWidth, svgHeight) / 2;var svg = d3.select('svg')

.attr("width", svgWidth)
.attr("height", svgHeight); var g = svg.append("g")
.attr("transform", "translate(" + svgWidth / 2 + "," + svgHeight / 2 + ")");

9[Creating a pie chart](https://scrimba.com/p/pb4WsX/cPyPVAr)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 1:18 • 4 days ago

//API to fetch historical data of Bitcoin Price Indexconst api = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-31&end=2018-04-01';/** * Loading data from API when DOM Content has been loaded'. */document.addEventListener("DOMContentLoaded", function(event) {

fetch(api)
.then(function(response) { return response.json(); })
.then(function(data) { var parsedData = parseData(data);
drawChart(parsedData);
})
.catch(function(err) { console.log(err); })

10[Create a line chart](https://scrimba.com/p/pb4WsX/cwmGZCw)
 • [Sohaib Nehal](https://scrimba.com/@sohaibnehal) • 5:14 • 4 days ago

# Learn how to make use of your data like a pro

D3.js is the most popular data visualization library for the web. It allows you to make sense of your data through a powerful API of methods.

**Course content**

Throughout the course you'll learn the most important features of the library while building four different visualizations. You'll be able to play around with the code whenever you want, so that you can be sure that you'll understand how it works.

**What you’ll learn**

- Selection and manipulation
- Data loading
- Labels
- Axes
- Scales
- SVG elements
- Bar charts
- Pie charts
- Line charts

## What people are saying about Scrimba:

## Related courses

[Introduction to HTML](https://scrimba.com/g/ghtml)

[Learn Bootstrap 4 for free](https://scrimba.com/g/gbootstrap4)

[Learn CSS Variables for free](https://scrimba.com/g/gcssvariables)

[Learn Flexbox for free](https://scrimba.com/g/gflexbox)

[Learn CSS Grid for free](https://scrimba.com/g/gR8PTE)
mleft
mright

Scrimba.com is in beta

[Terms](https://github.com/scrimba/community/blob/master/TERMS.md)[FAQ](https://github.com/scrimba/community/blob/master/FAQ.md)[Docs](https://github.com/scrimba/community/blob/master/DOCS.md)[About](https://scrimba.com/about)