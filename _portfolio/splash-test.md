---
title: "스플래시 페이지 제목"
layout: splash
permalink: /splash-page/
date: 2016-03-23T11:48:41-04:00
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/unsplash-image-1.jpg
  actions:
    - label: "Download"
      url: "https://github.com/mmistakes/minimal-mistakes/"
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
excerpt: "부제목"

intro: 
  - excerpt: 'asdghkjtyugdf'
feature_row:
  - image_path: assets/images/foo-bar-identity-th.jpg
    alt: "placeholder image 1"
    title: "Placeholder 1"
    excerpt: "tjutyhjgdhj"
  - image_path: assets/images/foo-bar-identity-th.jpg
    image_caption: "Image courtesy of [Unsplash](https://unsplash.com/)"
    alt: "placeholder image 2"
    title: "Placeholder 2"
    excerpt: "asdfasdfasdfasdtehdfgdfg"
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
  - image_path: assets/images/foo-bar-identity-th.jpg
    title: "Placeholder 3"
    excerpt: "thdfgdsfgsd"
feature_row2:
  - image_path: assets/images/foo-bar-identity-th.jpg
    alt: "placeholder image 2"
    title: "Placeholder Image Left Aligned"
    excerpt: 'dfsdfsdfsd'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row3:
  - image_path: assets/images/foo-bar-identity-th.jpg
    alt: "placeholder image 2"
    title: "Placeholder Image Right Aligned"
    excerpt: 'wsetqwrtgaerfasdf'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
feature_row4:
  - image_path: assets/images/foo-bar-identity-th.jpg
    alt: "placeholder image 2"
    title: "Placeholder Image Center Aligned"
    excerpt: 'asdfasdfasdfasdf'
    url: "#test-link"
    btn_label: "Read More"
    btn_class: "btn--primary"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

{% include feature_row id="feature_row2" type="left" %}

{% include feature_row id="feature_row3" type="right" %}

{% include feature_row id="feature_row4" type="center" %}