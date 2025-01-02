---
title: "Cheatsheet"
header:
  image: /assets/images/defaults/header-main.png
layout: archive
permalink: /Cheatsheet/
---

{% assign category_name = "Cheatsheet" %}

{% assign filtered_posts = site.posts | where: "categories", category_name %}

{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}