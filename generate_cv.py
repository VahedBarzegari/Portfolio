#!/usr/bin/env python3
"""
Generate a professional CV PDF from portfolio data
"""

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
except ImportError:
    print("reportlab is not installed. Installing...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

from datetime import datetime

# CV Data extracted from HTML
CV_DATA = {
    "name": "Vahed Barzegari",
    "title": "Data Scientist & Post Doctoral Fellow",
    "email": "vahed@yorku.ca",
    "location": "Toronto, Canada",
    "linkedin": "linkedin.com/in/vahed-barzegari-bafghi-214936228",
    "github": "github.com/VahedBarzegari",
    "google_scholar": "scholar.google.ca/citations?user=JHjxrhYAAAAJ",
    
    "summary": """I am a Data Scientist at Interactive-OR Lab and a Post Doctoral Fellow at York University, specializing in transportation engineering and operations research. With a PhD in Civil Engineering – Transportation from K.N. Toosi University of Technology, I focus on developing data-driven solutions for public transportation systems, transit electrification, and urban accessibility challenges. My research bridges optimization theory and practical applications, creating interactive tools and decision-support systems that help transit agencies make informed decisions.""",
    
    "education": [
        {
            "degree": "Doctor of Philosophy (PhD)",
            "field": "Civil Engineering – Transportation",
            "institution": "K. N. Toosi University of Technology",
            "location": "Tehran, Iran",
            "period": "September 2017 – February 2023"
        },
        {
            "degree": "Master of Science (MSc)",
            "field": "Civil Engineering – Transportation Planning",
            "institution": "K.N. Toosi University of Technology",
            "location": "Tehran, Iran",
            "period": "September 2015 – September 2017"
        },
        {
            "degree": "Bachelor of Science (BSc)",
            "field": "Civil Engineering",
            "institution": "K.N. Toosi University of Technology",
            "location": "Tehran, Iran",
            "period": "September 2011 – August 2015"
        }
    ],
    
    "experience": [
        {
            "title": "Research Assistant (Post Doctoral Fellow)",
            "company": "York University",
            "location": "Toronto, Canada",
            "period": "July 2024 – Present",
            "bullets": [
                "Developed an interactive 15-minute city accessibility toolkit using Python Shiny and OpenStreetMap, integrating census data to analyse amenity distribution, population needs, and multimodal access across Toronto.",
                "Designed and validated novel duplication indicators (segment- and passenger-based) to evaluate network efficiency, providing evidence-based policy recommendations for urban transit in Almaty.",
                "Engineered an extended data specification (TPFS) enhancing GTFS by incorporating Revenue, Non-Revenue, and Ridership feeds, and demonstrated practical implementation with DART case study.",
                "Developed an integrated optimization framework for charger deployment, fleet type selection, and scheduling, applying it to 20 major transit networks to evaluate electrification strategies.",
                "Built a mixed-integer optimization model and interactive decision-support tool for electric bus allocation and charging, enabling scenario-based planning and validated with TTC operations.",
                "Created predictive analytics methods using real-time GTFS data to detect and mitigate bus bunching/gapping, enhancing service reliability and operational planning."
            ]
        },
        {
            "title": "Civil Technician",
            "company": "Madanchian Chogharat Civil and Development Cooperative Company",
            "location": "Bafq, Iran",
            "period": "June 2023 – December 2023",
            "bullets": [
                "Developed and maintained managerial dashboards in Excel to monitor 10+ years of project data, including budgets, scope of work (SOW), progress tracking, and project duration.",
                "Prepared comprehensive reports (monthly, quarterly, and annual) to support data-driven decision-making and performance evaluation.",
                "Collaborated with project partners and stakeholders through regular meetings to align objectives, review progress, and address challenges."
            ]
        },
        {
            "title": "Data Analyst",
            "company": "Yazd University",
            "location": "Yazd, Iran",
            "period": "August 2022 – May 2023",
            "bullets": [
                "Investigated regulatory, legal, and social aspects of motorcycle use in Isfahan to inform evidence-based mobility policies.",
                "Applied machine learning techniques to accident data for predicting high-risk locations, identifying safety hazards, and uncovering key accident causes.",
                "Analysed spatial patterns of crashes to map hazard-prone areas and prioritize safety interventions.",
                "Proposed urban design and policy measures, including dedicated motorcycle lanes, restricted streets, and improved enforcement to enhance mobility and safety.",
                "Conducted a questionnaire survey to explore rider demographics, usage patterns, and behavioural factors, applying ML-based clustering for deeper insights."
            ]
        }
    ],
    
    "projects": [
        {
            "name": "TransitPath",
            "year": "2025",
            "description": "An advanced routing platform that computes realistic door-to-door travel paths by integrating GTFS transit data, walking networks, and time-dependent transfers. Provides optimal itineraries with second-by-second trajectory insights for researchers and planners.",
            "technologies": ["Python", "GTFS", "Routing", "Travel Planning", "Analytics", "Transit Operations"]
        },
        {
            "name": "GTFS Analysis Tool",
            "year": "2025",
            "description": "Enables researchers, planners, and developers to identify data issues, validate feed quality, and gain deeper insights into transit network structures.",
            "technologies": ["JavaScript", "GTFS", "Data Analysis", "Transit Planning"]
        },
        {
            "name": "Bus Electrification Tool",
            "year": "2025",
            "description": "An interactive planning tool that enables transit agencies to explore charging infrastructure and battery scenarios. Test different configurations, evaluate costs, and optimize fleet electrification strategies with data-driven insights.",
            "technologies": ["Python", "Shiny", "Optimization", "Transit Planning", "Electrification"]
        },
        {
            "name": "Headway Management Tool",
            "year": "2025",
            "description": "Developed in collaboration with TTC, this tool uses real-time GTFS data and predictive analytics to detect and mitigate bus bunching and gapping. Helps operators maintain consistent headways and improve service reliability across six pilot routes.",
            "technologies": ["Python", "GTFS", "Real-time Data", "Transit Operations", "Predictive Analytics"]
        },
        {
            "name": "15-Minute City Accessibility Toolkit",
            "year": "2025",
            "description": "An interactive platform that assesses and visualizes accessibility across Toronto using multimodal travel data, demographics, and facility distributions. Supports urban planning, equity analysis, and accessibility evaluation within the 15-minute city framework.",
            "technologies": ["Python", "Shiny", "OpenStreetMap", "GIS", "Urban Planning", "Accessibility Analysis"]
        }
    ],
    
    "awards": [
        {
            "name": "Transportation Achievement Award (TSMO)",
            "organization": "Institute of Transportation Engineers (ITE Canada)",
            "year": "2026",
            "for": "Real-time Decision Support for Transit Headway Management",
        },
        {
            "name": "1st Place, Open Data Challenge",
            "organization": "City of Toronto",
            "year": "2026",
            "for": "Transit Headway Management Platform",
        },
        {
            "name": "Project of the Year Award",
            "organization": "Institute of Transportation Engineers (ITE Toronto)",
            "year": "2025",
            "for": "Real-Time Application of AI in Correction of Bus Bunching at the TTC",
        },
        {
            "name": "Accepted to MSc Through Brilliant Talents Quota",
            "organization": "K.N. Toosi University of Technology",
            "for": "Admitted to the master's degree program through the Brilliant Talents quota.",
        },
        {
            "name": "2nd Rank, National Doctoral Entrance Exam",
            "organization": "National Doctoral Entrance Exam (Iran)",
            "for": "Achieved second rank in the national doctoral entrance examination.",
        },
    ],
    
    "publications": [
        {
            "title": "A comprehensive analysis of duplication in public transportation",
            "authors": "Barzegari, V., Taubkin, G.G., Barsukov, P. and Nourinejad, M.",
            "venue": "Transportation Research Part A: Policy and Practice, 204, p.104747",
            "year": "2026"
        },
        {
            "title": "Transit electrification through charger deployment, fleet type selection, and charging schedule optimization",
            "authors": "Barzegari, V. and Nourinejad, M.",
            "venue": "Energy, p.139181",
            "year": "2025"
        },
        {
            "title": "Public transportation fleet electrification and charger schedule optimization using a decomposition heuristic",
            "authors": "Naeimian, B., Mohseni, G., Barzegari, V., Nourinejad, M. and Park, P.Y.",
            "venue": "Energy, 333, p.137135",
            "year": "2025"
        },
        {
            "title": "Fleet cost and capacity effects of automated vehicles in mixed traffic networks: A system optimal assignment problem",
            "authors": "Barzegari, V., Edrisi, A. and Nourinejad, M.",
            "venue": "Transportation Research Part C: Emerging Technologies, 148, p.104020",
            "year": "2023"
        },
        {
            "title": "Subway System Usage by Elderly: Application of a Hybrid Choice Model",
            "authors": "Edrisi, A., Hayati Salout, M., Ganjipour, H. and Barzegari, V.",
            "venue": "Numerical Methods in Civil Engineering, 7(3), pp.78-93",
            "year": "2022"
        },
        {
            "title": "Optimal number and location of parking facilities in presence of autonomous vehicles",
            "authors": "Barzegari, V. and Edrisi, A.",
            "venue": "Numerical Methods in Civil Engineering, 7(1), pp.70-83",
            "year": "2022"
        },
        {
            "title": "Serial formation and parallel competition in public transportation",
            "authors": "Edrisi, A., Barzegari, V. and Nourinejad, M.",
            "venue": "Transportmetrica A: Transport Science, 17(4), pp.1193-1216",
            "year": "2021"
        }
    ],
    
    "skills": {
        "Optimization and Modelling": [
            "Mixed-integer Linear Programming (MILP)",
            "Decomposition Heuristics",
            "Scheduling Optimization",
            "Fleet Allocation",
            "Charger Allocation",
            "Transit Electrification Planning"
        ],
        "Programming and Tools": [
            "MATLAB", "Python", "Pandas", "NumPy", "Shiny",
            "Matplotlib", "Seaborn", "HTML", "CSS", "JavaScript",
            "GAMS", "Excel", "VBA"
        ],
        "Software": [
            "EMME", "Microsoft Office", "Excel", "Word", "PowerPoint"
        ],
        "Data Analysis and Machine Learning": [
            "Predictive Analytics", "Clustering", "Regression Analysis",
            "Accident Risk Modelling", "Demand Forecasting", "Spatial Analysis"
        ],
        "GIS and Mapping": [
            "QGIS", "OpenStreetMap", "Spatial Data Integration",
            "Urban Accessibility Analysis", "Transit Network Visualization"
        ],
        "Soft Skills": [
            "Communication", "Collaboration", "Presentation",
            "Independent Working", "Team Setting", "Problem-solving",
            "Public Engagement", "Technical Documentation", "Project Management"
        ]
    },
    
    "certificates": [
        {
            "name": "Databases and SQL for Data Science with Python",
            "issuer": "IBM (Coursera)",
            "date": "November 2025",
            "credential_id": "Q4PU2UKLKR5B"
        }
    ]
}


def create_cv_pdf(filename="Vahed_Barzegari_CV.pdf"):
    """Generate a professional CV PDF"""
    
    # Create PDF document
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Section heading style
    section_style = ParagraphStyle(
        'CustomSection',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=8,
        spaceBefore=16,
        fontName='Helvetica-Bold',
        borderColor=colors.HexColor('#1e40af'),
        borderWidth=0,
        borderPadding=0,
        leftIndent=0
    )
    
    # Job title style
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4,
        fontName='Helvetica-Bold'
    )
    
    # Company style
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=2,
        fontName='Helvetica'
    )
    
    # Date/location style
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#64748b'),
        spaceAfter=6,
        fontName='Helvetica-Oblique'
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#475569'),
        leftIndent=18,
        spaceAfter=4,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    # Normal text style
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#475569'),
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    # Contact info style
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#475569'),
        spaceAfter=3,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Add Header
    story.append(Paragraph(CV_DATA["name"], title_style))
    story.append(Paragraph(CV_DATA["title"], subtitle_style))
    
    # Add contact information
    contact_info = f"{CV_DATA['email']} | {CV_DATA['location']} | LinkedIn: {CV_DATA['linkedin']} | GitHub: {CV_DATA['github']}"
    story.append(Paragraph(contact_info, contact_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Add Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    story.append(Paragraph(CV_DATA["summary"], normal_style))
    story.append(Spacer(1, 0.15*inch))
    
    # Add Education
    story.append(Paragraph("EDUCATION", section_style))
    for edu in CV_DATA["education"]:
        degree_text = f"<b>{edu['degree']}</b>"
        if edu.get('field'):
            degree_text += f" - {edu['field']}"
        story.append(Paragraph(degree_text, job_title_style))
        story.append(Paragraph(edu["institution"], company_style))
        story.append(Paragraph(f"{edu['period']} | {edu['location']}", date_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.1*inch))
    
    # Add Work Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))
    for exp in CV_DATA["experience"]:
        story.append(Paragraph(f"<b>{exp['title']}</b>", job_title_style))
        story.append(Paragraph(exp["company"], company_style))
        story.append(Paragraph(f"{exp['period']} | {exp['location']}", date_style))
        for bullet in exp["bullets"]:
            story.append(Paragraph(f"• {bullet}", bullet_style))
        story.append(Spacer(1, 0.15*inch))
    
    # Add Projects
    story.append(Paragraph("KEY PROJECTS", section_style))
    for proj in CV_DATA["projects"]:
        story.append(Paragraph(f"<b>{proj['name']}</b> ({proj['year']})", job_title_style))
        story.append(Paragraph(proj["description"], normal_style))
        tech_text = f"<i>Technologies: {', '.join(proj['technologies'])}</i>"
        story.append(Paragraph(tech_text, date_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.1*inch))
    
    # Add Awards & Honors (newest year first; stable for ties)
    if CV_DATA.get("awards"):
        story.append(Paragraph("AWARDS & HONORS", section_style))
        for award in sorted(
            CV_DATA["awards"],
            key=lambda a: int(str(a.get("year", "0"))) if str(a.get("year", "0")).isdigit() else 0,
            reverse=True,
        ):
            aw_line = f"<b>{award['name']}</b> — {award['organization']}"
            if award.get("year"):
                aw_line += f", {award['year']}"
            story.append(Paragraph(aw_line, job_title_style))
            for_text = award.get("for")
            if for_text:
                story.append(Paragraph(f"For: “{for_text}”", normal_style))
            story.append(Spacer(1, 0.08*inch))
        story.append(Spacer(1, 0.05*inch))
    
    # Add Publications (selected/important ones)
    story.append(Paragraph("SELECTED PUBLICATIONS", section_style))
    # Show only first 5 publications to save space
    for pub in CV_DATA["publications"][:5]:
        pub_text = f"<b>{pub['title']}</b><br/>{pub['authors']}<br/><i>{pub['venue']}</i> ({pub['year']})"
        story.append(Paragraph(pub_text, normal_style))
        story.append(Spacer(1, 0.1*inch))
    
    # Add Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_style))
    skills_text_parts = []
    for category, skills_list in CV_DATA["skills"].items():
        skills_text_parts.append(f"<b>{category}:</b> {', '.join(skills_list)}")
    
    # Combine skills into paragraphs for better layout
    skills_combined = " | ".join(skills_text_parts)
    # Split into multiple paragraphs if too long
    story.append(Paragraph(skills_combined, normal_style))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Add Certificates
    if CV_DATA.get("certificates"):
        story.append(Paragraph("CERTIFICATIONS", section_style))
        for cert in CV_DATA["certificates"]:
            cert_text = f"<b>{cert['name']}</b><br/>{cert['issuer']} - {cert['date']}"
            if cert.get('credential_id'):
                cert_text += f" (ID: {cert['credential_id']})"
            story.append(Paragraph(cert_text, normal_style))
            story.append(Spacer(1, 0.1*inch))
    
    # Build PDF
    doc.build(story)
    print(f"CV PDF generated successfully: {filename}")


if __name__ == "__main__":
    create_cv_pdf()

