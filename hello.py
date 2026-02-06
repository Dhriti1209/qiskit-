from qiskit import QuantumCircuit
# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

qc.h(0)        # Hadamard gate
qc.cx(0, 1)    # CNOT gate

print(qc)
