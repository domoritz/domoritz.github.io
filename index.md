---
layout: page
title: "Home"
class: home
---

# Hi, I'm Dominik Moritz

<div class="columns" markdown="1">

<div class="intro" markdown="1">
I'm a research scientist at [Apple](https://www.apple.com/) , working on data visualization and interactive systems for artificial intelligence. In 2020, I will start as an assistant professor at [Carnegie Mellon University](https://hcii.cmu.edu/) where I co-started the [Data Interaction Group](https://dig.cmu.edu/).

I received my PhD from the [Paul G. Allen School](https://www.cs.washington.edu/) at the [University of Washington](https://www.washington.edu/), where I worked with [Jeff Heer](https://homes.cs.washington.edu/~jheer/) and [Bill Howe](https://homes.cs.washington.edu/~billhowe/) in the [Interactive Data Lab](http://idl.cs.washington.edu/) and the [Database Group](https://db.cs.washington.edu/).

I research scalable interactive systems for visualization and analysis. My systems have [won](https://vega.github.io/vega-lite/) [awards](https://uwdata.github.io/draco/) at premier academic venues and are used by the [Python](https://altair-viz.github.io) and [JavaScript](https://vega.github.io/vega-lite/) data science communities.
</div>

<div class="me" markdown="1">
<picture>
  <source srcset='/images/dominik_berlin.webp' type='image/webp' />
  <img
    src='/images/dominik_berlin.jpg'
    alt='Dominik Moritz'/>
</picture>

{:.no-list}
* <a href="mailto:{{ site.email }}">{{ site.email }}</a>
</div>

</div>

During my first year at UW, I received support from the [Fulbright program](https://en.wikipedia.org/wiki/Fulbright_Program). In 2013, I received my B.S. from [Hasso Plattner Institute](https://hpi.de/). I am a scholar of the [German National Academic Foundation](http://www.studienstiftung.de/). I have worked with the [Open Knowledge Foundation](http://www.okfn.org), [Google Research](https://ai.google/research/), and [Microsoft Research](https://www.microsoft.com/en-us/research/group/vibe/). Details are in my [CV]({{ "/cv/" | relative_url }}).

## Featured Projects

<div class="featured-projects">
  {% assign sorted_projects = site.data.projects | sort: 'highlight' %}
  {% for project in sorted_projects %}
    {% if project.highlight %}
      {% include project.html project=project %}
    {% endif %}
  {% endfor %}
</div>
<a href="{{ "/projects/" | relative_url }}" class="button">
  <i class="fas fa-chevron-circle-right"></i>
  Show More Projects
</a>

## Featured Publications

<div class="featured-publications">
  {% for pub in site.data.publications %}
    {% if pub.highlight %}
      <a href="{{ pub.pdf }}" class="publication">
        <strong>{{ pub.title }}</strong>
        <span class="authors">{% for author in pub.authors %}{{ author }}{% unless forloop.last %}, {% endunless %}{% endfor %}</span>.
        <i>{{ pub.venue }}, {{ pub.year }}</i>.
        {% for award in pub.awards %}<br/><span class="award"><i class="fas fa-{% if award == "Best Paper Award" %}trophy{% else %}award{% endif %}" aria-hidden="true"></i> {{ award }}</span>{% endfor %}
      </a>
    {% endif %}
  {% endfor %}
</div>

<a href="{{ "/publications/" | relative_url }}" class="button">
  <i class="fas fa-chevron-circle-right"></i>
  Show All Publications
</a>

<div class="news-travel" markdown="1">

<div class="news" markdown="1">
## News

<ul>
{% for news in site.data.news limit:10 %}
  {% include news.html news=news %}
{% endfor %}
</ul>

</div>

<div class="travel" markdown="1">
## Travel

<table>
<tbody>
{% assign future_travel = site.data.travel | where_exp:'item','item.start == null' %}
{% for travel in future_travel %}
  {% include travel.html travel=travel %}
{% endfor %}
{% assign sorted_travel = site.data.travel | where_exp:'item','item.start' | sort: 'start' | reverse %}
{% for travel in sorted_travel limit:12 %}
  {% include travel.html travel=travel %}
{% endfor %}
</tbody>
</table>

</div>

</div>
