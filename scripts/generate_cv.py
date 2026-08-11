from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT = "output/pdf/Kennedy-Mwangi-QA-CV.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4


styles = getSampleStyleSheet()
STYLES = {
    "Name": ParagraphStyle("Name", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=24, leading=28, textColor=colors.HexColor("#101828"), spaceAfter=4),
    "Title": ParagraphStyle("Title", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5, leading=14, textColor=colors.HexColor("#475467"), spaceAfter=7),
    "Contact": ParagraphStyle("Contact", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11, textColor=colors.HexColor("#475467")),
    "Section": ParagraphStyle("Section", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8.7, leading=10, textColor=colors.HexColor("#7c3aed"), spaceBefore=10, spaceAfter=5),
    "Body": ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica", fontSize=8.9, leading=12, textColor=colors.HexColor("#344054"), spaceAfter=3),
    "Role": ParagraphStyle("Role", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=colors.HexColor("#101828"), spaceBefore=5, spaceAfter=1),
    "Meta": ParagraphStyle("Meta", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=colors.HexColor("#667085"), spaceAfter=2),
    "Metric": ParagraphStyle("Metric", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=15, leading=17, textColor=colors.HexColor("#101828"), alignment=1),
    "MetricLabel": ParagraphStyle("MetricLabel", parent=styles["Normal"], fontName="Helvetica", fontSize=7.6, leading=9, textColor=colors.HexColor("#667085"), alignment=1),
}


def section(title):
    return Paragraph(title.upper(), STYLES["Section"])


def body(text):
    return Paragraph(text, STYLES["Body"])


def bullet(text):
    return Paragraph(f"- {text}", STYLES["Body"])


def role(company, title, period, bullets):
    items = [Paragraph(f"{company} - {title}", STYLES["Role"]), Paragraph(period, STYLES["Meta"])]
    items.extend(bullet(item) for item in bullets)
    return items


def paint_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.white)
    canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#667085"))
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_WIDTH - 15 * mm, 8 * mm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=15 * mm,
    leftMargin=15 * mm,
    topMargin=14 * mm,
    bottomMargin=13 * mm,
)

story = [
    Paragraph("Kennedy Mwangi", STYLES["Name"]),
    Paragraph("Quality Assurance Engineer | QA Leadership | Test Automation | API & Data Validation", STYLES["Title"]),
    Paragraph("Nairobi, Kenya | kenmwas7@gmail.com | +254 726 156 420 | linkedin.com/in/mwangi-k-847b24295 | github.com/Kmwas", STYLES["Contact"]),
    Spacer(1, 6),
    section("Professional Summary"),
    body("Quality Assurance Engineer with 10+ years of experience delivering reliable web, mobile, API-led, and data-heavy software across humanitarian technology, e-commerce, telco, fintech, and enterprise environments. Strong record in QA leadership, Cypress automation, regression strategy, API and database validation, performance testing, CI feedback loops, and stakeholder-ready release communication."),
    section("Selected Impact"),
]

metrics = [
    ("9", "Junior QAs mentored"),
    ("50%", "Manual regression reduction"),
    ("35%", "Test efficiency improvement"),
    ("30%", "Production bug reduction"),
]
metric_table = Table(
    [[Paragraph(value, STYLES["Metric"]) for value, _ in metrics], [Paragraph(label, STYLES["MetricLabel"]) for _, label in metrics]],
    colWidths=[42 * mm] * 4,
)
metric_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f7f5ff")),
            ("BOX", (0, 0), (-1, -1), 0.25, colors.HexColor("#d8ccff")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#d8ccff")),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]
    )
)
story.extend([metric_table, section("Core Skills")])

skills = [
    ["Quality Engineering", "Test strategy, risk-based testing, exploratory testing, regression, UAT, release validation, requirements analysis"],
    ["Automation", "Cypress, Selenium, Katalon Studio, Webdriver.io, reusable frameworks, CI and continuous testing pipelines"],
    ["API & Data Quality", "Postman, REST APIs, SQL, Postgres, MySQL, database validation, data integrity, business-rule validation"],
    ["Leadership & Delivery", "QA planning, KPIs, mentoring, Jira, TestRail, HP Quality Center, Bugzilla, Asana, GitHub, Bitbucket"],
]
skills_table = Table([[Paragraph(left, STYLES["Meta"]), Paragraph(right, STYLES["Body"])] for left, right in skills], colWidths=[39 * mm, 129 * mm])
skills_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), 0.25, colors.HexColor("#d7d9df")), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
story.extend([skills_table, section("Experience")])

story.extend(role("International Rescue Committee", "Quality Assurance Analyst", "2026 - Present | Nairobi", [
    "Assure quality across data-driven products and workstreams involving dashboards, calculations, configurations, APIs, workflows, and releases.",
    "Use cross-layer validation to compare UI behaviour, API responses, backend data, and business rules where product risk is highest.",
]))

story.extend(role("Nathan Digital", "QA Lead", "Dec 2023 - 2026 | Nairobi", [
    "Managed QA across multiple high-profile projects while mentoring 9 junior QAs across test design, debugging, automation, and delivery discipline.",
    "Implemented standardized test documentation and automation practices, contributing to a 35% improvement in test efficiency.",
    "Expanded Cypress automation coverage, reducing manual regression testing by 50% and speeding release cycles.",
    "Supported CI and continuous testing pipelines, reducing developer feedback loops and average bug-fix time by 25%.",
]))

story.extend(role("Copia Global", "Senior QA Engineer", "Jan 2022 - Oct 2023 | Tatu City", [
    "Implemented Cypress automation, cutting testing time by 40% and improving release speed.",
    "Reduced production bugs by 30% through early-stage testing and close developer collaboration.",
    "Developed test plans for 50+ projects and supported performance testing that improved platform scalability.",
]))

story.append(PageBreak())
story.extend(role("Wasoko", "Senior QA Engineer", "Jul 2019 - Dec 2021 | Nairobi", [
    "Led functional and regression testing across multiple platforms, increasing release accuracy through structured validation.",
    "Automated 100+ test scripts using Webdriver.io, reducing manual testing hours and improving execution consistency.",
    "Built a test case repository and worked with cross-functional teams to support predictable delivery.",
]))

story.extend(role("Safaricom PLC", "QA Engineer", "Oct 2018 - Jul 2019 | Nairobi", [
    "Supported QA for major projects including Safaricom Selfcare and Masoko.",
    "Automated repetitive test cases using Katalon and strengthened data integrity through database testing.",
    "Worked with users and delivery teams to understand product needs and improve release quality.",
]))

story.extend(role("M-Kopa", "QA Engineer", "Mar 2015 - Oct 2018 | Nairobi", [
    "Created regression suites, verified resolved defects, and supported multiple product releases.",
    "Reduced issue resolution time through close collaboration with support and development teams.",
    "Improved product quality by identifying defects early and communicating quality concerns clearly across teams.",
]))

story.extend([
    section("Education"),
    body("<b>Bachelor of Science in Information Technology</b> - Mount Kenya University, Second Class, Upper Division"),
    section("Portfolio Themes"),
    bullet("Data quality: scenario-based coverage for reporting logic, calculations, configuration, and backend validation."),
    bullet("Automation: maintainable Cypress, Katalon, Selenium, and Webdriver.io coverage around repeatable risk areas."),
    bullet("Leadership: QA standards, KPIs, risk assessment, mentoring, release readiness, and stakeholder communication."),
])

doc.build(story, onFirstPage=paint_page, onLaterPages=paint_page)
