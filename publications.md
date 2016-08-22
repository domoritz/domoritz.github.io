---
layout: page
permalink: /publications/
title: Publications
---

{% assign years = site.data.publications | group_by:"year" %}
{% for year in years %}
## {{ year.name }}
{:#y{{ year.name }}}
{% for pub in year.items %}
  {% include publication.html pub=pub %}
{% endfor %}
{% endfor %}
