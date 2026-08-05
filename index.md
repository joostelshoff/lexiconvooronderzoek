---
layout: page
title: Home
---

# Lexicon voor Onderzoek

Ruimte om een lexicon voor onderzoek in te ontwikkelen.

## Archetypes
{% assign archetypes = site.pages | where_exp: "p", "p.path contains 'archetypes/'" | sort: "title" %}
<ul>
{% for archetype in archetypes %}
  <li><a href="{{ archetype.url | relative_url }}">{{ archetype.title | default: archetype.name }}</a></li>
{% endfor %}
</ul>

## Termen

{% assign termen = site.pages | where_exp: "p", "p.path contains 'termen/'" | sort: "title" %}
<ul>
{% for term in termen %}
  <li><a href="{{ term.url | relative_url }}">{{ term.title | default: term.name }}</a></li>
{% endfor %}
</ul>
