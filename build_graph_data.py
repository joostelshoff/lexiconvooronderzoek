#!/usr/bin/env python3
"""
Bouwt assets/graph-data.json: een lijst van nodes (alle termen) en links
(alle [[wikilink]]-verwijzingen ertussen), zodat de site een Obsidian-achtige
graph-weergave kan tonen.

Gebruik: plaats dit script in de root van de repo en voer uit met:
    python3 build_graph_data.py

Draai dit script elke keer opnieuw nadat je termen hebt toegevoegd, verwijderd
of van links voorzien, en commit het aangepaste graph-data.json bestand mee.
"""
import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {".git", "_site", "node_modules"}
SKIP_STEMS = {"allterms"}  # niet-inhoudelijke Obsidian-bestanden (bv. dataview-queries)

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
PREFERRED_TERM_RE = re.compile(r"^preferred_term:\s*(.+?)\s*$", re.MULTILINE)
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]")


def find_all_md_files():
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.stem.lower() in SKIP_STEMS:
            continue
        yield path


def parse_file(path):
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    front_matter, body = (match.group(1), match.group(2)) if match else ("", text)

    title_match = TITLE_RE.search(front_matter)
    if title_match:
        title = title_match.group(1).strip('"\'')
    else:
        preferred_match = PREFERRED_TERM_RE.search(front_matter)
        if preferred_match:
            title = preferred_match.group(1).strip('"\'')
        else:
            heading_match = HEADING_RE.search(body)
            title = heading_match.group(1).strip() if heading_match else path.stem

    return title, body


def main():
    files = list(find_all_md_files())

    # key (lowercase stem) -> {id, label, url}
    nodes_by_key = {}
    for path in files:
        rel = path.relative_to(ROOT)
        title, _ = parse_file(path)
        url = "/" + str(rel.with_suffix(".html")).replace("\\", "/")
        url = urllib.parse.quote(url, safe="/()")
        key = path.stem.lower()
        nodes_by_key[key] = {"id": key, "label": title, "url": url}

    links = []
    seen_links = set()
    for path in files:
        source_key = path.stem.lower()
        _, body = parse_file(path)
        for match in WIKILINK_RE.finditer(body):
            target = match.group(1).strip().lower()
            if target not in nodes_by_key:
                continue  # verwijzing naar een term zonder eigen pagina
            if target == source_key:
                continue  # geen zelf-verwijzingen
            pair = tuple(sorted((source_key, target)))
            if pair in seen_links:
                continue
            seen_links.add(pair)
            links.append({"source": source_key, "target": target})

    data = {
        "nodes": list(nodes_by_key.values()),
        "links": links,
    }

    out_dir = ROOT / "assets"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "graph-data.json"
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{len(data['nodes'])} termen, {len(data['links'])} links.")
    print(f"Geschreven naar: {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
