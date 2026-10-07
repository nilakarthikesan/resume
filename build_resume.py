#!/usr/bin/env python3
"""Build the public resume PDF from its versioned, editable source."""
from html import escape
from pathlib import Path
import json

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parent
WIDTH, HEIGHT = letter
LEFT, RIGHT, TOP, BOTTOM = 36, 36, 32, 29
CONTENT_WIDTH = WIDTH - LEFT - RIGHT
BODY_SIZE = 9.0
BODY_LEADING = 10.0


def register_serif_fonts():
    """Embed locally installed fonts when available; retain PDF standard fallback."""
    candidates = (
        (Path("/System/Library/Fonts/Supplemental"),
         ("Times New Roman.ttf", "Times New Roman Bold.ttf", "Times New Roman Italic.ttf",
          "Times New Roman Bold Italic.ttf")),
        (Path("/usr/share/fonts/truetype/liberation2"),
         ("LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf", "LiberationSerif-Italic.ttf",
          "LiberationSerif-BoldItalic.ttf")),
        (Path("/usr/share/fonts/truetype/liberation"),
         ("LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf", "LiberationSerif-Italic.ttf",
          "LiberationSerif-BoldItalic.ttf")),
    )
    for directory, filenames in candidates:
        if all((directory / filename).is_file() for filename in filenames):
            for name, filename in zip(("Times-Roman", "Times-Bold", "Times-Italic", "Times-BoldItalic"),
                                      filenames):
                pdfmetrics.registerFont(TTFont(name, str(directory / filename)))
            pdfmetrics.registerFontFamily("Times-Roman", normal="Times-Roman", bold="Times-Bold",
                                          italic="Times-Italic", boldItalic="Times-BoldItalic")
            print(f"Embedded serif fonts from {directory}")
            return
    print("Using PDF standard Times fonts; install Liberation Serif for embedded fonts.")


register_serif_fonts()

STYLES = {
    "body": ParagraphStyle("body", fontName="Times-Roman", fontSize=BODY_SIZE,
                           leading=BODY_LEADING, textColor=colors.black),
    "title": ParagraphStyle("title", fontName="Times-Bold", fontSize=9.5,
                            leading=10.5),
    "subtitle": ParagraphStyle("subtitle", fontName="Times-Italic", fontSize=9.0,
                               leading=9.8),
    "name": ParagraphStyle("name", fontName="Times-Bold", fontSize=23,
                           leading=26, alignment=TA_CENTER),
    "contact": ParagraphStyle("contact", fontName="Times-Roman", fontSize=8.9,
                              leading=11, alignment=TA_CENTER),
}


def build():
    data = json.loads((ROOT / "resume.json").read_text())
    output = ROOT / "Resume_Official.pdf"
    pdf = canvas.Canvas(str(output), pagesize=letter, invariant=1)
    pdf.setTitle(f'{data["name"]} - Resume')
    pdf.setAuthor(data["name"])
    pdf.setSubject("Professional resume; research project protocol added October 2026")
    y = HEIGHT - TOP

    def paragraph(text, style="body", x=LEFT, width=CONTENT_WIDTH):
        nonlocal y
        p = Paragraph(text, STYLES[style])
        _, height = p.wrap(width, HEIGHT)
        p.drawOn(pdf, x, y - height)
        y -= height

    def row(text, right="", style="title", inset=10):
        nonlocal y
        s = STYLES[style]
        right_font = "Times-Roman" if style == "title" else "Times-Italic"
        right_width = stringWidth(right, right_font, s.fontSize) + 10 if right else 0
        p = Paragraph(text, STYLES[style])
        _, height = p.wrap(CONTENT_WIDTH - inset - right_width, HEIGHT)
        p.drawOn(pdf, LEFT + inset, y - height)
        if right:
            pdf.setFont(right_font, s.fontSize)
            pdf.drawRightString(WIDTH - RIGHT - 5, y - s.fontSize, right)
        y -= height

    def section(label):
        nonlocal y
        y -= 4
        pdf.setFont("Times-Roman", 11.25)
        pdf.drawString(LEFT, y - 11.25, label.upper())
        y -= 13
        pdf.setLineWidth(0.5)
        pdf.line(LEFT, y, WIDTH - RIGHT, y)
        y -= 3

    def entry(item, project=False):
        nonlocal y
        if item.get("inline_subtitle"):
            row(f'{escape(item["title"])} <font name="Times-Roman">|</font> '
                f'<font name="Times-Italic" size="9">{item["subtitle"]}</font>',
                item.get("right", ""))
        else:
            row(escape(item["title"]), item.get("right", ""))
        if project and not item.get("inline_subtitle"):
            row(item["subtitle"], style="subtitle")
        elif not project:
            row(escape(item["subtitle"]), item.get("dates", ""), style="subtitle")
        for bullet in item["bullets"]:
            p = Paragraph(bullet, STYLES["body"])
            _, height = p.wrap(CONTENT_WIDTH - 32, HEIGHT)
            pdf.circle(LEFT + 22, y - BODY_SIZE + 3, 1.0, stroke=0, fill=1)
            p.drawOn(pdf, LEFT + 32, y - height)
            y -= height + 0.5
        y -= 1

    paragraph(escape(data["name"]), "name")
    contacts = [escape(data["phone"])] + [
        f'<a href="{escape(item["url"], quote=True)}"><u>{escape(item["label"])}</u></a>'
        for item in data["contact"]
    ]
    paragraph(" | ".join(contacts), "contact")
    y -= 3

    for label, key in (("Education", "education"), ("Experience", "experience"),
                       ("Projects", "projects")):
        section(label)
        for item in data[key]:
            entry(item, project=(key == "projects"))

    section("Technical Skills")
    for line in data["skills"]:
        paragraph(line, x=LEFT + 10, width=CONTENT_WIDTH - 10)

    if y < BOTTOM:
        raise ValueError(f"Resume exceeds one-page content area by {BOTTOM - y:.1f} pt. "
                         "Edit content or spacing; do not silently clip text.")
    pdf.showPage()
    pdf.save()
    print(f"Built {output.name}: 1 page, {y:.1f} pt bottom clearance")


if __name__ == "__main__":
    build()
