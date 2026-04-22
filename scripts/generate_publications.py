#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "_data" / "publications.tsv"
OUTPUT_DIR = ROOT / "_publications"


def clean(value: str | None) -> str:
    return (value or "").strip()


def yaml_quote(value: str) -> str:
    value = value.replace('"', '\\"')
    return f'"{value}"'


def yaml_block(value: str, indent: int = 0) -> str:
    prefix = " " * indent
    lines = value.splitlines() or [""]
    return "|-\n" + "\n".join(f"{prefix}  {line}" for line in lines)


def excerpt_from_abstract(text: str, limit: int = 280) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def make_front_matter(row: Dict[str, str]) -> str:
    title = clean(row.get("title"))
    slug = clean(row.get("url_slug"))
    pub_date = clean(row.get("pub_date"))
    venue = clean(row.get("venue"))
    abstract = clean(row.get("abstract"))
    citation_text = clean(row.get("citation_text"))
    pdf_file_name = clean(row.get("pdf_file_name")) or "paper.pdf"
    pdf_url = f"/publication/{slug}/{pdf_file_name}"

    lines: List[str] = [
        "---",
        f"title: {yaml_quote(title)}",
        "collection: publications",
        f"permalink: /publication/{slug}/",
        f"date: {pub_date}",
        f"venue: {yaml_quote(venue)}",
        f"pdf_url: {yaml_quote(pdf_url)}",
        f"paperurl: {yaml_quote(pdf_url)}",
    ]

    authors = [a.strip() for a in clean(row.get("authors")).split(";") if a.strip()]
    if authors:
        lines.append("authors:")
        for author in authors:
            lines.append(f"  - {yaml_quote(author)}")

    if abstract:
        lines.append(f"excerpt: {yaml_quote(excerpt_from_abstract(abstract))}")
        lines.append("abstract: " + yaml_block(abstract))

    if citation_text:
        lines.append("citation: " + yaml_block(citation_text))

    field_map = {
        "journal_title": "citation_journal_title",
        "conference_title": "citation_conference_title",
        "volume": "citation_volume",
        "issue": "citation_issue",
        "firstpage": "citation_firstpage",
        "lastpage": "citation_lastpage",
        "doi": "citation_doi",
        "code_url": "code_url",
        "project_url": "project_url",
        "publication_type": "publication_type",
    }
    for source_key, target_key in field_map.items():
        value = clean(row.get(source_key))
        if value:
            lines.append(f"{target_key}: {yaml_quote(value)}")

    lines.append("---")
    return "\n".join(lines)


def make_body(row: Dict[str, str]) -> str:
    sections: List[str] = []

    links: List[str] = ["[PDF]({{ page.paperurl | relative_url }})"]
    doi = clean(row.get("doi"))
    if doi:
        links.append(f"[DOI](https://doi.org/{doi})")
    if clean(row.get("code_url")):
        links.append(f"[Code]({clean(row.get('code_url'))})")
    if clean(row.get("project_url")):
        links.append(f"[Project]({clean(row.get('project_url'))})")
    sections.append(" ".join(links))

    citation_text = clean(row.get("citation_text"))
    if citation_text:
        sections.append("### Citation\n" + citation_text)

    return "\n\n".join(sections).strip() + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for path in OUTPUT_DIR.glob("autogen-*.md"):
        path.unlink()

    with DATA_FILE.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = list(reader)

    for row in rows:
        slug = clean(row.get("url_slug"))
        title = clean(row.get("title"))
        pub_date = clean(row.get("pub_date"))
        if not slug or not title or not pub_date:
            raise ValueError("Each row must include pub_date, url_slug, and title.")

        output_path = OUTPUT_DIR / f"autogen-{pub_date}-{slug}.md"
        output_path.write_text(make_front_matter(row) + "\n" + make_body(row), encoding="utf-8")
        print(f"Generated {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
