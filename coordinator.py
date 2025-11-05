import os
from agents.ai_agents.scan_agent import ScanAgent
from agents.ai_agents.mask_agent import MaskAgent
from agents.ai_agents.score_agent import ScoreAgent
from agents.ai_agents.report_agent import ReportAgent

class CoordinatorAgent:
    def __init__(self):
        self.scan_agent = ScanAgent()
        self.mask_agent = MaskAgent()
        self.score_agent = ScoreAgent()
        self.report_agent = ReportAgent()

    def run_audit(self, data_folder='data'):
        report = {}

        files = [
            os.path.join(data_folder, f)
            for f in os.listdir(data_folder)
            if f.endswith('.csv')
        ]

        for file in files:
            df, findings = self.scan_agent.scan_file(file)
            masked_df, findings = self.mask_agent.apply_masking(df, findings)
            score = self.score_agent.calculate_score(findings)

            total_rows = len(df)
            total_columns = len(df.columns)
            total_cells = total_rows * total_columns
            total_issues = len(findings)

            risk_percent = (total_issues / total_cells) * 100 if total_cells > 0 else 0

            report[file] = {
                "findings": findings,
                "score": score,
                "total_issues": total_issues,
                "risk_percent": f"{risk_percent:.1f}"
            }

            

        #self.report_agent.generate_report(report)
