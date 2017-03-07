---
layout: page
permalink: /projects/
title: Projects
---

{:.lead}
Here are some projects I have worked on for school, work, or fun that you might find interesting. You can find the code for most of them on [GitHub](https://github.com/domoritz).

* TOC
{:toc}

## Research

### Vega stack

With the Interactive Data Lab, we created the [Vega stack](https://vega.github.io/) and a number of tools for data exploration based on it.

#### Vega-Lite

I am the co-author of [Vega-Lite](https://vega.github.io/vega-lite/), a high-level visualization grammar. It provides a concise JSON syntax for supporting rapid generation of visualizations to support analysis. Vega-Lite specifications can be compiled to Vega specifications.

{% include image name="vega-lite.png" caption="Vega-Lite examples." %}

#### Polestar and Voyager

We built the data exploration tools [Polestar](https://github.com/vega/polestar) and [Voyager](https://github.com/vega/voyager) on top of Vega-Lite. We have [written a paper about these systems]({{ "/publications/#voyager-exploratory-analysis-via-faceted-browsing-of-visualization-recommendations" | relative_url }}).

#### ipyvega

IPython/Jupyter notebook module for Vega and Vega-Lite. The code is on [GitHub](https://github.com/vega/ipyvega).

### Myria

[Myria](http://myria.cs.washington.edu/) is a distributed Big Data management system in the cloud which is being developed in the [Database group](http://db.cs.washington.edu/) at the [University of Washington](http://uw.edu/).

## Jobs

### Data Search at Google Research

During my internship with Google Research in Mountain View, I worked on the UX for Goods. The system is described in [this paper](http://research.google.com/pubs/pub45390.html).

### Production System Monitoring at Google

During my internship at Google in NYC during the summer of 2014, I implemented a new out of core join and aggregation operators for a large-scale time series database. The system processes production monitoring data from various systems at Google.

Not much about this system is public but there is a [talk from John Banning about the system](https://vimeo.com/173607638).

### CKAN at the Open Knowledge foundation

[CKAN](http://www.ckan.org) is the world’s leading open-source data portal platform used by [data.gov.uk](http://data.gov.uk), [data.gov](http://catalog.data.gov/) and [publicdata.eu](http://publicdata.eu/) among many others.

It is a powerful data management system that makes data accessible – by providing tools to streamline publishing, sharing, finding and using data. CKAN is aimed at data publishers (national and regional governments, companies and organizations) wanting to make their data open and available. CKAN is mainly developed by the [Open Knowledge Foundation](http://okfn.org/).

Development happens on [GitHub](https://github.com/ckan/ckan).

I also developed and contributed to many other tools related to CKAN like [messytables](https://github.com/okfn/messytables) and the [datapusher](https://github.com/ckan/datapusher).

## School

### Text detection with neural networks

For a class project, I extracted 500k labeled images of figures from roughly 1M papers. For each image I created a mask that shows where the text in the image is. I then used the images to train a neural network that would find text in images. The project is on [GitHub](https://github.com/domoritz/label_generator).

{:.center.two-thirds}
{% include image name="text-detection.png" caption="Text detection output." %}

### Space Clean Up

A bomberman clone written in Squeak Smalltalk. Code is on [GitHub](https://github.com/matthias-springer/space-cleanup).

{% include image name="scu.jpg" caption="Screenshot of Space Clean Up." %}

### MapLink/Gis.ly

For [Patrick Baudisch's](http://www.patrickbaudisch.com/) [HCI class at HPI](https://hpi.de/baudisch/teaching.html), we had to implement an application that ususally requires large screens on a iPod nano (enough for 4 buttons). We implemented a [GIS]() application that allows users to geo-reference images by simply aligning points. We introduced the concept of an X-Ray layer to enable users on small devices to align points.

You can find more details in the [paper]({{ "/files/2013-MapLink.pdf" | relative_url }}).

{:.center.half}
{% include image name="maplink.png" caption="MapLink." %}

{:.video}
<iframe width="560" height="315" src="https://www.youtube.com/embed/U9-zceFffSY" frameborder="0" allowfullscreen></iframe>

### Singing VHDL board

Together with another student at HPI, I built a music player in VHDL. The code as well as schematics to print the board are on [GitHub](https://github.com/domoritz/S76D). I wrote a short [blog post about the project]({% post_url 2012-03-27-singing_vhdl_board | relative_url %}).

{:.video}
<iframe width="560" height="315" src="https://www.youtube.com/embed/qsjFVgriZzY" frameborder="0" allowfullscreen></iframe>

### The glass is half full

In this class project I write about how we can use an optimistic approach to concurrency control. You can find the paper [here]({{ "/files/2012-the_glass_is_half_full.pdf" | relative_url }}).

### SoSat

A SAT solver that uses different statistical optimization algorithms to solve SAT problems encoded in the DIMACS format. This solver is written in Python and uses [Numpy](http://www.numpy.org/) to speed up calculations. The two main algorithms in this solver are an *ant colony optimization algorithm* and a *genetic algorithm*. To support these algorithms, there are some pre-processing algorithms.

With [Matthias Springer](http://www.matthiasspringer.de/). The code is on [GitHub](https://github.com/domoritz/SoSAT).

### Tagshot

Tagshot is a photo management tool in the browser. We designed and developed as a class project. Our goal was to create a tool that let's users efficiently manage large numbers of photos and in particular add tags. The code is on [GitHub]() and I wrote a [blog post about it]({% post_url 2012-03-17-tagshot-und-andere-projekte | relative_url %}).

{:.video}
<iframe width="640" height="360" src="https://www.youtube.com/embed/nB3fcDLNk8g" frameborder="0" allowfullscreen></iframe>


## Side projects

### Himawari 8

A chrome extension that shows the latest image from the Himawari 8 weather satellite when you open a new tab. The code is on [Github](https://github.com/domoritz/himawari-8-chrome) and you can install the extension from the [Chrome web store](https://chrome.google.com/webstore/detail/himawari-8-satellite-new/llelgapflianaapmnpncgakfjhfhnojm).

{:.center.two-thirds}
{% include image name="himawari.png" caption="Himawari Chrome extension new tab page." %}

### Game of Life

I implemented Conway's Game of Life in Python, Go, Rust, and C#. All projects are on [GitHub](https://github.com/search?q=user%3Adomoritz+gameoflife).

### Leaflet plugins

Leaflet is an open source JavaScript library for mobile friendly interactive maps. I used it for various projects and also wrote a few extensions.


#### LocateControl

A simple control to find your current location on a leaflet map. Very popular and used on [the OpenStreetMap home page](http://osm.org/).

The code is at [github.com/domoritz/leaflet-locatecontrol](https://github.com/domoritz/leaflet-locatecontrol).

{:.center.two-thirds}
{% include image name="locate.png" caption="Leaflet locate extension." %}


#### MaskCanvas

Visualize coverage on a leaflet map. The data is store in a quad-tree to make queries to the data super fast.

The code is at [github.com/domoritz/leaflet-maskcanvas](https://github.com/domoritz/leaflet-maskcanvas). I used it to visualize [public transit coverage around Berlin](http://domoritz.github.com/vbb-coverage/).

{:.center.two-thirds}
{% include image name="vbb.png" caption="Public transit coverage around Berlin." %}


#### Heatmap layer

For this project I combined the MaskCanvas layer and `heatmap.js` from my friend [Patrick](http://www.patrick-wied.at).
You can learn more about it at [patrick-wied.at/static/heatmapjs/example-heatmap-leaflet.html](http://www.patrick-wied.at/static/heatmapjs/example-heatmap-leaflet.html)


#### Informaticup 2011: Optimal ATM placement

[Blog post about our entry]({% post_url 2011-01-23-informaticup-2011 | relative_url %}).

{:.center.two-thirds}
{% include image name="hatfield.png" caption="Visualization of optimal ATM placement." %}


#### Informaticup 2012: Shopping tour optimizer

[Blog post about our entry]({% post_url 2012-03-17-shoppingtour-optimizer | relative_url %}).

{:.video}
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/HSMU7a_TlgI" frameborder="0" allowfullscreen></iframe>
