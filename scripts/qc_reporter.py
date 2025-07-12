from reportlab.pdfgen import canvas
import os

def generate_reports(input_path, fixed_path, qc_results):
    # Set output path
    output_dir = "reports"
    os.makedirs(output_dir, exist_ok=True)  # ✅ Ensure the folder exists

    report_path = os.path.join(output_dir, "qc_problem_report.pdf")

    # Create PDF
    c = canvas.Canvas(report_path)
    c.setFont("Helvetica", 12)

    c.drawString(100, 800, "🎧 QC Problem Report")
    c.drawString(100, 780, f"Input File: {input_path}")
    c.drawString(100, 760, f"Fixed File: {fixed_path}")

    y = 740
    for key, value in qc_results.items():
        c.drawString(100, y, f"{key}: {value}")
        y -= 20

    # Save PDF
    c.save()

    return report_path
