import pandas as pd
import re
import spacy

nlp = spacy.load("en_core_web_sm")

PATTERNS = {
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
    "Email": r"\b[\w.-]+@[\w.-]+\.\w{2,4}\b",
    "Phone": r"\b(?:\+91[\-\s]?|0)?[6-9]\d{9}\b",
    "Aadhaar": r"\b\d{4}\s?\d{4}\s?\d{4}\b",
    "PAN": r"\b[A-Z]{5}\d{4}[A-Z]\b"
}

class ScanAgent:
    def scan_file(self, file_path):
        df = pd.read_csv(file_path)
        findings = []
        for col in df.columns:
            for idx, val in enumerate(df[col].astype(str)):
                for pii_type, pattern in PATTERNS.items():
                    if re.search(pattern, val):
                        findings.append({
                            "type": pii_type,
                            "column": col,
                            "row": idx,
                            "original": val,
                            "masked": None
                        })

                doc = nlp(val)
                for ent in doc.ents:
                    if ent.label_ in ["PERSON", "DATE", "GPE"]:
                        findings.append({
                            "type": ent.label_,
                            "column": col,
                            "row": idx,
                            "original": ent.text,
                            "masked": None
                        })
        return df, findings
