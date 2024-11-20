---
layout: page
title: "Home"
class: home
---

# Hi, I'm Dominik Moritz

<div class="columns" markdown="1">

<div class="intro" markdown="1">
I'm a professor at the [Human-Computer Interaction Institute](https://hcii.cmu.edu/) at [Carnegie Mellon University](https://www.cmu.edu/) and an ML researcher at [Apple](https://www.apple.com/) <i class="fab fa-apple"></i>. I design and build interactive systems for visualization and analysis. At CMU, I co-lead the [Data Interaction Group](https://dig.cmu.edu/). [Read this]({% post_url 2024-11-20-phd-application %}) if you want to apply for a PhD with me.

I received my PhD from the [Paul G. Allen School](https://www.cs.washington.edu/) at the [University of Washington](https://www.washington.edu/), where I worked with [Jeff Heer](https://homes.cs.washington.edu/~jheer/) and [Bill Howe](https://homes.cs.washington.edu/~billhowe/) in the [Interactive Data Lab](http://idl.cs.washington.edu/) and the [Database Group](https://db.cs.washington.edu/).

My systems have [won](https://vega.github.io/vega-lite/) [awards](https://uwdata.github.io/draco/) [at](https://arxiv.org/pdf/2110.12536) [premier](https://www.domoritz.de/papers/2023-LineBias-VIS.pdf) [academic](https://www.domoritz.de/papers/2023-AutoProfiler-VIS.pdf) [venues](https://arxiv.org/pdf/2404.03085) and are used by the [Python](https://altair-viz.github.io) and [JavaScript](https://vega.github.io/vega-lite/) data science communities.

Find me on [GitHub](https://github.com/domoritz), the [Fediverse](https://vis.social/@dom), [Bluesky](https://bsky.app/profile/domoritz.de), [LinkedIn](https://www.linkedin.com/in/dominik-moritz-409b8124/), or [Twitter](https://twitter.com/domoritz).
</div>

<div class="me" markdown="1">
<picture>
  <source srcset='/images/dominik_berlin.webp' type='image/webp' />
  <img
    src='/images/dominik_berlin.jpg'
    alt='Dominik Moritz'>
</picture>

{:.no-list}
* <a href="mailto:{{ site.email }}">{{ site.email }}</a>
* NSH 2504B
</div>

</div>

During my first year at UW, I received support from the [Fulbright program](https://en.wikipedia.org/wiki/Fulbright_Program). In 2013, I received my B.S. from [Hasso Plattner Institute](https://hpi.de/). I am a scholar of the [German National Academic Foundation](http://www.studienstiftung.de/). I have worked with the [Open Knowledge Foundation](http://www.okfn.org), [Google Research](https://ai.google/research/), [Microsoft Research](https://www.microsoft.com/en-us/research/group/vibe/), and others. Details are in my [CV]({{ "/cv/" | relative_url }}).

## Featured <a href="{{ "/projects/" | relative_url }}">Projects</a>

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

## Featured <a href="{{ "/publications/" | relative_url }}">Publications</a>

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
