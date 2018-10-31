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

Want me to give a talk? Send me an [email](mailto:{{ site.email }})!

{% assign talktitles = site.data.talks | group_by:"title" %}
{% for title in talktitles %}
{:.talk-title}
### {{ title.name }}
{% for talk in title.items %}
  {% include talk.html talk=talk %}
{% endfor %}
{% endfor %}
