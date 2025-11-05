import pandas as pd
import re
import spacy
from quantum.quantum_mask import quantum_mask_string

nlp = spacy.load("en_core_web_sm")  # For named entity recognition

# Add more patterns
PATTERNS = {
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
    "Email": r"\b[\w.-]+@[\w.-]+\.\w{2,4}\b",
    "Phone": r"\b(?:\+91[\-\s]?|0)?[6-9]\d{9}\b",
    "Aadhaar": r"\b\d{4}\s?\d{4}\s?\d{4}\b",
    "PAN": r"\b[A-Z]{5}\d{4}[A-Z]\b"
}


def audit_file(file_path):
    findings = []
    df = pd.read_csv(file_path)
    masked_df = df.copy()

    for col in df.columns:
        for idx, val in enumerate(df[col].astype(str)):
            for pii_type, pattern in PATTERNS.items():
                if re.search(pattern, val):
                    masked_value = quantum_mask_string(val) if pii_type == "SSN" else None
                    findings.append({
                        "type": pii_type,
                        "column": col,
                        "row": idx,
                        "original": val,
                        "masked": masked_value
                    })
                    if masked_value:
                        masked_df.at[idx, col] = masked_value

            # Also detect names, dates via NLP (bonus)
            doc = nlp(val)
            for ent in doc.ents:
                if ent.label_ in ["PERSON", "DATE", "GPE"]:  # Person, Date, Location
                    findings.append({
                        "type": ent.label_,
                        "column": col,
                        "row": idx,
                        "original": ent.text,
                        "masked": None
                    })

    return findings, masked_df

