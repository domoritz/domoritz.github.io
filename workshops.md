---
layout: page
permalink: /workshops/
title: Workshops & Bootcamps
class: workshops
---


{:.hidden}
# Workshops

{% assign workshoptitles = site.data.workshops | group_by:"title" %}
{% for title in workshoptitles %}
{:.workshop-title}
### {{ title.name }}
{% assign sorted_workshops = title.items | sort: 'date' | reverse %}
{% for workshop in sorted_workshops  %}
  {% include workshop.html workshop=workshop %}
{% endfor %}
{% endfor %}
