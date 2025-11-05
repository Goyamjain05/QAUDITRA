import os
from joblib import Parallel, delayed
from agents.audit_agent import audit_file





def calculate_score(findings):
    score = 0
    for f in findings:
        if f['type'] == 'SSN':
            score += 10
        elif f['type'] == 'Email':
            score += 5
        elif f['type'] in ['Aadhaar', 'PAN']:
            score += 8
        elif f['type'] == 'Phone':
            score += 6
        elif f['type'] in ['PERSON', 'DATE', 'GPE']:
            score += 3
    return min(score, 100)

def run_parallel_audit(data_folder='data'):
    files = [
        os.path.join(data_folder, file)
        for file in os.listdir(data_folder)
        if file.endswith('.csv')
    ]

    print(f"🧾 Found {len(files)} files to audit...")

    results = Parallel(n_jobs=-1)(  # Use all available cores
        delayed(audit_file)(file)
        for file in files
    )

    # Combine results into a dict { filename: findings }
    audit_report = {}
    for i, file in enumerate(files):
        findings, _ = results[i]
        audit_report[file] = findings

    return audit_report
