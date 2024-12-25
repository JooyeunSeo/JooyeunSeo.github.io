---
title: "Samples"
layout: archive
permalink: /대분류1-Samples/
---

{% assign category_name = "Samples" %}

{% assign filtered_posts = site.posts | where: "categories", category_name %}

{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}