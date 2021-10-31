---
layout: page
permalink: /workshops/
title: Workshop & Bootcamps conducted
class: workshops
---


{:.hidden}
# Workshops

{% assign talktitles = site.data.workshops | group_by:"title" %}
{% for title in talktitles %}
{:.talk-title}
### {{ workshop.name }}
{% assign sorted_talks = title.items | sort: 'date' | reverse %}
{% for talk in sorted_talks  %}
  {% include talk.html talk=talk %}
{% endfor %}
{% endfor %}
