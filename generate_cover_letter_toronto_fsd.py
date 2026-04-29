#!/usr/bin/env python3
"""Generate a PDF cover letter for City of Toronto Fleet Services – Data Specialist (64089)."""

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY

# Job posting: Data Specialist, Job ID 64089, Fleet Services (posting 23-Apr-2026 to 07-May-2026)
OUTPUT = "Barzegari_Cover_Letter_Data_Specialist_64089.pdf"

def build_story():
    styles = getSampleStyleSheet()
    normal = ParagraphStyle(
        "CLNormal",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1e293b"),
        alignment=TA_JUSTIFY,
        spaceAfter=10,
    )
    header = ParagraphStyle(
        "CLHeader",
        parent=normal,
        fontName="Helvetica-Bold",
        fontSize=12,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=2,
    )
    subhead = ParagraphStyle(
        "CLSub",
        parent=normal,
        fontSize=10,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=20,
    )
    to_block = ParagraphStyle(
        "CLTo",
        parent=normal,
        spaceAfter=16,
    )
    re_line = ParagraphStyle(
        "CLRe",
        parent=normal,
        fontName="Helvetica-Bold",
        spaceAfter=12,
    )
    sign = ParagraphStyle(
        "CLSign",
        parent=normal,
        spaceBefore=6,
    )

    story = []
    story.append(Paragraph("Vahed Barzegari", header))
    story.append(Paragraph("Toronto, Canada  |  vahed@yorku.ca", subhead))
    story.append(Spacer(1, 0.05 * inch))
    story.append(Paragraph("24 April 2026", normal))

    story.append(Paragraph(
        "Hiring Committee<br/>"
        "City of Toronto - Fleet Services Division<br/>"
        "Fleet Services, Business Management (Fleet Business Intelligence and Reporting)<br/>"
        "843 Eastern Avenue; other work locations as assigned, including the Union Station area",
        to_block,
    ))
    story.append(Paragraph("Re: Data Specialist (Job ID: 64089) - Full-Time, Temporary (24 months)", re_line))
    story.append(Paragraph("Dear Members of the Hiring Committee,", normal))

    p1 = (
        "I am writing to express my interest in the <b>Data Specialist</b> position (Job ID 64089) with "
        "<b>Fleet Services, Business Management</b>, reporting to the Manager, Fleet Business Intelligence and Reporting. "
        "The role's focus on building and sustaining advanced analytics capacity, high-performing data pipelines, and "
        "reliable ETL/ELT and reporting for large municipal datasets closely matches my experience turning complex "
        "operational and spatial data into decision-ready insight in a public-sector, Toronto context."
    )
    story.append(Paragraph(p1, normal))

    p2 = (
        "I hold a <b>PhD in Civil Engineering (Transportation)</b> and work as a <b>Data Scientist and Postdoctoral Fellow</b> "
        "at York University, specializing in data-driven methods for public transportation, fleet electrification, and "
        "urban systems. I use <b>Python, SQL, and GIS</b> extensively (including spatial data, mapping, and network analysis), "
        "and I apply <b>statistics, optimization, and predictive modelling</b> to large structured and sensor-oriented datasets "
        "such as real-time GTFS, GPS-relevant feed data, and electrification and charging scenarios. I have validated "
        "electric bus allocation and charging decision-support with <b>TTC operations</b>, built decision tools used for "
        "transit service reliability, and published peer-reviewed work on large-scale system analysis. That experience "
        "translates well to FSD's fleet assets, work management, and sustainability and infrastructure priorities. I hold "
        "a professional credential in <b>Databases and SQL for Data Science (IBM / Coursera)</b> and I document models, code, and "
        "assumptions to support governance and handoff. I have developed interactive dashboards and analytical outputs for "
        "technical and non-technical audiences and am ready to deepen my use of <b>Tableau, Power BI,</b> and corporate BI "
        "platforms in a dedicated Fleet Business Intelligence environment."
    )
    story.append(Paragraph(p2, normal))

    p3 = (
        "I have a demonstrated record of collaboration with the City's ecosystem: work linked to the <b>Headway Management / "
        "bunching pilot</b> and related analytics has been recognized through the <b>City of Toronto Open Data Challenge "
        "(1st place, 2026)</b> and professional awards, reflecting a commitment to <b>data quality, root-cause analysis, and "
        "actionable reporting</b>. I am motivated by FSD's leadership of Canada's largest municipal fleet, the Sustainable "
        "Fleet plan, and safety and compliance mandates, and I am prepared to work cross-functionally with corporate partners "
        "on data governance, performance of high-volume ETL/ELT, and clear communication to management and Council-facing "
        "materials when required."
    )
    story.append(Paragraph(p3, normal))

    p4 = (
        "I would welcome an interview to discuss how my background in <b>advanced analytics, geospatial and fleet-relevant "
        "modelling, and municipal-scale data pipelines</b> can support Fleet Services. Thank you for your consideration of "
        "my application for the <b>Non-Union, 35 hours per week (Monday to Friday)</b> position posted until 7 May 2026."
    )
    story.append(Paragraph(p4, normal))

    story.append(Paragraph("Sincerely,", sign))
    story.append(Spacer(1, 0.35 * inch))
    story.append(Paragraph("Vahed Barzegari", normal))
    return story


def main():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        rightMargin=0.85 * inch,
        leftMargin=0.85 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )
    doc.build(build_story())
    print(f"Wrote: {OUTPUT}")


if __name__ == "__main__":
    main()
