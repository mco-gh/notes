World Tour

# World Tour

# Antarctica

![](../_resources/34927fd168d5cb2fda025c540e549919.png)

 [Open](https://bl.ocks.org/mbostock/raw/4183330)

See [discussion on Hacker News](http://news.ycombinator.com/item?id=4858817). Built with [D3](http://d3js.org/) and [TopoJSON](https://github.com/mbostock/topojson).

## index.html[#](https://bl.ocks.org/mbostock/4183330#index.html)

	<!DOCTYPE html>
	<meta charset="utf-8">
	<style>

	h1 {
	  position: absolute;
	  top: 500px;
	  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
	  font-size: 18px;
	  text-align: center;
	  width: 960px;
	}

	</style>
	<h1></h1>
	<script src="//d3js.org/d3.v3.min.js"></script>
	<script src="//d3js.org/queue.v1.min.js"></script>
	<script src="//d3js.org/topojson.v1.min.js"></script>
	<script>

	var width = 960,
	    height = 960;

	var projection = d3.geo.orthographic()
	    .translate([width / 2, height / 2])
	    .scale(width / 2 - 20)
	    .clipAngle(90)
	    .precision(0.6);

	var canvas = d3.select("body").append("canvas")
	    .attr("width", width)
	    .attr("height", height);

	var c = canvas.node().getContext("2d");

	var path = d3.geo.path()
	    .projection(projection)
	    .context(c);

	var title = d3.select("h1");

	queue()
	    .defer(d3.json, "/mbostock/raw/4090846/world-110m.json")
	    .defer(d3.tsv, "/mbostock/raw/4090846/world-country-names.tsv")
	    .await(ready);

	function ready(error, world, names) {
	  if (error) throw error;

	  var globe = {type: "Sphere"},
	      land = topojson.feature(world, world.objects.land),
	      countries = topojson.feature(world, world.objects.countries).features,
	      borders = topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }),
	      i = -1,
	      n = countries.length;

	  countries = countries.filter(function(d) {
	    return names.some(function(n) {
	      if (d.id == n.id) return d.name = n.name;
	    });
	  }).sort(function(a, b) {
	    return a.name.localeCompare(b.name);
	  });

	  (function transition() {
	    d3.transition()
	        .duration(1250)
	        .each("start", function() {
	          title.text(countries[i = (i + 1) % n].name);
	        })
	        .tween("rotate", function() {
	          var p = d3.geo.centroid(countries[i]),
	              r = d3.interpolate(projection.rotate(), [-p[0], -p[1]]);
	          return function(t) {
	            projection.rotate(r(t));
	            c.clearRect(0, 0, width, height);
	            c.fillStyle = "#ccc", c.beginPath(), path(land), c.fill();
	            c.fillStyle = "#f00", c.beginPath(), path(countries[i]), c.fill();
	            c.strokeStyle = "#fff", c.lineWidth = .5, c.beginPath(), path(borders), c.stroke();
	            c.strokeStyle = "#000", c.lineWidth = 2, c.beginPath(), path(globe), c.stroke();
	          };
	        })
	      .transition()
	        .each("end", transition);
	  })();
	}

	d3.select(self.frameElement).style("height", height + "px");

	</script>

## LICENSE[#](https://bl.ocks.org/mbostock/4183330#license)

Released under the [GNU General Public License, version 3](https://opensource.org/licenses/GPL-3.0).