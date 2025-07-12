
from reportlab.pdfgen import canvas
import os

def generate_reports(original, fixed, qc_results):
    report_path = "outputs/reports/qc_report.pdf"
    c = canvas.Canvas(report_path)
    c.drawString(100, 800, "QC Report")
    for i, (k,v) in enumerate(qc_results.items()):
        c.drawString(100, 780 - i*20, f"{k}: {v}")
    c.save()
    return {"QC Report (PDF)": report_path}
