---
layout: page
permalink: /publications/
title: Publications
---

You can find my academic and professional experience as well as talks I have given in [my CV]({{ 'cv.html' | relative_url  }}).

{% assign years = site.data.publications | group_by:"year" %}
{% for year in years %}
## {{ year.name }}
{:#y{{ year.name }}}
{% for pub in year.items %}
  {% include publication.html pub=pub %}
{% endfor %}
{% endfor %}
