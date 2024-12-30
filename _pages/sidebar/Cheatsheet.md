---
title: "Cheatsheet"
layout: archive
permalink: /Cheatsheet/
---

{% assign category_name = "cheatsheet" %}

{% assign filtered_posts = site.posts | where: "categories", category_name %}

{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}