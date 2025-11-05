from quantum.quantum_mask import quantum_mask_string

class MaskAgent:
    def apply_masking(self, df, findings):
        masked_df = df.copy()
        for f in findings:
            if f["type"] == "SSN" and f["masked"] is None:
                masked = quantum_mask_string(f["original"])
                f["masked"] = masked
                masked_df.at[f["row"], f["column"]] = masked
        return masked_df, findings
