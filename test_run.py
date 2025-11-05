from core.parallel_audit import run_parallel_audit
from core.report_generator import generate_html_report

report = run_parallel_audit('data')
generate_html_report(report)

print("📄 Audit completed. Open reports/audit_report.html in your browser.")
