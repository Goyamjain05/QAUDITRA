from jinja2 import Environment, FileSystemLoader
import os

def generate_html_report(report_data, output_file='reports/audit_report.html'):
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    # Render HTML with report data
    html_output = template.render(report=report_data)


    # Ensure reports folder exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"✅ Report generated: {output_file}")
