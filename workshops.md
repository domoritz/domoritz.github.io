---
layout: page
permalink: /workshops/
title: Workshops & Bootcamps
class: workshops
---


{:.hidden}
# Workshops

{% assign talktitles = site.data.workshops | group_by:"title" %}
{% for title in talktitles %}
{:.talk-title}
### {{ title.name }}
{% assign sorted_talks = title.items | sort: 'date' | reverse %}
{% for talk in sorted_talks  %}
  {% include talk.html talk=talk %}
{% endfor %}
{% endfor %}
