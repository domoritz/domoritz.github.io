---
layout: post
title: "Value-Suppressing Uncertainty Palettes"
description: Color palettes that make uncertainty harder to ignore by trading off value resolution against uncertainty.
---

*Originally published at [Medium](https://medium.com/@uwdata/value-suppressing-uncertainty-palettes-426130122ce9).*

<figure>
<div class="flex-rows">
<figure><img src="{{ '/images/posts/vsup/election-polls-bivariate-map.avif' | relative_url }}" alt="A bivariate choropleth map of the US showing Clinton lead against margin of error, with a square legend"></figure>
<figure><img src="{{ '/images/posts/vsup/election-polls-vsup-map.avif' | relative_url }}" alt="A bivariate map (left) and a Value-Suppressing Uncertainty Palette (VSUP, right), showing polling data for US states before the 2016 Presidential Election"></figure>
</div>
<figcaption><em>Fig. 1. A bivariate map (left) and a Value-Suppressing Uncertainty Palette (VSUP, right), showing polling data for US states before the 2016 Presidential Election. It’s tempting to interpret narrow leads for a candidate as a sure thing. However, polling data is volatile and there can be a lot of uncertainty. VSUPs intentionally make it harder to distinguish uncertain states, but allow you to make finer-grained distinctions in value when the uncertainty is low.</em></figcaption>
</figure>

The real world is full of uncertainty, but it can be tough to communicate that uncertainty. This is especially true for data visualization, where the usual practice is to *quantify* uncertainty (turn it into a number somehow) and then *encode* uncertainty by visualizing it. This has to happen at the same time as figuring out how to represent the rest of the data. Uncertainty information inherently makes visualizations more complex: it’s more data to show, and uncertainty quantification can be a complex process that results in numbers that are difficult to interpret.

To make matters worse, one goal of showing uncertainty is to *integrate* the uncertainty into your decision-making process. That is, you may want people to be less confident in decisions based on highly uncertain data. If you don’t properly integrate uncertainty information, then you risk making the uncertainty *ignorable*, such that people will ignore the risks and variation in the data, and treat things that should have a lot of uncertainty (the outcomes of elections, the effectiveness of medication or diets, or the expected arrival of transportation) as certainties. You also don’t want to be too *hasty*: if there’s too much uncertainty, maybe the right decision is to wait until there’s more data, or refrain from making too strong of a prediction.

<figure>
<img src="{{ '/images/posts/vsup/sasquatch-sightings-bivariate-map.avif' | relative_url }}" alt="A bivariate map from Joshua Stevens that shows both population density and sasquatch sightings in the continental US">
<figcaption><em>Fig. 2. A</em> <a href="http://www.joshuastevens.net/cartography/make-a-bivariate-choropleth-map/"><em>bivariate map from Joshua Stevens</em></a> <em>that shows both population density and sasquatch sightings in the continental US. The brighter the purple, the more sasquatch sightings. The brighter the green, the more population density. Bright blue counties have both dense population and lots of sasquatch sightings.</em></figcaption>
</figure>

One strategy to make uncertainty unignorable is to use a “bivariate map.” Bivariate maps encode two types of data in the same visual channel. For example, [Joshua Stevens’ Sasquatch map](http://www.joshuastevens.net/cartography/make-a-bivariate-choropleth-map/) (Fig. 2) assigns a color to a U.S. county based on two variables: its population density, and its number of sasquatch sightings. These maps have been around for a long time (see Fig. 3), but they can be hard to interpret. The visual properties we use to represent sasquatch sightings can be difficult to disentangle from the colors we use to represent population density: we don’t perceive “40% green, 60% purple” very accurately when we look at colors! As such, bivariate maps usually limit themselves to a small set of outputs. There’s only 9 possible colors in the sasquatch map, and only 16 possible texture comparisons in the map in Fig. 3.

<figure>
<img src="{{ '/images/posts/vsup/mayr-1874-land-use-map.avif' | relative_url }}" alt="One of the earliest surviving examples of a bivariate color map, an 1874 map of land use from Bavarian statistician Georg Mayr">
<figcaption><em>Fig. 3. One of the earliest surviving examples of a bivariate color map, an</em> <a href="http://infowetrust.com/scroll/#mayr4"><em>1874 map of land use from Bavarian statistician Georg Mayr</em></a><em>. The width of the vertical red lines show the density of horses in the area, the width of the horizontal green lines the density of cattle. It’s a bit difficult to interpret, but perhaps you can make out regions where there are lots of both horses and cattle, or vice versa.</em></figcaption>
</figure>

When we make a Value-Suppressing Uncertainty Palette, we decide to spend this limited budget of outputs in the service of integrating data and uncertainty. We give *more* distinct outputs to the bivariate map when the data are very certain, and *fewer* when the data is highly uncertain. VSUPs have an internal “tree quantization” scheme to determine which combination of data value and uncertainty value corresponds to which discrete color. When data is highly uncertain, then there’s only one output color. As certainty increases, this color has two “child colors” that divide the data domain equally, allowing us to distinguish high and low values from each other. As certainty increases again, each of these two children have two children of their own, chopping up the data domain into smaller and smaller regions, and allowing fine-grain distinctions as the level of certainty goes up. To drive this metaphor home, rather than the traditional bivariate square legend shape, we prefer to present VSUP legends as a pyramid or wedge (Fig. 4).

<figure>
<img src="{{ '/images/posts/vsup/bivariate-square-vs-vsup-wedge.avif' | relative_url }}" alt="A traditional bivariate map assigns one unique output (in this case, a color), to every combination of the two variables of interest">
<figcaption><em>Fig. 4. A traditional bivariate map assigns one unique output (in this case, a color), to every combination of the two variables of interest. VSUPs, by contrast, assume that differences between values become less important as uncertainty increases, and so gradually reduce the number of outputs as data become more uncertain. When there’s too much uncertainty, everything gets mapped to the same color.</em></figcaption>
</figure>

Fig. 1 shows an example of a VSUP designed to show polling data prior to the 2016 U.S. Presidential Election. If the candidates are very far apart in the polls, and the margins of error very low, then it’s responsible to talk about even minute differences in polling: a candidate leading 51% to 49% with very narrow margins of error is probably going to win in that state. As such, most of the colors are devoted to these highly certain values. As the margins of error gets bigger, speculating about these small differences becomes less responsible: we devote fewer and fewer colors to them, and states can only be said to lean in one direction or the other. If a candidate is polling within 2 margins of error from their opponent, everything gets mapped to the same “tossup” color. The VSUP *suppresses* uncertain values, discouraging viewers from making predictions about them.

<figure>
<div class="flex-rows">
<figure><img src="{{ '/images/posts/vsup/snap-usage-value-map.avif' | relative_url }}" alt="A choropleth map of the US showing the percentage of households using SNAP, with a square legend"></figure>
<figure><img src="{{ '/images/posts/vsup/snap-usage-vsup-map.avif' | relative_url }}" alt="Standard value map (left) and VSUP (right) showing the percentage of US households using the Supplemental Nutrition Assistance Program"></figure>
</div>
<figcaption>Fig. 5. Standard value map (left) and VSUP (right) showing the percentage of US households using the Supplemental Nutrition Assistance Program. Without uncertainty information, Wyoming seems like a clear outlier with few households needing assistance, whereas the east coast looks like a solid mass of high values. In the VSUP, we see that Wyoming’s low population means that its estimates have high uncertainty, and may not be much different than its neighbors. Similar, it is mostly the Rust Belt (with states like New York, Pennsylvania, and Michigan) that have both high rates and high certainty in those estimates.</figcaption>
</figure>

VSUPs encourage people to be cautious about their judgments when uncertainty is high, but this is not always the behavior a designer might want to see: for instance, a highly uncertain but highly important “[black swan](https://en.wikipedia.org/wiki/Black_swan_theory)” event might deserve high salience in the display, no matter the uncertainty information. Likewise, VSUPs rely on the designer to choose important levels of uncertainty, and what counts as “too uncertain to distinguish.” This definition might not be fixed, or could change over the course of the analysis session. In that case, the designer might want to allow some interactivity or filtering to reshape the VSUP and support new tasks.

There are more details about VSUPs, including an empirical evaluation of their effectiveness, in our [paper repository](https://github.com/uwdata/papers-vsup/). If you’d like to start making VSUPs for yourself, we’ve got [a module](https://github.com/uwdata/vsup) that plays nice with [D3.js](https://d3js.org/)!

*This article was written by Michael Correll, Dominik Moritz, and Jeffrey Heer, describing a paper we presented at CHI 2018. For more,* [*read the paper*](http://idl.cs.washington.edu/papers/uncertainty-palettes)*.*
