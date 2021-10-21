---
layout: page
permalink: /workshops/
title: Workshop & Bootcamps conducted
class: workshops
---


{:.hidden}
# Talks

{% assign talktitles = site.data.talks | group_by:"title" %}
{% for title in talktitles %}
{:.talk-title}
### {{ title.name }}
{% assign sorted_talks = title.items | sort: 'date' | reverse %}
{% for talk in sorted_talks  %}
  {% include talk.html talk=talk %}
{% endfor %}
{% endfor %}

-- This page is work in progress --