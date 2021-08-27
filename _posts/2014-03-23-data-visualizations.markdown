---
layout: post
title: "Data visualizations"
description: "CSE512 at UW and other projects"
date: 2014-03-23 23:50:21 -0700
comments: true
categories: UW
tags:
  - visualization
---

During the spring quarter at UW, I took Jeffrey Heer's [data visualization class](https://courses.cs.washington.edu/courses/cse512/14wi/index.html). As part of this class, I worked on three assignments and a final project of which I would like to share the first two assignments.

In the [first assignment](http://courses.cs.washington.edu/courses/cse512/14wi/a1.html) we had to design a visualization for Burtin's antibiotics dataset. The task was to design a visualization without any knowledge from the class. Here is what I created:

<iframe src="https://domoritz.github.io/vis-a1/" width="100%" height="600px"></iframe>

I created the static visualization with D3. The code is on [GitHub](https://github.com/domoritz/vis-a1).

For the [second assignment](http://courses.cs.washington.edu/courses/cse512/14wi/a2.html), we could choose between different datasets to visualize. I chose the FAA flight data and wanted to answer the question whether airlines overestimate the flight times in order to avoid having bad on-time records. TL;DR, the answer is yes.

{% include image name="a2-domoritz.png" alt="Airlines overestimate flight times." %}

The data in this plot is based on 1.4GB of flight records for one month each year since 1987. I created the plot with Tableau.

Not as part of the class but during the [Open Data Day](http://opendataday.org/), I worked on a [live map of bus locations in Seattle](https://domoritz.github.io/live-bus-seattle).
