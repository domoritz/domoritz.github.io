# Website

## Paper previews

The Publications page shows pre-rendered AVIF paper thumbnails.
Previews are hidden on mobile (600px and below) to leave the text full width.
Images are checked in as `images/papers/<publication-filename>.avif`, so site builds
do not fetch or render PDFs. Links and rendering sources come from each publication's
front matter. To generate previews for new papers:

```sh
uv run --with-requirements scripts/requirements-paper-previews.txt scripts/generate-paper-previews.py
```

The generator prefers local PDFs, then downloads linked PDFs or arXiv papers.
Existing previews are reused; use `--force` to refresh them, or
`--only 2023-mosaic --source papers/2023-Mosaic-VIS.pdf` to supply a PDF explicitly.
Entries without previews use a shared generic AVIF paper image.
The generator also renders this fallback from its checked-in SVG source.
Downloads are cached in the system
temporary directory. Commit the generated images with their publication entries.
For papers in a combined proceedings PDF, set `preview_page` in the publication
front matter to the paper's page number (starting at 1).
For a supplied cover image without a public PDF, set `preview_image` to its
repository-relative path. Keep these originals in `scripts/paper-preview-sources/`,
which is excluded from the built site; the preview is displayed without a PDF link.

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
