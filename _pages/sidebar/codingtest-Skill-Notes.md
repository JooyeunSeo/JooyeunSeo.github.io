---
title: "Skill notes for coding test"
header:
  image: /assets/images/defaults/header-main.png
layout: archive
permalink: /skill-notes/
---

{% assign category_name = "Skill-Notes" %}

{% assign filtered_posts = site.posts | where: "categories", category_name %}

{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}