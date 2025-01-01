---
title: "Blog with Jekyll"
header:
  image: /assets/images/defaults/header-main.png
layout: archive
permalink: /etc-Jekyll/
---

{% assign category_name = "Jekyll" %}

{% assign filtered_posts = site.posts | where: "categories", category_name %}

{% for post in filtered_posts %}
  {% include archive-single.html %}
{% endfor %}