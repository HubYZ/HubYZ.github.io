---
permalink: /
title: "Publications"
excerpt: "Publication list"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

This website is configured for publications only.

Please edit `_data/publications.tsv` to add or update papers. Each row will automatically generate one publication page during the GitHub Pages build.

{% if author.googlescholar %}
You can also find my articles on [Google Scholar]({{ author.googlescholar }}).
{% endif %}

[View all publications]({{ '/publications/' | relative_url }})
