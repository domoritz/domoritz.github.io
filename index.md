---
layout: page
title: "Hi, I'm Dominik Moritz"
---

<div class="home-columns" markdown="1">

<div class="intro" markdown="1">
I'm a PhD candidate at the [University of Washington](https://www.washington.edu/) in the [Paul G. Allen School of Computer Science & Engineering](https://www.cs.washington.edu/). I am advised by [Jeff Heer](https://homes.cs.washington.edu/~jheer/) from the [Interactive Data Lab](http://idl.cs.washington.edu/) and [Bill Howe](https://homes.cs.washington.edu/~billhowe/) from the [eScience Institute](http://escience.washington.edu/), the [iSchool](https://ischool.uw.edu/), and the [Database Group](https://db.cs.washington.edu/).

I combine large-scale systems with interactive data visualization to develop tools that enhance people's ability to understand and communicate data. The Systems I develop have won awards at premier academic venues, and are used by the [Python](https://altair-viz.github.io) and [JavaScript](https://vega.github.io/vega-lite/) data science communities. Learn more about my research through my [publications]({{ "/publications/" | relative_url }}) or watch my [talks]({{ "/publications/#talks" | relative_url }}).
</div>

<div class="me" markdown="1">
<img src="{{ '/images/dominik_berlin.jpg' | absolute_url }}" alt="Image of me">

{:.no-list}
* <a href="mailto:{{ site.email }}">{{ site.email }}</a>
* [Paul G. Allen Center](http://www.washington.edu/maps/?q=cse) Room [486](https://norfolk.cs.washington.edu/directory/index.php?prev_floor=4&show_room=CSE486)
</div>

</div>

During my first year at UW, I received support from the [Fulbright program](https://en.wikipedia.org/wiki/Fulbright_Program). Until 2013, I studied IT-Systems Engineering at [Hasso Plattner Institute](http://www.hpi.uni-potsdam.de) at the University of Potsdam, Germany. I am a scholar of the [German National Academic Foundation](http://www.studienstiftung.de/). I have worked with the [Open Knowledge Foundation](http://www.okfn.org), Google, [Google Research](https://ai.google/research/), and [Microsoft Research](https://www.microsoft.com/en-us/research/group/vibe/). Details are in my [CV]({{ "/cv.html" | relative_url }}).

<span style="color:firebrick; font-weight: bold">I am on the research faculty market this year. Please get in touch if you are hiring.</span>

<div class="news-travel" markdown="1">

<div class="news" markdown="1">
## News

<ul>
{% for news in site.data.news %}
  {% include news.html news=news %}
{% endfor %}
</ul>

</div>

<div class="travel" markdown="1">
## Travel

<table>
<tbody>
{% for travel in site.data.travel %}
  {% include travel.html travel=travel %}
{% endfor %}
</tbody>
</table>

</div>

</div>
