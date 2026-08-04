#!/usr/bin/env python3
"""
Voegt Jekyll front matter toe aan alle .md-bestanden in termen/ die dit nog
niet hebben. Zonder front matter negeert GitHub Pages/Jekyll deze bestanden
niet als pagina (ze worden dan niet meegenomen of niet mooi weergegeven).

Gebruik: plaats dit script in de root van de repo (naast de map 'termen')
en voer uit met: python3 add_front_matter.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET_DIR = ROOT / "termen"


def has_front_matter(text: str) -> bool:
    return text.lstrip().startswith("---")


def make_title(stem: str) -> str:
    return stem.replace("_", " ").replace("-", " ").strip()


def main() -> None:
    if not TARGET_DIR.exists():
        print(f"Map niet gevonden: {TARGET_DIR}")
        return

    count = 0
    for md_file in sorted(TARGET_DIR.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        if has_front_matter(text):
            continue
        title = make_title(md_file.stem)
        front_matter = f"---\ntitle: {title}\nlayout: page\n---\n\n"
        md_file.write_text(front_matter + text, encoding="utf-8")
        count += 1
        print(f"Front matter toegevoegd: {md_file.relative_to(ROOT)}")

    print(f"\nKlaar. {count} bestand(en) aangepast.")


if __name__ == "__main__":
    main()
