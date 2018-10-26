---
layout: page
permalink: /publications/
title: Publications
---

You can find my academic and professional experience in [my CV]({{ 'cv.html' | relative_url  }}). Talks are listed [below](#talks).

{% assign pubyears = site.data.publications | group_by:"year" %}
{% for year in pubyears %}
## {{ year.name }}
{:#y{{ year.name }}}
{% for pub in year.items %}
  {% include publication.html pub=pub %}
{% endfor %}
{% endfor %}


# Talks

These are talks I have given outside of regular conferences. Want me to give a talk? Send me an [email](mailto:{{ site.email }})!

{% assign talkyears = site.data.talks | group_by:"year" %}
{% for year in talkyears %}
## {{ year.name }}
{:#y{{ year.name }}}
{% for talk in year.items %}
  {% include talk.html talk=talk %}
{% endfor %}
{% endfor %}
