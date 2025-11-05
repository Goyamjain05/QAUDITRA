class ScoreAgent:
    def calculate_score(self, findings):
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
