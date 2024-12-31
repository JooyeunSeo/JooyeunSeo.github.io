---
title: "test"
header:
  image: /assets/images/defaults/header-main.png
layout: archive
permalink: /etc-test/
---

{% assign category_name = "test" %}

{% assign filtered_posts = site.posts | where: "categories", category_name %}

{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}