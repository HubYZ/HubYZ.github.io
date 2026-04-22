---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Edit `_data/publications.tsv` to add or update papers. Each row will generate one publication page automatically when the site is built.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
