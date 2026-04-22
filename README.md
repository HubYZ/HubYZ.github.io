# Publications only GitHub Pages template

This version keeps only the publications workflow.

## What you edit

1. `_config.yml`
   Update your site title, URL, repository, and sidebar author information.

2. `_data/publications.tsv`
   Each row is one paper.

3. `publication/<url_slug>/paper.pdf`
   Put the PDF for each paper in its matching folder.

## Automatic generation

`python3 scripts/generate_publications.py`

This script reads `_data/publications.tsv` and generates one markdown page per paper in `_publications/`.

## GitHub Pages

The repository includes `.github/workflows/deploy.yml`.
After you push to GitHub and enable Pages with `GitHub Actions`, the workflow will:

1. generate publication pages
2. build the Jekyll site
3. deploy the site to GitHub Pages

## Google Scholar related fields

The HTML head of each publication page includes Scholar friendly citation tags such as:

- `citation_title`
- `citation_author`
- `citation_publication_date`
- `citation_abstract_html_url`
- `citation_pdf_url`
- `citation_journal_title`
- `citation_conference_title`
- `citation_doi`

## TSV columns

Required columns:

- `pub_date`
- `url_slug`
- `title`
- `authors`
- `venue`
- `abstract`
- `pdf_file_name`

Optional columns:

- `publication_type`
- `journal_title`
- `conference_title`
- `volume`
- `issue`
- `firstpage`
- `lastpage`
- `doi`
- `citation_text`
- `code_url`
- `project_url`
