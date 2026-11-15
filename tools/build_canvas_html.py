#!/usr/bin/env python3
"""
Builds Canvas-ready HTML from the course's Markdown pages.

The Markdown files are the source. This script writes an HTML copy of each
page into "Canvas HTML/", ready to paste into the Canvas HTML editor (</>).

What it changes for Canvas and for accessibility:
  - Removes the front matter and the page's top heading (Canvas shows the
    page title itself, and page content should start at heading level 2).
  - Gives every table a caption, taken from the heading above it, and marks
    the header cells with scope="col".
  - Adds visible borders and padding to tables with inline styles, because
    Canvas removes <style> blocks.
  - Turns Obsidian callouts into plain block quotes with a bold title.
  - Turns check-box lists into ordinary lists.

Run from the repository root:   python3 tools/build_canvas_html.py
Needs:                          pip install markdown-it-py beautifulsoup4
"""
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Canvas HTML"
SOURCES = ["Class Pages", "Exercises", "Schedule"]

TABLE_STYLE = "border-collapse: collapse; width: 100%;"
CELL_STYLE = "border: 1px solid #6b6b6b; padding: 6px 8px; text-align: left; vertical-align: top;"
HEAD_STYLE = CELL_STYLE + " background-color: #f0f0f0;"
CAPTION_STYLE = "text-align: left; font-weight: bold; padding: 4px 0;"

md = MarkdownIt("commonmark").enable("table")


def strip_front_matter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def plain(text):
    return re.sub(r"\s+", " ", text).strip()


def convert(text):
    text = strip_front_matter(text)
    # Check-box lists become ordinary lists.
    text = re.sub(r"^(\s*)- \[[ xX]\] ", r"\1- ", text, flags=re.M)

    soup = BeautifulSoup(md.render(text), "html.parser")

    # Canvas shows the page title, so drop the page's own top heading.
    page_title = ""
    first_h1 = soup.find("h1")
    if first_h1 is not None:
        page_title = plain(first_h1.get_text())
        first_h1.decompose()

    # Obsidian callouts:  > [!info] Title
    for quote in soup.find_all("blockquote"):
        first = quote.find("p")
        if first is None:
            continue
        html = first.decode_contents()
        match = re.match(r"\s*\[!(\w+)\]\s*([^\n<]*)", html)
        if match:
            title = match.group(2).strip() or match.group(1).capitalize()
            rest = html[match.end():].lstrip("\n")
            new_html = f"<strong>{title}</strong>" + (f"<br>{rest}" if rest.strip() else "")
            first.clear()
            first.append(BeautifulSoup(new_html, "html.parser"))

    # Tables: caption, header scope, visible borders.
    used = {}
    for table in soup.find_all("table"):
        heading = table.find_previous(["h2", "h3", "h4"])
        caption_text = plain(heading.get_text()) if heading is not None else page_title or "Table"
        used[caption_text] = used.get(caption_text, 0) + 1
        if used[caption_text] > 1:
            caption_text = f"{caption_text} ({used[caption_text]})"

        table["style"] = TABLE_STYLE
        caption = soup.new_tag("caption", style=CAPTION_STYLE)
        caption.string = caption_text
        table.insert(0, caption)

        for cell in table.find_all("th"):
            cell["scope"] = "col"
            cell["style"] = HEAD_STYLE
        for cell in table.find_all("td"):
            cell["style"] = CELL_STYLE

    return str(soup).strip() + "\n"


def main():
    count = 0
    for folder in SOURCES:
        for source in sorted((ROOT / folder).glob("*.md")):
            target = OUT / folder / (source.stem + ".html")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(convert(source.read_text(encoding="utf-8")), encoding="utf-8")
            count += 1
    print(f"Wrote {count} HTML files to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
