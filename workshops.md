---
layout: page
permalink: /workshops/
title: Workshop & Bootcamps conducted
class: workshops
---


-- This page is work in progress --

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
