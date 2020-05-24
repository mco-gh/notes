A High-Level Grammar of Interactive Graphics

#   **Vega-Lite** – A Grammar of Interactive Graphics

 [(L)](https://vega.github.io/editor/#/examples/vega-lite/stacked_area_stream)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/circle)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/bar_layered_transparent)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/tick_strip)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/layer_line_color_rule)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/trellis_barley)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/bar_grouped)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/circle_github_punchcard)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/stacked_bar_weather)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/trellis_bar_histogram)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/area)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/stacked_bar_v)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/line_color)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/circle_opacity)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/line_slope)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/trellis_anscombe)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/point_binned_opacity)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/line_month)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/rect_heatmap)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/interactive_layered_crossfilter)  [(L)](https://vega.github.io/editor/#/examples/vega-lite/layer_connected_scatterplot)

**Vega-Lite** is a high-level grammar of interactive graphics. It provides a concise JSON syntax for rapidly generating visualizations to support analysis. Vega-Lite specifications can be compiled to [Vega](http://vega.github.io/vega) specifications.

  Vega-Lite specifications describe visualizations as mappings from data to **properties of graphical marks** (e.g., points or bars). The Vega-Lite compiler **automatically produces visualization components** including axes, legends, and scales. It then determines properties of these components based on a set of **carefully designed rules**. This approach allows specifications to be succinct and expressive, but also provide user control. As Vega-Lite is designed for analysis, it supports **data transformations** such as aggregation, binning, filtering, sorting, and **visual transformations** including stacking and faceting. Moreover, Vega-Lite specifications can be **composed** into layered and multi-view displays, and made **interactive with selections**.     [Get started Latest Version: 2.3.1](https://vega.github.io/vega-lite/tutorials/getting_started.html)  [Try online](https://vega.github.io/editor/#/custom/vega-lite)

Read our [introduction article to Vega-Lite v2 on Medium](https://medium.com/@uwdata/de6661c12d58), watch our [OpenVis Conf talk about the new features in Vega-Lite v2](https://www.youtube.com/watch?v=9uaHRWj04D4), check out the [documentation](https://vega.github.io/vega-lite/docs/) and take a look at our [example gallery](https://vega.github.io/vega-lite/examples/).

**[We are looking to mentor students for a Google Summer of Code project with us. Apply if you want to shape the future of declarative data visualization!](https://summerofcode.withgoogle.com/organizations/5646868357316608/)**

## [](https://vega.github.io/vega-lite/#example)Example

With Vega-Lite, we can start with a [bar chart of the average monthly precipitation]() in Seattle, [overlay a rule for the overall yearly average](), and have it represent [an interactive moving average for a dragged region]().

JanFebMarAprMayJunJulAugSepOctNovDecdate (month)012345Mean of precipitation

[Open in Vega Editor](https://vega.github.io/vega-lite/#)

	{
	  "data": {"url": "data/seattle-weather.csv"},
	  "mark": "bar",
	  "encoding": {
	    "x": {
	      "timeUnit": "month",
	      "field": "date",
	      "type": "ordinal"
	    },
	    "y": {
	      "aggregate": "mean",
	      "field": "precipitation",
	      "type": "quantitative"
	    }
	  }
	}

## [](https://vega.github.io/vega-lite/#additional-links)Additional Links

- Award winning [research paper](http://idl.cs.washington.edu/papers/vega-lite) and [video of our OpenVis Conf talk](https://www.youtube.com/watch?v=9uaHRWj04D4) on the design of Vega-Lite

- [JSON schema](http://json-schema.org/) specification for [Vega-Lite](https://github.com/vega/schema) ([latest](https://vega.github.io/schema/vega-lite/v2.json))

- Ask questions about Vega-Lite in the [Vega Discussion Group / Mailing List](https://groups.google.com/forum/?fromgroups#!forum/vega-js)

- Fork our [Vega-Lite Block](https://bl.ocks.org/domoritz/455e1c7872c4b38a58b90df0c3d7b1b9), or [Observable Notebook](https://beta.observablehq.com/@domoritz/vega-lite-demo).

## [](https://vega.github.io/vega-lite/#team)Team

The development of Vega-Lite is led by [Kanit “Ham” Wongsuphasawat](https://twitter.com/kanitw), [Dominik Moritz](https://twitter.com/domoritz), [Arvind Satyanarayan](https://twitter.com/arvindsatya1), and [Jeffrey Heer](https://twitter.com/jeffrey_heer) of the [University Washington Interactive Data Lab](https://idl.cs.washington.edu/). Please see the [contributors page](https://github.com/vega/vega-lite/graphs/contributors) for the full list of contributors.