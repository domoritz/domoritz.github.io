#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "PyMuPDF>=1.26,<3",
#     "Pillow>=11.3,<14",
#     "PyYAML>=6,<7",
# ]
# ///
"""Render public papers' first pages to small, static AVIF thumbnails."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from pathlib import Path
import tempfile
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import pymupdf
from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "images/papers"
IMAGE_WIDTH = 192  # 2x the displayed width of 96 CSS pixels.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Regenerate existing previews")
    parser.add_argument("--only", help="Publication filename stem to render")
    parser.add_argument("--source", help="Override PDF URL/path (requires --only)")
    args = parser.parse_args()
    if args.source and not args.only:
        parser.error("--source requires --only")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    fallback = OUTPUT / "fallback.avif"
    if args.force or not fallback.exists():
        with pymupdf.open(ROOT / "scripts/paper-preview-sources/fallback.svg") as svg:
            with pymupdf.open(stream=svg.convert_to_pdf(), filetype="pdf") as document:
                page = document[0]
                scale = IMAGE_WIDTH / page.rect.width
                pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
                Image.open(BytesIO(pixmap.tobytes("png"))).convert("RGB").save(fallback, "AVIF", quality=55, speed=6)
    cache = Path(tempfile.gettempdir()) / "domoritz-paper-pdfs"
    cache.mkdir(exist_ok=True)
    failures = []

    def render(path):
        slug = path.stem
        target = OUTPUT / f"{slug}.avif"
        if target.exists() and not args.force and not args.source:
            return slug, None, None
        pub = yaml.safe_load(path.read_text().split("---", 2)[1])
        if pub.get("preview_image") and not args.source:
            return slug, ((ROOT / pub["preview_image"]).read_bytes(), None), None
        sources = []
        if args.source:
            sources.append(args.source)
        if pub.get("pdf"):
            sources.append(pub["pdf"])
        if pub.get("arxiv"):
            sources.append(f"https://arxiv.org/pdf/{pub['arxiv']}")
        if not sources:
            return slug, None, "no public PDF linked"
        errors = []
        for source in dict.fromkeys(sources):
            try:
                parsed = urlparse(source)
                local = ROOT / parsed.path.lstrip("/")
                # Prefer checked-in PDFs, including copies with the same filename.
                if not local.is_file():
                    local = ROOT / "papers" / Path(parsed.path).name
                cached = cache / f"{slug}.pdf"
                if local.is_file():
                    data = local.read_bytes()
                elif cached.exists() and not args.source:
                    data = cached.read_bytes()
                else:
                    url = source.replace("http://", "https://", 1)
                    url = url.replace("www.arxiv.org/", "arxiv.org/").replace("arxiv.org/abs/", "arxiv.org/pdf/")
                    request = Request(url, headers={"User-Agent": "domoritz-paper-previews/1.0"})
                    with urlopen(request, timeout=45) as response:
                        data = response.read()
                    if not data.startswith(b"%PDF"):
                        raise ValueError("response is not a PDF")
                    cached.write_bytes(data)
                # MuPDF rendering is serialized below: it is not thread-safe.
                return slug, (data, pub.get("preview_page", 1)), None
            except Exception as error:
                errors.append(f"{source}: {error}")
        return slug, None, "; ".join(errors)

    paths = sorted((ROOT / "_publications").glob("*.html"))
    if args.only:
        paths = [p for p in paths if p.stem == args.only]
        if not paths:
            parser.error("Unknown publication")
    with ThreadPoolExecutor(max_workers=4) as pool:
        for slug, result, error in pool.map(render, paths):
            if error:
                failures.append((slug, error))
                print(f"SKIP {slug}: {error}", flush=True)
                continue
            if result is None:
                continue
            data, page_number = result
            if page_number is None:
                with Image.open(BytesIO(data)) as original:
                    image = original.convert("RGB")
                    image = image.resize((IMAGE_WIDTH, round(image.height * IMAGE_WIDTH / image.width)), Image.Resampling.LANCZOS)
            else:
                with pymupdf.open(stream=data, filetype="pdf") as document:
                    page = document[page_number - 1]
                    scale = IMAGE_WIDTH / page.rect.width
                    pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
                    image = Image.open(BytesIO(pixmap.tobytes("png"))).convert("RGB")
            target = OUTPUT / f"{slug}.avif"
            image.save(target, "AVIF", quality=55, speed=6)
            print(f"OK {slug}: {target.stat().st_size} bytes", flush=True)
    preview_count = sum(path.name != "fallback.avif" for path in OUTPUT.glob("*.avif"))
    print(f"{preview_count} previews available; {len(failures)} entries skipped.")
    # Entries without a linked PDF use the fallback; linked PDFs that fail need attention.
    if any(error != "no public PDF linked" for _, error in failures):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
