---
layout: page
permalink: /blog/
---

# Blog posts

<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

<div class="post-list">
  {% for post in site.posts %}
    {% assign currentdate = post.date | date: "%Y" %}
    {% if currentdate != date %}
      <h2 id="y{{ currentdate }}" class="year">{{ currentdate }}</h2>
      {% assign date = currentdate %}
    {% endif %}

    <div class="post-block">
      <h3>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </h3>
      <span class="post-meta">{{ post.date | date: "%b %-d" }}</span>
      {% if post.description %}<p class="post-subtitle">{{ post.description }}</p>{% endif %}
    </div>
  {% endfor %}
</div>
