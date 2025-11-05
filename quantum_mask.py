from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer.backends.aer_simulator import AerSimulator

def quantum_mask_bit(bit_val: int) -> int:
    """
    Simulate quantum noise masking on a bit using Hadamard gate.
    """
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)

    if bit_val == 1:
        qc.x(0)  # Flip qubit if bit is 1

    qc.h(0)         # Apply Hadamard for superposition (randomness)
    qc.measure(0, 0)

    # Use new-style AerSimulator for Qiskit 1.x
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()

    return int(max(counts, key=counts.get))  # Return '0' or '1'


def quantum_mask_string(original: str) -> str:
    """
    Apply quantum_mask_bit to each digit in a string like SSN.
    """
    masked = ''
    for char in original:
        if char.isdigit():
            bit = int(char) % 2
            masked_bit = quantum_mask_bit(bit)
            masked += str(masked_bit)
        else:
            masked += char
    return masked
