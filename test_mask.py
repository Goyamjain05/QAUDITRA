from quantum.quantum_mask import quantum_mask_string

original_ssn = "123-45-6789"
masked_ssn = quantum_mask_string(original_ssn)

print(f"Original SSN: {original_ssn}")
print(f"Masked SSN:   {masked_ssn}")
