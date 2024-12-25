---
title: "Test"
layout: archive
permalink: /대분류1-Test/
---

{% assign category_name = "Test" %}

{% assign filtered_posts = site.posts | where: "categories", category_name %}

{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}