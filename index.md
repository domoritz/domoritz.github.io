---
layout: page
title: "Home"
class: home
---

# Hi, I'm Anuj Gupta

<div class="columns" markdown="1">

<div class="intro" markdown="1" style="text-align: justify"> 

I am a senior executive, advisor, investor and thought leader working in the area of machine learning. My interests lie at the intersection of Mathematics and Computer Science. In my career, I have incubated and led mutlple succesful AI teams at both - early stage startups as well as Fortune 50. I have worked very closely with founders and CXOs to successfully deliver AI products. I have owned AI function end-to-end: from vision, strategy, team building, deep techniical direction, execution and people realted matters. I have co-authored a best-selling [book on NLP](http://www.practicalnlp.ai/) with O'Reilly Media in 2020. The book focuses on various phases of building AI systems when you are part of product teams. The book has been translated in mutiple languages and is currently used by over 40 universities globally for their AI curriculum. 

Curently I am heading the AI fucntion at [Vahan Inc](https://vahan.ai/) [(YC S'19)](https://news.crunchbase.com/news/why-yc-went-8725-miles-away-from-mountain-view-to-find-the-next-big-startup/). At Vahan we are using AI, systems and data to radically transform the Blue Collar Workers (BCW) space. Using deep tech, we help gig economy companies screen & recruit BCW at scale and high velocity. This goes a long way not just in providing jobs but also saves BCW from exploitation at the hands of middlemen and bring positive change to many lives.

I have been a major contributor in AI community - both in India and abroad. I am a major keynote speaker, pannelist and mentor. 

<br>
<br>


<!---
I'm faculty at the [Human-Computer Interaction Institute](https://hcii.cmu.edu/) at [Carnegie Mellon University](https://www.cmu.edu/) and an ML researcher at [Apple](https://www.apple.com/) <i class="fab fa-apple"></i>. I design and build interactive systems for visualization and analysis. At CMU, I co-lead the [Data Interaction Group](https://dig.cmu.edu/).

I received my PhD from the [Paul G. Allen School](https://www.cs.washington.edu/) at the [University of Washington](https://www.washington.edu/), where I worked with [Jeff Heer](https://homes.cs.washington.edu/~jheer/) and [Bill Howe](https://homes.cs.washington.edu/~billhowe/) in the [Interactive Data Lab](http://idl.cs.washington.edu/) and the [Database Group](https://db.cs.washington.edu/).

My systems have [won](https://vega.github.io/vega-lite/) [awards](https://uwdata.github.io/draco/) at premier academic venues and are used by the [Python](https://altair-viz.github.io) and [JavaScript](https://vega.github.io/vega-lite/) data science communities.
--->

</div>

<div class="me" markdown="1">
<picture>
  <source srcset='/images/anuj_gupta.webp' type='image/webp' />
  <img
    src='/images/anuj_gupta.jpg'
    style="border:1px solid grey"
    alt='Anuj Gupta'>
</picture>

<!---
{:.no-list}
* <a href="mailto:{{ site.email }}">{{ site.email }}</a>
* NSH 2602B
--->

</div>



<!---
During my first year at UW, I received support from the [Fulbright program](https://en.wikipedia.org/wiki/Fulbright_Program). In 2013, I received my B.S. from [Hasso Plattner Institute](https://hpi.de/). I am a scholar of the [German National Academic Foundation](http://www.studienstiftung.de/). I have worked with the [Open Knowledge Foundation](http://www.okfn.org), [Google Research](https://ai.google/research/), and [Microsoft Research](https://www.microsoft.com/en-us/research/group/vibe/). Details are in my [CV]({{ "/cv/" | relative_url }}).
--->


<!---
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
--->


<!---
## Featured Publications

<div class="featured-publications">
  {% assign sorted_publications = site.publications | sort: 'year' | reverse %}
  {% for pub in sorted_publications %}
    {% if pub.highlight %}
      <a href="{{ pub.pdf }}" class="publication">
        <strong>{{ pub.title }}</strong>
        <span class="authors">{% for author in pub.authors %}{{ author }}{% unless forloop.last %}, {% endunless %}{% endfor %}</span>.
        <i>{% if pub.venue %}{{ pub.venue }}, {% endif %}{{ pub.year }}</i>.
        {% for award in pub.awards %}<br/><span class="award"><i class="fas fa-{% if award == "Best Paper Award" %}trophy{% else %}award{% endif %}" aria-hidden="true"></i> {{ award }}</span>{% endfor %}
      </a>
    {% endif %}
  {% endfor %}
</div>

<a href="{{ "/publications/" | relative_url }}" class="button">
  <i class="fas fa-chevron-circle-right"></i>
  Show All Publications
</a>
--->


<!---
<div class="news-travel" markdown="1">

<div class="news" markdown="1">
## Latest News

<ul>
{% for news in site.data.news limit:10 %}
  {% include news.html news=news %}
{% endfor %}
</ul>

</div>
-->

<!---
<div class="travel" markdown="1">
## Latest Travel

<table>
<tbody>
{% assign future_travel = site.data.travel | where_exp:'item','item.start == null' %}
{% for travel in future_travel %}
  {% include travel.html travel=travel %}
{% endfor %}
{% assign sorted_travel = site.data.travel | where_exp:'item','item.start' | sort: 'start' | reverse %}
{% for travel in sorted_travel limit:10 %}
  {% include travel.html travel=travel %}
{% endfor %}
</tbody>
</table>

</div>

</div>

-->


