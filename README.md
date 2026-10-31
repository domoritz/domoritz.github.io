# Website

## Paper previews

Publication lists and Featured Publications share first-page AVIF thumbnails.
The images and `_data/publication_previews.json` are checked in, so site builds
do not fetch or render PDFs. To generate previews for new papers:

```sh
python -m venv /tmp/paper-previews-venv
/tmp/paper-previews-venv/bin/pip install -r scripts/requirements-paper-previews.txt
/tmp/paper-previews-venv/bin/python scripts/generate-paper-previews.py
```

The generator prefers local PDFs, then downloads linked PDFs or arXiv papers.
Existing previews are reused; use `--force` to refresh them, or
`--only 2023-mosaic --source papers/2023-Mosaic-VIS.pdf` to supply a PDF explicitly.
Entries without public PDFs stay text-only. Downloads are cached in the system
temporary directory. Commit the generated images and manifest together.
For papers in a combined proceedings PDF, set `preview_page` in the publication
front matter to the paper's page number (starting at 1).

## Write

```
bundle exec jekyll post "My New Post"
```

## Run

```
bundle exec jekyll serve --livereload
```

## Run with Docker

```
docker run \
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 -p 35729:35729 \
  -it jekyll/jekyll \
  jekyll serve --livereload
```
