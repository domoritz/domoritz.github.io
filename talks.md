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
{% assign sorted_talks = title.items | sort: 'date' | reverse %}
{% for talk in sorted_talks  %}
  {% include talk.html talk=talk %}
{% endfor %}
{% endfor %}

<!-- 

{% assign pubyears = site.publications | group_by:"year"  %}
{% assign sorted_pubyears = pubyears | reverse %}
{% for year in sorted_pubyears %}

{:#y{{ year.name }} .year}
{% for pub in year.items %}
  {% include publication.html pub=pub %}
{% endfor %}
{% endfor %}

{% include publication.html pub=pub %}

<!-- <script src="https://cdn.jsdelivr.net/npm/itemsjs@1.0.40/dist/itemsjs.min.js"></script> -->
<script>
  {% include itemsjs.min.js %}
  {% include pubfilter.js %}
</script>
 -->
