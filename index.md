---
layout: page
title: Home
---

# Lexicon Vooronderzoek

Ruimte om een lexicon voor onderzoek in te ontwikkelen.

## Termen

{% assign termen = site.pages | where_exp: "p", "p.path contains 'termen/'" | sort: "title" %}
<ul>
{% for term in termen %}
  <li><a href="{{ term.url | relative_url }}">{{ term.title | default: term.name }}</a></li>
{% endfor %}
</ul>
