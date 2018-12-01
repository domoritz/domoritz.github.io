---
layout: page
permalink: /talks/
title: Talks
class: talks
---

{:.hidden}
# Talks

{% assign talktitles = site.data.talks | group_by:"title" %}
{% for title in talktitles %}
{:.talk-title}
### {{ title.name }}
{% for talk in title.items %}
  {% include talk.html talk=talk %}
{% endfor %}
{% endfor %}
