---
layout: page
permalink: /projects/
title: Projects
class: projects
---

{:.hidden}
# Projects

{:.lead}
Here are some projects I have worked on for school, work, or fun. You can find the code for most of them on [GitHub](https://github.com/domoritz).

<div class="grid">
  {% for project in site.data.projects %}
    {% include project.html project=project %}
  {% endfor %}
</div>
