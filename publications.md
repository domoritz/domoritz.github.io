---
layout: page
permalink: /publications/
---

# Publications

{% assign years = site.data.publications | group_by:"year" %}
{% for year in years %}
## {{ year.name }}
{% for pub in year.items %}
  {% include publication.html pub=pub %}
{% endfor %}
{% endfor %}
