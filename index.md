---
layout: page
title: Home
---

# Lexicon voor Onderzoek

Ruimte om een lexicon voor onderzoek in te ontwikkelen, gebaseerd op open informatie.

## Archetypes

{% assign archetypen = site.pages | where_exp: "p", "p.path contains 'archetypes/'" | sort: "title" %}
<ul>
{% for term in archetypen %}
  <li><a href="{{ term.url | relative_url }}">{{ term.title | default: term.preferred_term | default: term.name }}</a></li>
{% endfor %}
</ul>

## Termen

{% assign termen = site.pages | where_exp: "p", "p.path contains 'termen/'" | sort: "title" %}
<ul>
{% for term in termen %}
  <li><a href="{{ term.url | relative_url }}">{{ term.title | default: term.preferred_term | default: term.name }}</a></li>
{% endfor %}
</ul>

## Docs
{% assign docs = site.pages | where_exp: "p", "p.path contains 'docs/'" | sort: "title" %}
<ul>
{% for term in docs %}
  <li><a href="{{ term.url | relative_url }}">{{ term.title | default: term.preferred_term | default: term.name }}</a></li>
{% endfor %}
</ul>
